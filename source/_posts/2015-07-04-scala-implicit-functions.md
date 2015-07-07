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

In the previous post, we looked at implicit parameters; parameters that will be automatically passed values that have been marked as `implicit`. In this post, we'll take a look at implicit functions and how they can be useful to convert things of one type to things of another.

<!-- more -->

## Implicit Functions

Often used to conveniently (but secretly) convert from one type to another.