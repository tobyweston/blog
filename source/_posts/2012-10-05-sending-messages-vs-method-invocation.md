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

The difference between sending a message and calling methods is subtle. Sending a message (in lets say, Ojective-C) usually results in a method being called but not always. The recieving object decides how to handle a message whilst a call to a method a more static thing [1]. In lanaguages like Java, the method lookup is still done, it's just done behind the schenes. By calling a _method, for example, `apple.eat()`, the reference to `apple` allows this dynamic lookup.

It's very similar in concept (and in fact, implemented in some languages) as the distinction between functions and methods.

## Functions vs Methods

Functions are class level operatation whereas methods are object level operations.

Methods in Objective-C for example, are compiled down to C functions with additional parameters. One of which is the reciever. So, our method from above would produce a function `-(void) eat: (Apple*) apple`

http://stackoverflow.com/questions/3036330/method-vs-function-vs-procedure-vs-class

[1] https://www.informit.com/articles/article.aspx?p=1568732