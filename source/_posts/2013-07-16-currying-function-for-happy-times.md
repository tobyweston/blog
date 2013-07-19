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

Currying is the technique of transforming a function with multiple arguments into a function with just one argument which takes the first argument of the original function and returns another single argument function. This chaining continues over the number of arguments of the original. The last in the chain will have access to all of the argument and so can return the result.

In Java, this might look like this.





In Scala, a curried function is one that operates over multiple, independent parameters. Any regular function with multiple parameters can be turned into a curried function if

<!-- more -->


http://www.codecommit.com/blog/scala/function-currying-in-scala
http://danielwestheide.com/blog/2013/01/30/the-neophytes-guide-to-scala-part-11-currying-and-partially-applied-functions.html