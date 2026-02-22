---
title: "Abstracting ReentrantReadWriteLock"
pubDate: "2009-08-01"
categories: 'java concurrency'
keywords: "Java ReentrantReadWriteLock, read write lock, concurrency, locks, synchronized, tempus-fugit, thread safety"
description: "Java's ReentrantReadWriteLock allows concurrent reads but serialised writes. Learn how to abstract the lock boilerplate safely using try/finally blocks."
---

All locks in Java are reentrant. They have to be in so that the owner of a monitor can reenter protected code. If a thread requests a lock that it already holds, it'll be given it. Without this, a subclass couldn't override a snynchronised method and then call the superclass method without deadlocking.
  
Java's [ReentrantReadWriteLock](http://java.sun.com/javase/6/docs/api/java/util/concurrent/locks/ReentrantReadWriteLock.html) is about acquiring separate read and write locks for efficiency. For example, in the case where you may have infrequent writes but frequent reads, it _may_ be more efficient to not synchronise all access with just one lock. Instead, [ReentrantReadWriteLock](http://java.sun.com/javase/6/docs/api/java/util/concurrent/locks/ReentrantReadWriteLock.html) can allow all read access to only block when a write is taking place. You'll end up with multiple simultaneous reads but synchronised writes and all the reads will have guaranteed visibility of the writes.

With all [Lock](http://java.sun.com/javase/6/docs/api/java/util/concurrent/locks/Lock.html) implementations, you specifically acquire the lock and are politely asked to release the lock within a finally block. Makes sense but gives unlock responsibility on the developer.

  
Vanilla Java would have you;


``` java
Lock l = ...;
l.lock();
try {
    // access the resource protected by this lock
} finally {
    l.unlock();
}
```

Why not wrap the boiler plate code up in a mini DSL and pass in a lambda to execute the cleanup? Any implementation must call both lock and unlock and re-throw any exceptions. The following test shows this to be true.


``` java
@RunWith(JMock.class)
public class ExecuteUsingLockTest {

    private final Mockery context = new JUnit4Mockery() {{
        setImposteriser(ClassImposteriser.INSTANCE);
    }};

    ReadLock readLock = context.mock(ReadLock.class);
    WriteLock writeLock = context.mock(WriteLock.class);

    @Test
    public void readLock() {
        setExpectationsOn(readLock);
        execute(something()).using(readLock);
    }

    @Test
    public void writeLock() {
        setExpectationsOn(writeLock);
        execute(something()).using(writeLock);
    }

    @Test (expected = Exception.class)
    public void readLockThrowingException() throws Exception {
        setExpectationsOn(readLock);
        execute(somethingThatThrowsException()).using(readLock);
    }

    @Test(expected = Exception.class)
    public void writeLockThrowingException() throws Exception {
        setExpectationsOn(writeLock);
        execute(somethingThatThrowsException()).using(writeLock);
    }

    private Callable<Void, RuntimeException> something() {
        return new Callable<Void, RuntimeException>() {
            public Void call() throws RuntimeException {
                return null;
            }
        };
    }

    private Callable<Void, Exception> somethingThatThrowsException() {
        return new Callable<Void, Exception>() {
            public Void call() throws Exception {
                throw new RuntimeException("bad robot");
            }
        };
    }

    private void setExpectationsOn(final Lock lock) {
        context.checking(new Expectations() {{
            one(lock).lock();
            one(lock).unlock();
        }});
    }
}
```

The implementation is fairly straight forward with a couple of interesting points to note around generics.

    
``` java
public class ExecuteUsingLock<T, E extends Exception> {

    private final Callable<T, E> callable;

    private ExecuteUsingLock(Callable<T, E> callable) {
        this.callable = callable;
    }

    public static <T, E extends Exception> ExecuteUsingLock<T, E> execute(Callable<T, E> callable) {
        return new ExecuteUsingLock<T, E>(callable);
    }

    public T using(ReentrantReadWriteLock.WriteLock write) throws E {
        try {
            write.lock();
            return callable.call();
        } finally {
            write.unlock();
        }
    }

    public T using(ReentrantReadWriteLock.ReadLock read) throws E {
        try {
            read.lock();
            return callable.call();
        } finally {
            read.unlock();
        }
    }
}
```

  
Having the [micro-DSL](/blog/2009-02-16-more-on-micro-dsls/) pass in the generic `Callable` on the static constructor meant that I couldn't make just the method generic and instead had to link the types by making the class definition generic. You might also notice that the `Callable` used isn't Java's `Callable`, as Sun saw fit not to have the `Exception` as a generic type.

 By creating a new `Callable` interface with a generic exception, I was able to neaten up the DSL so that we're not forced to throw `Exception` from a method that uses the `ExecuteUsingLock` class. Instead, you define your closure function to throw `RuntimeException`.

  
A real world example might be something that updates a status probe where the variable lock below is an instance of `ReentrantReadWriteLock`.

    
``` java
public void setStatus(final Status status) {
    execute(settingStatus(status)).using(lock.writeLock());
}

public String getStatus() {
    return execute(gettingStatus()).using(lock.readLock());
}

private Callable<Void, RuntimeException> settingStatus(final Status status) {
    return new Callable<Void, RuntimeException>() {
        public Void call() {
            EnclosingClass.this.status = status;
            return null;
        }
    };
}

private Callable<Status, RuntimeException> gettingStatus() {
    return new Callable<Status, RuntimeException>() {
        public Status call() {
            return EnclosingClass.this.status.toString();
        }
    };
}
```

All this to avoid the boiler plate code. You can try it for yourself by using the [tempus-fugit](http://tempusfugitlibrary.org/) project.

