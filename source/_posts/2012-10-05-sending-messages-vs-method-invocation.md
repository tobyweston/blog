---
layout: post
title: "Sending Messages vs Method Invocation"
date: 2012-10-05 04:12
comments: true
categories: java object-oriented
sidebar: false
published: false
keywords: "message sending, smalltalk, java, object-oriented, method invocation"
description: "What's the difference between sending an object a message and just invoking a method on an object? Why is a function difference than a method?"
---

People often talk about sending a message in object-oriented languages whilst others talk about invoking methods on objects? What's the difference? Whilst we're on the topic, what's the difference between a function and a method? Is there a difference between an object reference and a pointer? What's a function pointer?

<!-- more -->


## Sending Messages

The terminology of sending an a message to an object is partly historical. Languages like Smalltalk adopted it as a metaphor when working with objects. To understand why the metaphor is useful, we have to look at things before the advent of object oriented languages. In these days, procedural programming relied on subroutines (functions and procedures) to modify state. With no concept of "objects", state is simply associated with data structures. So applying a function to those structures would produce new state and applying a procedure would modify state.

With the advent of "objects" that encapsulate state *and* behaviour, the messaging metaphor invites us to think about objects performing their own operations. Objects communicate by sending each other *messages*. Instead of calling a method as you would a function in procedural programming, you send a message to an object requesting it to perform one of its methods. This allows us to think about *methods* in more abstract terms. Rather than think about data structures and the functions (and procedures) that affect them, we can focus on _behaviours_ [2].

> So, sending messages helps us think in object-oriented terms rather than procedural or functional terms but there is also a more concrete, technical difference.

Sending a message means the receiving object decides how to handle a message whilst a call to a function (or procedure) is a more static thing [1]. In lanaguages like Java, the function (or procedure) lookup is still done, it's just done behind the scenes at runtime. By calling a method, for example, `apple.eat()`, the reference to `apple` allows the JVM to associate the object `apple` with the procedure `eat`. This is called [dynamic dispatch](http://en.wikipedia.org/wiki/Dynamic_dispatch).

It's very similar in concept (and in fact, implemented in some languages) as the distinction between functions and methods.



## Functions vs Methods

Functions and procedures are [subroutines](http://en.wikipedia.org/wiki/Subroutine) disassociated from the data they act upon. Methods on the other hand are subroutines associated with objects. Functions are class level subroutines whereas methods are object level subroutines. For example, a *method* in Objective-C, is compiled down to a C *function* with additional parameters, one of which is the receiver object. It associates the function with an object. Our method above would produce a function `-(void) eat: (Apple*) apple`.

A C function is equivalent to a static class method in Java.



http://stackoverflow.com/questions/3036330/method-vs-function-vs-procedure-vs-class


[1] https://www.informit.com/articles/article.aspx?p=1568732
[2] Object-Oriented Programming with Objective-C, Apple.