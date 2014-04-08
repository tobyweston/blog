---
layout: post
title: "Currying Functions in Java & Scala"
date: 2013-07-21 06:58
comments: true
categories: java scala java8
sidebar: false
published: true
keywords: "curried function, partial application, java, scala, functional programming"
description: "Currying in Java and Scala. A quick look at what curried functions are and how you'd curry a Java function and it's counterpart in Scala."
---

Currying is the technique of transforming a function with multiple arguments into a function with just one argument. The single argument is the value of the first argument from the original function and the function returns another single argument function. This in turn would take the second original argument and itself return another single argument function. This chaining continues over the number of arguments of the original. The last in the chain will have access to all of the arguments and so can do whatever it needs to do.

You can turn any function with multiple arguments into it's curried equivalent. Let's have a look at this in action.

<!-- more -->


## Java

For example, in Java, you can convert

{% codeblock lang:java %}
public static int add(int a, int b) {
    return a + b;
}
{% endcodeblock %}

into something like this (where `Function<A, B>` defines a single method `B apply(A a)`).

{% codeblock lang:java %}
public static Function<Integer, Function<Integer, Integer>> add() {
    return new Function<Integer, Function<Integer, Integer>>() {
        @Override
        public Function<Integer, Integer> apply(final Integer x) {
            return new Function<Integer, Integer>() {
                @Override
                public Integer apply(Integer y) {
                    return x + y;
                }
            };
        }
    };
}
{% endcodeblock %}

In Java 8, it's much less verbose using the new lambda syntax.

{% codeblock lang:java %}
public static Function<Integer, Function<Integer, Integer>> add() {
    return x -> y -> x + y;
}
{% endcodeblock %}


Calling the original method

{% codeblock lang:java %}
add(1, 1);                       // gives 2
{% endcodeblock %}

and calling the curried version

{% codeblock lang:java %}
add();                          // gives back a instance of Function<[A, B]>
add().apply(1);                 // gives back a instance of Function<[A, B]>
add().apply(1).apply(1)         // gives 2
{% endcodeblock %}


## Scala

In Scala, the regular uncurried function would look like this.

{% codeblock lang:scala %}
def add(x: Int, y: Int): Int = {
  x + y
}
{% endcodeblock %}


As Scala supports curried functions, you can turn this into it's curried version simply by separating out the arguments.


{% codeblock lang:scala %}
// shorthand
def add(x: Int)(y: Int): Int = {
  x + y
}
{% endcodeblock %}

Which is shorthand for writing it out like this.

{% codeblock lang:scala %}
// longhand
def add(x: Int): (Int => Int) = {
  (y: Int) => {
    x + y
  }
}
{% endcodeblock %}


Using the REPL to show how they're called;

{% codeblock lang:sh %}
scala> def add(x: Int)(y: Int): Int = {
     |   x + y
     | }
add: (x: Int)(y: Int)Int

scala> add(1) _
res1: Int => Int = <Function>

scala> (add(1) _).apply(1)
res2: Int = 2

scala> add(1)(1)
res3: Int = 2
{% endcodeblock %}

and working with the longhand version;

{% codeblock lang:sh %}
scala> def add2(x: Int): (Int => Int) = {
     |   (y: Int) => {
     |     x + y
     |   }
     | }
add2: (x: Int)Int => Int

scala> add2(1).apply(1)
res4: Int = 2
{% endcodeblock %}


It turns out that it's this partial application of functions that's really interesting. Currying in Scala allows us to defer execution and reuse functions. We'll have a look at that in the next article.


## More Information

 * [Gist](https://gist.github.com/tobyweston/6027570)
 * [Function Currying in Scala](http://www.codecommit.com/blog/scala/function-currying-in-scala)
 * [Currying and Partially Applied Functions](http://danielwestheide.com/blog/2013/01/30/the-neophytes-guide-to-scala-part-11-currying-and-partially-applied-functions.html)