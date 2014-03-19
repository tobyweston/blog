---
layout: post
title: "Method References in Java 8"
date: 2014-02-18 21:33
comments: true
categories: java, java8
sidebar: false
published: true
keywords: "JDK 8, Java 8, OpenJDK 8, lambda support, method references, method references in java, oracle docs"
description: "Oracle have made a mess in their official docs, read my more straight forward description of method references in Java 8"
---

Java 8 brings with it method references; shortcuts that you can use anywhere you would use a lambda. The [Oracle docs](http://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html) describe four types of method reference but do such a poor job of describing them that I felt compelled to describe them myself.

<!-- more -->

[Oracle describe the four kinds of method reference](http://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html) as follows.

| Kind                                                                           | Example                                |
|--------------------------------------------------------------------------------|----------------------------------------|
| Reference to a static method                                                   | `ContainingClass::staticMethodName`
| Reference to an instance method of a particular object                         | `ContainingObject::instanceMethodName`
| Reference to an instance method of an arbitrary object of a particular type    | `ContainingType::methodName`
| Reference to a constructor                                                     | `ClassName::new`




Static and constructor references are straight forward but it's their description of instance method references that muddies the waters. What on earth is an instance method of an arbitrary object of a particular type? Aren't all objects _of a_ particular type?  Why is it important that the object is _arbitrary_?


## What they should have written

It's talking about four types of method reference; constructor references, static method references, instance method references and what it calls instance method references of a particular type. The last one is really just another kind of instance method reference.

What they should have written is this.

| Kind                                                        | Syntax                           | Example                  | As Lambda                       |
|-------------------------------------------------------------|----------------------------------|--------------------------|---------------------------------|
| Reference to a static method                                | `Class::staticMethodName`        | `String::valueOf`        | `(s) -> String.valueOf(s);`
| Reference to an instance method of an object (closure)      | `object::instanceMethodName`     | `x::toString`            | `() -> "hello".toString();`
| Reference to an instance method of an object (lambda)       | `Class::instanceMethodName`      | `Object::toString`       | `(s) -> s.toString();`
| Reference to a constructor                                  | `ClassName::new`                 | `String::new`            | `() -> new String();`


The distinction between a method reference that closes over something (a closure) and one that doesn't (a lambda) may be a bit academic but at least it's a formal definition as opposed to Oracle's unhelpful distinction. If you're interested in the difference between a closure and a lambda, check out my [previous article]({{ root_url }}/blog/2010/07/13/lambdas-vs-closures).


## The "closure" method reference

The example above is an instance method reference using a closure. It creates a lambda that will call the `toString` method on the instance `x`.

``` java
public void example() {
    String x = "";
    function(x::toString);
}
```


where the signature of `function` looks like this

``` java
public static String function(Supplier<String> supplier) {
    return supplier.get();
}
```


The `Supplier` interface must provide a string value (the `get` call) and the only way it can do that is if it's been supplied to it on construction. It's equivalent to

``` java
public void example() {
    String x = "";
    function(() -> x.toString());
}
```


Notice here that the lambda has no arguments (it uses the 'hamburger' symbol). This shows that the value of `x` isn't available in the lambda's local scope and so can only be available from outside it's scope. It's a closure because must close over `x`.

The anonymous class equivalent really makes this obvious, it looks like this.

``` java
public void example() {
    String x = "";
    function(new Supplier<String>() {
        @Override
        public String get() {
            return x.toString(); // <- closes over 'x'
        }
    });
}
```


All three of these are equivalent. Compare this to the lambda variation of an instance method reference where it doesn't have it's argument explicitly passed in from an outside scope.


## The "lambda" method reference

This example is similar to the previous one, it calls the `toString` method of a string only this time, the string is supplied to the function that's making use of the lambda and not passed in from an outside scope.

``` java
public void lambdaExample() {
    function("value", String::toString);
}
```


The `String` part looks like it's referring to a class but it's actually referencing an instance. It's confusing, I know but to see things more clearly, we need to see the function that's making use of the lambda. It looks like this.

``` java
public static String function(String value, Function<String, String> function) {
    return function.apply(value);
}
```


So, the string value is passed directly to the function, it would look like this as a fully qualified lambda.

``` java
public void lambdaExample() {
    function("value", x -> x.toString());
}
```


If you expand it fully to an anonymous interface, it looks like this. The `x` parameter is made available and not closed over. It's a lambda rather than a closure.

``` java
public void lambdaExample() {
    function("value", new Function<String, String>() {
      @Override
      public String apply(String x) {   // <- takes the argument as a parameter, doesn't need to close over it
        return x.toString();
      }
    });
}
```


## Summary

There difference between the two types of instance method reference is basically academic. Sometimes, you'll need to pass something in, other times, the usage of the lambda will supply it for you. My gripe though is with Oracle's documentation. It's _the_ canonical reference material but is just plain confusing. It feels like interns are producing one of Java's most important artifacts.
