---
name: lamdas-vs-closures
layout: post
title: Lamdas vs. Closures
time: 2010-07-13 23:21:00 +01:00
categories: java tempus-fugit
---

When writing Java in a functional style, apart from the verbosity of it all,
it always bugged me about the terminology we use. I tend to talk about
closure-like arguments but revisiting some old University materials when
clearing out the loft, I've adjusted my vocabulary somewhat. Taking the
`WaitFor` class from [tempus-fugit](http://code.google.com/p/tempus-fugit/)
as an example, passing an anonymous class instance as a parameter to a method
 that will later call the instance is a kind of functional programming. I say
  kind-of because its not really functional programming,
  Java isn't a functional language but we can bend it into a style that's similar. For example,
  
{% codeblock lang:java %}
...
server.start();
waitOrTimeout(new Condition() {
   @Override
   public boolean isSatisfied() {
      return server.isRunning();
   }
}, timeout(seconds(5)));
{% endcodeblock %}


The anonymous class implementing `Condition` is evaluated by the method
`waitOrTimeout` (it's that which will call the `isSatisfied`) method.

The recent shift to this functional style has lead to eager anticipation of
JDK7 and the promise of closures. More accurately however, it's the inclusion
of _lamdas_ that we're waiting for, not _closures_. Closures have in fact been
available in Java since 1.1, so what's the difference?

<!-- more -->

### Lambs to the Slaughter

  
So, we want to be able to define anonymous functions on the fly, the result of
the function is purely dependent on it's arguments and this is called a lamda.
Those functions that depend on external values (not just it's arguments) are
when closures come into it. The act of binding those external values to the
anonymous function is referred to as _closure_. After closure, when all
variables have been captured and bound to the function, the term is closed.

  
For example, the code snippet above will return a new `Condition` instance on
each invocation. Because it will bind the variable server to the anonymous
function, it will return a closure. To put it another way, we'll extract the
anonymous part to a method to explicitly create a new instance, such

  
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

This should make it more obvious that the variable outside the scope of the
anonymous `Condition` is required (the server variable), each call to the
`isRunning` method will return a closure over the argument, the instance of
which captures the value of server. Java implements the closure by passing a
reference to the outer scoped (lets say `Foo.class`) to the anonymous class
(`Foo$1.class`). The `access$000` call accesses the appropriate private field
 in the outer class directly in the bytecode

  
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


  
So, if, we have update the example again, this time removing the out of scope
variable, we're left with something like this;

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


Then no out of scope variables are required, the term doesn't need to be
closed. The anonymous function that is left is effectively a lamda.

  
What JDK7 will (finger's crossed) bring is more explicit, concise way of
expressing the same ideas. It will support lamdas as a language feature
although I can't quite figure out what the example would look like in those
terms. See the [straw man proposal](http://cr.openjdk.java.net/%7Emr/lambda
/straw-man/) and see if you can figure it out!


{% img http://4.bp.blogspot.com/_-uMxV_fCbC4/SVInGoVdYJI/AAAAAAAAC08/I4RV1KzCyPo/s320/gibble_22x22.png %}


