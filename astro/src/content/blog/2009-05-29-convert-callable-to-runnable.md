---
title: "Convert a Callable to a Runnable"
pubDate: "2009-05-29"
categories: 'java concurrency'
keywords: "Java Callable, Runnable, Executors, scheduled executor, fixed rate, tempus-fugit, concurrency"
description: "The Executors framework can convert Runnable to Callable but not the reverse. Here's how to wrap a Callable as a Runnable to schedule it at a fixed rate."
---

The `Executors` class has helper methods to convert from a `Runnable` to a `Callable`, presumably so you can submit a `Runnable` task to an executor, but it doesn't offer the counterpart helper. Something to convert a `Callable` to a `Runnable`.


`Callable`, like `Runnable`, is still just something that can be called. It offers a return type but really has nothing to do with concurrency, it just so happens to fit in nicely with the executor framework like `Runnable` does with `Thread`.


Often I'll have utility classes, useful nuggets of functionality dressed up as a `Callable`, and if I want to schedule them with an executor with a fixed delay or fixed rate, I can't. The interface wants a `Runnable` and only a `Runnable`. Most likely because it doesn't really make much sense to schedule a fixed rate execution of a task that returns something when it would take quite some thinking to actually do something with the return value.

  
None the less, I'd like to schedule something at a fixed rate (ignoring the result) that I also schedule elsewhere and actually do something with the result.

## Test First
  
Starting with the tests, any helper must delegate to the `Callable` and handle any exceptions.

    
``` java
@RunWith(JMock.class)
public class CallableAdapterTest {
   private final Mockery context = new Mockery();
   private final Callable callable = context.mock(Callable.class);

   private static final Object RESULT = new Object();

   @Test
   public void delegates() throws Exception {
      callableWill(returnValue(RESULT));
      runnable(callable).run();
   }

   @Test(expected=RuntimeException.class)
   public void exceptionBubblesUp() throws Exception {
      callableWill(throwException(new Exception()));
      runnable(callable).run();
   }

   private void callableWill(final Action action) throws Exception {
      context.checking(new Expectations() {{
         one(callable).call(); will(action);
      }});
   }
}
```

## The Code
  
To get a green light, the implementation is fairly trivial.


``` java
public class CallableAdapter {

   public static Runnable runnable(final Callable callable) {
      return new Runnable() {
         @Override
         public void run()
            try
               callable.call();
            } catch (Exception e) {
               throw new RuntimeException(e);
            }
         }
      };
   }
}
```

You can find the code in the [tempus-fugit](http://tempusfugitlibrary.org/) project.




