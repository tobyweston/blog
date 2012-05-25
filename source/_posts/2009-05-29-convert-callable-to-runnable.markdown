---
name: convert-callable-to-runnable
layout: post
title: Convert a Callable to a Runnable
time: 2009-05-29 21:37:00 +01:00
categories: java object-oriented tempus-fugit
comments: true
sidebar : false
---

Every time I come across it, it bugs me.
  
The `Executors` class has helper methods to convert from a `Runnable` to a
`Callable`, presumably so you can submit an old school `Runnable` task to an
executor, but I can never find the counterpart helper. Something to convert a
`Callable` to a `Runnable`.

  
I seem to keep finding myself needing one and you might think me silly for
doing so but it's because I'm into the habit of coding as `Callable`s now. I
tend to think of `Runnable` as simply something that can run, not in terms of a
`Thread` or concurrent task. I like the way I think about `Runnable`.

Lets have a go at converting `Callable` to a `Runnable`.

<!-- more -->

`Callable` is like the new cool kid, with its funky return value and the ability
to throw an exception. Wow, why did I ever bother with `Runnable` in the first
place? `Callable`, like `Runnable`, however is still just something that can be
called, it just so happens to fit in nicely with the executor framework and
kind of looks all bling.

  
I digress... back to jusitifying why I think I'm always needing to convert
from `Callable` to `Runnable`. As I say, if both interfaces represent something
that can be called, I favour `Callable` becuase its more powerful. I can return
useful things and catch useful exceptions. I'm in the habit of using `Callable`.

  
Often then, I'll have utility classes, useful nuggets of functionality dressed
up as a `Callable`, and if I want to schedule them with an executor with a fixed
delay or fixed rate, I can't. The interface wants a `Runnable` and only a
`Runnable`. Most likely becuase it doesn't really make much sense to schedule a
fixed rate execution of a task that returns something when it would take quite
some thinking to actually do something with the return value.

  
None the less, I'd like to schedule something at a fixed rate (ignoring the
result) that I also schedule elsewhere and actually do something with the
result.

  
Starting with the tests, any helper must delegate to the `Callable` and handle
any exceptions.

    
{% assign braces = '{{' %}
{% codeblock lang:java %}
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
      context.checking(new Expectations() {{ braces }}
         one(callable).call(); will(action);
      }});
   }
}
{% endcodeblock %}


  
To get a green light, the implementation is fairly trivial.


{% codeblock lang:java %}
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
{% endcodeblock %}


  
Let me know if you've got any comments, great ideas on the subject or can
improve on the implementation above.


__Update__: Since writing this entry, I created the[ tempus-fugit](http://code.google.com/p/tempus-fugit/) project to
capture these kinds of ideas.




