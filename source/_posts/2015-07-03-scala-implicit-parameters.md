---
layout: post
title: "Implicit Parameters in Scala"
date: 2015-07-03 18:42
comments: true
categories: scala
sidebar: false
published: false
series: Scala Implicits
keywords: ""
description: ""
---

As the name suggests, "implicits" allow you to omit calling methods or referencing variables directly but instead rely on the compiler to make the connections for you. For example, you could write a function to convert from and `Int` to a `String` and rather than call that function _explicitly_, you can ask the compiler to do it for you, _implicitly_.  

In the next few posts, we'll look at the different types of implicit bindings Scala offers and show some examples of when they can be useful.

<!-- more -->

There are three categories of "implicits";

1. **[Implicit parameters]({{ root_url }}/blog/2015/07/03/scala-implicit-parameters/)** (aka implicit values) will be automatically passed values that have been marked as `implicit`
1. **[Implicit functions]({{ root_url }}/blog/2015/07/04/scala-implicit-functions/)** are `def`s that will be called automatically if the code wouldn't otherwise compile
1. **[Implicit classes]({{ root_url }}/blog/2015/07/05/scala-implicit-classes/)** extend behaviour of existing classes you don't otherwise control (akin to [Categories](https://developer.apple.com/library/prerelease/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html) in Objective-C)


<!-- more -->

## Implicit Parameters

At it's simplest, an implicit parameter is just a function parameter annotated with the `implicit` keyword. It means that if no value is supplied when called, the compiler will look for an implicit value and pass it in for you.

{% codeblock lang:scala %}
def multiply(implicit by: Int) = value * by
{% endcodeblock %}

You tell the compiler what it can pass in implicitly but annotating values with `implicit`

{% codeblock lang:scala %}
implicit val multiplier = 2
{% endcodeblock %}

and call the function like this

{% codeblock lang:scala %}
multiply
{% endcodeblock %}

The compiler knows to convert this into a call to `multiply(multiplier)`. If you forget to define an implicit `var`, you'll get an error like the following.

    error: could not find implicit value for parameter by: Int
           multiply
           ^

## Implicit `val`, `var` or `def`? 

You can actually ask the compiler to call your function with an implicit `val` (like we've just seen), a `var` or even another `def`. So, we could have written a function that returns an `Int` and Scala would attempt to use that instead.

{% codeblock lang:scala %}
implicit def f: Int = if (monday) 4 else 2
{% endcodeblock %}

The compiler would try to resolve this as `multiply(f())`.

However, you can't have more than one in scope. So if we have both the `multipler` value and `f` function defined as implicit and call `multiply`, we'd get the following error. 

    error: ambiguous implicit values:
     both value multiplier of type => Int
     and method f of type => Int
     match expected type Int
           multiply
           ^



## Syntax

You can only use `implicit` once in a parameter list, and all parameters following it will be implicit. For example;

{% codeblock lang:scala %}
def example1(implicit x: Int)                       // x is implicit
def example2(implicit x: Int, y: Int)               // x and y are implicit
def example1(x: Int, implicit y: Int)               // wont compile 
def example3(x: Int)(implicit y: Int)               // only y is implicit
def example3(implicit x: Int)(y: Int)               // wont compile
def example3(implicit x: Int)(implicit y: Int)      // wont compile

{% endcodeblock %}