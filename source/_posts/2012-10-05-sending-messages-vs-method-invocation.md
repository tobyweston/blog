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

People often talk about sending a message in object-oriented langauges whilst others talk about invoking methods on objects? What's the difference? Whilst we're there, what's the difference between a function and a method? Is there a difference between an object reference and a pointer?

<!-- more -->



Languages with strong links to Smalltalk 

As well as some other interesting assertions like functions are different than methods and why references are different than pointers.


## Sending Messages

The terminology of sending an object a message is partly historical. Languages like Smalltalk adopted it as a metaphor when working with obhects. To understand why the metaphor is useful, we have to look at things before the advent of object oriented languages. In these dark times, procedural programming relied on subroutines (functions and procedures) to modify state. With no such concept of "objects", state was associated with data structures. So applying a function to a procedure would produce new state and applying a procedure would modify state. Simplistically speaking.

With the advent of "objects" that encapsulate state *and* behaviour, the messagine metaphore invites us to think about objects performing their own operations. Objects communicate by sending each other *messages*. Instead of calling a method as you would a function in procedural programming, you send a message to an object requesting it to perform one of its methods [2]. This allows us to think about *methods* in more abstract terms. Rather than think about data structures and the functions (and procedures) that affect them, we can focus on _behaviours_.




So, sending messages helps us think in object-oriented terms rather than procedural or functional terms.

 Rather than tell an object to perform some action, traditionally implemented via efferial subroutines of functions or procedures, it's useful to think of it terms of asking the object itself

requesting objects perform behaviours. It's a usful 

The difference between sending a message and calling methods is subtle. Sending a message usually results in a method being called but not always. The recieving object decides how to handle a message whilst a call to a method is a more static thing [1]. In lanaguages like Java, the method lookup is still done, it's just done behind the schenes. By calling a method, for example, `apple.eat()`, the reference to `apple` allows this dynamic lookup.

It's very similar in concept (and in fact, implemented in some languages) as the distinction between functions and methods.

## Functions vs Methods

Functions are class level operatation whereas methods are object level operations.

Methods in Objective-C for example, are compiled down to C functions with additional parameters. One of which is the reciever. So, our method from above would produce a function `-(void) eat: (Apple*) apple`

http://stackoverflow.com/questions/3036330/method-vs-function-vs-procedure-vs-class

[1] https://www.informit.com/articles/article.aspx?p=1568732
[2] Object-Oriented Programming with Objective-C, Apple.