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

1. **[Implicit parameters]({{ root_url }}/blog/2015/07/03/scala-implicit-parameters/)** will be automatically passed values that have been marked as `implicit`
1. **[Implicit functions]({{ root_url }}/blog/2015/07/04/scala-implicit-functions/)** are `def`s that will be called automatically if the code wouldn't otherwise compile
1. **[Implicit classes]({{ root_url }}/blog/2015/07/05/scala-implicit-classes/)** extend behaviour of existing classes you don't otherwise control (akin to [Categories](https://developer.apple.com/library/prerelease/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html) in Objective-C)


<!-- more -->

## Implicit Parameters