---
name: lambdas-vs-closures
layout: post
title: Lambdas vs. Closures
time: 2010-07-13 23:21:00 +01:00
categories: java tempus-fugit
comments: true
sidebar : false
description: "What's the difference between a lambda and a closure? Find out here!"
keywords: "lambda vs closures, closures vs lambdas, functional style java, higher order functions, pure functions"
---

{% img right ../../../../../images/lambda.png 'The Lambda greek character'%}

When writing Java in a functional style, things tend to get very verbose. We often create a bunch of anonymous implementation fragments and pass them around akin to a _function_ in functional languages. These fragments often get called closures or lambdas, but what's the difference between the two terms?

<!-- more -->

Lets take the `WaitFor` class from [tempus-fugit](http://tempusfugitlibrary.org/) as an example where we pass an anonymous instance as a parameter to the `waitOrTimeout` method. We define a function here that will be called at some later point by `waitOrTimeout`. We can think of this as _lazy invocation_. Java isn't a functional language but we've simulated at least one characteristic of a functional language using `WaitFor` and an anonymous function. We've created a _higher order function_ but not necessarily a _pure function_ ([1]({{ root_url }}/blog/2012/04/03/scala-as-a-functional-oo-hybrid/)).

For example,
  
{% codeblock lang:java %}
...
server.start();
WaitFor.waitOrTimeout(new Condition() {
   @Override
   public boolean isSatisfied() {
      return server.isRunning();
   }
}, timeout(seconds(5)));
{% endcodeblock %}


The anonymous class implementing `Condition` is evaluated by the method `waitOrTimeout` (which will call the `isSatisfied`) method.

The recent shift to this functional style has lead to eager anticipation of JDK7 and the promise of closures. More accurately however, it's the inclusion of _lambdas_ that we're waiting for, not _closures_. Closures have in fact been available in Java since 1.1, so what's the difference?


### Lambs to the Slaughter

So, we want to be able to define anonymous functions on the fly, the result of the function is purely dependent on it's arguments and this is called a lambda. Those functions that depend on external values (not just it's arguments) are when closures come into it. The act of binding those external values to the anonymous function is referred to as _closure_. After closure, when all variables have been captured and bound to the function, the term is closed.

  
For example, the code snippet above will return a new `Condition` instance on each invocation. Because it will bind the variable server to the anonymous function, it will return a closure. To put it another way, we'll extract the anonymous part to a method to explicitly create a new instance, such

  
{% codeblock lang:java %}
private static Condition isRunning(final Server server) {
   return new Condition() {
      @Override
      public boolean isSatisfied() {
         return server.isRunning();
      }
   };
}
{% endcodeblock %}

This should make it more obvious that the variable outside the scope of the anonymous `Condition` is required (the `server` variable), each call to the `isRunning` method will return a closure over the argument, the instance of which captures the value of server. Java implements the closure by passing a reference to the outer scoped (lets say `Foo.class`) to the anonymous class (`Foo$1.class`). The `access$000` call accesses the appropriate private field in the outer class directly in the bytecode

  
{% codeblock lang:java %}
class Foo$1 implements Condition {

    final Foo this$0;

    Foo$1() {
        this$0 = Foo.this;
        super();
    }

    public boolean isSatisfied() {
        return Foo.access$000(Foo.this).isRunning();
    }
}
{% endcodeblock %}


  
So, if, we have update the example again, this time removing the out of scope variable, we're left with something like this;

{% codeblock lang:java %}
private static Condition isRunning() {
   return new Condition() {
      @Override
      public boolean isSatisfied() {
         return true; // optimistic!
      };
   }
}
{% endcodeblock %}


Then no out of scope variables are required, the term doesn't need to be closed. The anonymous function that is left is effectively a lambda.

  
What JDK7 will (finger's crossed) bring is more explicit, concise way of expressing the same ideas. It will support lambdas as a language feature although I can't quite figure out what the example would look like in those terms. See the [straw man proposal](http://cr.openjdk.java.net/%7Emr/lambda/straw-man/) and see if you can figure it out!





