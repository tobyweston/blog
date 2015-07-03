---
layout: post
title: "Implicit Functions in Scala"
date: 2015-07-04 18:42
comments: true
categories: scala
sidebar: false
published: false
series: Scala Implicits
keywords: ""
description: ""
---

Implicits in Scala are either really awesome or really nasty. 

In this series, we'll take a look at the different types of implicit and when they can be useful.

There are three categories of "implicits";

1. Implicit parameters (`var`s)
1. Implicit functions (`def`s)
1. Implicit classes

<!-- more -->


## Implicit Functions

Often used to conveniently (but secretly) convert from one type to another.