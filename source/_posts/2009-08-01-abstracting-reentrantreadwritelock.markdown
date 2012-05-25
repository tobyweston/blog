---
name: abstracting-reentrantreadwritelock
layout: post
title: Abstracting ReentrantReadWriteLock
time: 2009-08-01 10:47:00 +01:00
categories: java concurrency tempus-fugit
comments: true
sidebar : false
---

All locks in Java are reentrant, they have to be in case the owner of the monitor ends up calling a method that needs that monitor. So, if a thread requests a lock that it already holds, it'll be given it. Without this, a subclass couldn't override a snynchronised method and then call the superclass method without deadlocking.
  
Java's [ReentrantReadWriteLock](http://java.sun.com/javase/6/docs/api/java/util/concurrent/locks/ReentrantReadWriteLock.html) is about acquiring seperate
read and write locks for efficiency. For example, in the case where you may
have infrequent writes but frequent reads, it _may_ be more efficient to not
synchronise all access with just one lock. Instead, [ReenstrantReadWriteLock](http://java.sun.com/javase/6/docs/api/java/util/concurrent/locks/ReentrantReadWriteLock.html) can allow all read access to only block when a write is taking
place. You'll end up with multiple simultaneous reads but synchronised writes
and all the reads will have guaranteed visibility of the writes.

With all [Lock](http://java.sun.com/javase/6/docs/api/java/util/concurrent/locks/Lock.html) implementations, you specifically acquire the lock and are
politely asked to release the lock within a finally block. Makes sense but it
always bugs me that we're forced into Java's verbosity trap, yet again.

  
So, vanilla Java would have you;


{% codeblock lang:java %}
Lock l = ...;
l.lock();
try {
    // access the resource protected by this lock
} finally {
    l.unlock();
}
{% endcodeblock %}


So why not wrap the boiler plate code up in a micro-DSL and pass a closure to execute? Any implementation must
call both lock and unlock and re-throw any exceptions. The following test shows this to be true.

<!-- more -->

{% assign braces = '{{' %}
{% codeblock lang:java %}
@RunWith(JMock.class)
public class ExecuteUsingLockTest {

    private final Mockery context = new JUnit4Mockery() {{ braces }}
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
        context.checking(new Expectations() {{ braces }}
            one(lock).lock();
            one(lock).unlock();
        }});
    }
}
{% endcodeblock %}


The implementation is fairly straight forward with a couple of interesting
points to note around generics.

    
{% codeblock lang:java %}
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
{% endcodeblock %}


  
Having the [micro-DSL]({{ root_url }}/blog/2009/02/16/more-on-micro-dsls/) pass in the generic `Callable` on the static constructor meant that I
couldn't make just the using method generic and instead had to link the types
by making the class definition generic. You might also notice that the
`Callable` used isn't Java's `Callable`, as Sun saw fit not to have the `Exception`
as a generic type. By creating a new `Callable` interface with a generic exception, I was able to
neaten up the DSL so that we're not forced
to throw `Exception` from a method that uses the `ExecuteUsingLock` class. Instead, you define your closure
function to throw `RuntimeException`.

  
A real world example might be something that updates a status probe where the
variable lock below is an instance of `ReentrantReadWriteLock`.

    
{% codeblock lang:java %}
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
{% endcodeblock %}


All this to avoid the boiler plate code! Fresh.

__Update__: Since writing this entry, I created the [tempus-fugit](http://code.google.com/p/tempus-fugit/) project to
capture these kinds of ideas.

  


