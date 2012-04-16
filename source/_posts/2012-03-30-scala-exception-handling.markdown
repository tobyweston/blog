---
layout: post
title: "Scala Exception Handling"
date: 2012-03-30 22:47
comments: true
categories: java scala exceptions
published: false
---

We're very used to Java's notion of checked and unchecked exceptions. If we want to force the developer to consider
exceptional behaviour then we typically throw a checked exception. The problem is that despite our best
intentions, we can't force the developer to actually deal with the exception sensibly. Java tries
to help by forcing a compilation error onto the developer so they at least forced to choose a course of action.
The trouble is though its all to tempting to swallow exceptions rethrowing and so either bury our heads in the
sand or litter our code with addition noise.

Scala has taken a different approach. Scala has done away with checked exceptions; all exceptions are effectively
`RuntimeException`s and so its left to the developer to decide when to handle them. This obviously leads to less
noise but puts more responsibility on the developer. Scala makes it easy to avoid the issue but without a clear system
wide policy for exception handling, we can still get into trouble.

This article describes a general approach to understanding _when_ and _how_ to deal with exceptions in Scala or indeed
 in Java when you've made the choice to only throw only sub-classes of `RuntimeException`. We'll take a look at
 Scala's syntax around exceptions and how pattern matching can help.

<!-- more -->

Two key points about exception handling are understanding _when_ to handle an exception and understanding
what action should be taken to naturalise it.

## When

Exception handling is really a system wide concern. By that, I mean that along with being consistent within the
entire system, it needs to be clear at what points within the system are appropriate for dealing with exceptions.
It's not ok to arbitrarily catch an exception, log it and then rethrow; there's no _strategy_ there and the next
developer could do exactly the same thing higher up the call hierarchy and duplicate your logs.

gotta be better than jdk7's pipe seperated catch exception block!

## How

