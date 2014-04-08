---
layout: post
title: "Functional Interfaces in Java 8"
date: 2014-04-07 21:33
comments: true
categories: java, java8
sidebar: false
published: true
keywords: "JDK 8, Java 8, OpenJDK 8, functional interface, @FunctionalInterface, lambda"
description: "xxx"
---

Java 8 treats lambdas as an instance of an interface type. It formalises this into something it calls "functional interfaces". A functional interface is just an interface with a single method. Java calls the method a "functional method" but the name "single abstract method" or SAM is often used. All the existing single method interfaces like `Runnable` and `Callable` in the JDK are now functional interfaces and lambdas can be used anywhere a single abstract method interface is used.

<!-- more -->

## @FunctionalInterface

Oracle have introduced a new annotation `@FunctionalInterface` to mark an interface as such. It's basically to communicate intent but also allows the compiler to do some additional checks.

For example. This interface compiles,

{% codeblock lang:java %}
public interface FunctionalInterfaceExample {
}
{% endcodeblock %}

but when you indicate that it should be a _functional interface_

{% codeblock lang:java %}
@FunctionalInterface // <- error here
public interface FunctionalInterfaceExample {
}
{% endcodeblock %}

The compiler will raise an error as there is no method. It says that "Example is not a functional interface" as "no abstract method was found". It'll also error if we try and add a second method.

{% codeblock lang:java %}
@FunctionalInterface
public interface FunctionalInterfaceExample {
    void apply();
    void illegal();    // <- error here
}
{% endcodeblock %}

This time it's saying "multiple, non-overriding abstract methods were found". Functional interfaces can have only **one** method.


## Extension

What about the case of an interfaces that extends another interfaces?

I'll create a new functional interface called "A" and another called "B" which extends "A". "B" is still "functional". It inherits the parents `apply` method as you'd expect.

{% codeblock lang:java %}
@FunctionalInterface
interface A {
    abstract void apply();
}

interface B extends A {

}
{% endcodeblock %}


If you wanted to make this clearer, you can also override the functional method from the parent.

{% codeblock lang:java %}
@FunctionalInterface
interface A {
    abstract void apply();
}

interface B extends A {
    @Override
    abstract void apply();
}
{% endcodeblock %}


We can verify it works as a functional interface if we use it as a lambda. So I'll implement a little method to show that a lambda can be assigned to a type of `A` and a type of `B`. The implementation will just print out "A" or "B".

{% codeblock lang:java %}
@FunctionalInterface
public interface A {
    void apply();
}

public interface B extends A {
    @Override
    void apply();
}

public static void main(String... args) {
    A a = () -> System.out.println("A");
    B b = () -> System.out.println("B");
}
{% endcodeblock %}

You can't add a new abstract method to the extending interface though, as the resulting type would have two abstract methods and the compiler will error.

{% codeblock lang:java %}
@FunctionalInterface
public interface A {
    void apply();
}

public interface B extends A {
    void illegal();
}

public static void main(String... args) {
    A a = () -> System.out.println("A");
    B b = () -> System.out.println("B");    // <- error
}
{% endcodeblock %}


In both cases, you can override methods from `Object` without causing problems. You can also add default methods (also new to Java 8).

As you'd probably expect, it doesn't make sense to try and mark an abstract class as a functional interface.


## Summary

An important point to take away was the idea that any place a functional interface is used, we can now use lambdas. Lambdas can be used in-lieu of anonymous implementations of the functional interface.
