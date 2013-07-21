---
layout: post
title: "Currying Functions for Happy Times"
date: 2013-07-17 06:58
comments: true
categories: java scala
sidebar: false
published: false
description: ""
keywords: "loan pattern"
---

Currying is the technique of transforming a function with multiple arguments into a function with just one argument which takes the first argument of the original function and returns another single argument function. This chaining continues over the number of arguments of the original. The last in the chain will have access to all of the arguments and so can do whatever it needs to do.

You can turn any function with multiple arguments into it's curried equivalent.

## Java

For example, in Java, you can convert

{% codeblock lang:java %}
public static int add(int a, int b) {
    return a + b;
}
{% endcodeblock %}

into something like this (where `Function1<A, B>` defines a single method `B apply(A a)`).

<!-- more -->
{% codeblock lang:java %}
public static Function1<Integer, Function1<Integer, Integer>> add() {
    return new Function1<Integer, Function1<Integer, Integer>>() {
        @Override
        public Function1<Integer, Integer> apply(final Integer x) {
            return new Function1<Integer, Integer>() {
                @Override
                public Integer apply(Integer y) {
                    return x + y;
                }
            };
        }
    };
}
{% endcodeblock %}


Calling the original method

{% codeblock lang:java %}
add(1, 1);                       // gives 2
{% endcodeblock %}

and calling the curried version

{% codeblock lang:java %}
add();                          // gives back a instance of Function1<[A, B]>
add().apply(1);                 // gives back a instance of Function1<[A, B]>
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

Which is shorthand for writing it out in full like this.

{% codeblock lang:scala %}
// longhand
def add(x: Int): (Int => Int) = {
  (y: Int) => {
    x + y
  }
}
{% endcodeblock %}


Using the REPL,

{% codeblock lang:sh %}
scala> def add(x: Int)(y: Int): Int = {
     | x + y
     | }
add: (x: Int)(y: Int)Int

scala> add(1) _
res1: Int => Int = <function1>

scala> (add(1) _).apply(1)
res2: Int = 2

scala> add(1)(1)
res3: Int = 2
{% endcodeblock %}


{% codeblock lang:sh %}
scala> def add2(x: Int): (Int => Int) = {
     |   (y: Int) => {
     |     x + y
     |   }
     | }
add2: (x: Int)Int => Int

scala> add2(1).apply(1)
res6: Int = 2
{% endcodeblock %}


## References

 * [Gist](https://gist.github.com/tobyweston/6027570)
 * [Function Currying in Scala](http://www.codecommit.com/blog/scala/function-currying-in-scala)
 * [Currying and Partially Applied Functions](http://danielwestheide.com/blog/2013/01/30/the-neophytes-guide-to-scala-part-11-currying-and-partially-applied-functions.html)