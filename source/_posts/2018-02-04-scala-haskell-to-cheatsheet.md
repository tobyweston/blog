---
layout: post
title: "Scala to Haskell Cheatsheet"
date: 2018-02-04 20:01
comments: true
categories: haskell, scala
sidebar: false
published: false
keywords: "haskell, scala, flatmap, point, >>="
description: "Haskell conventions and how they translate to Scala"
---

A lot of the advanced functional programming literature refers to Haskell, which when you're comming from Scala, may not be so helpful. If you want to know what `fmap` in Haskell maps to in Scala, read on...

<!-- more -->

## Standard Functions

|  Haskell |   Scala   |  Concept |                  Notes                  |
|----------|-----------|----------|-----------------------------------------|
| `>>=`    | `flatMap` | bind     | Defines monad                           |
| `return` | `unit`    | identity | Defines monad                           |
| `join`   | `flatten` |          |                                         |
| `fmap`   | `map`     |          | Defines a functor                       |


## Function Convensions

 * `point` and it's alias, `pure` are "constructor" like functions that take a thing and put it in a _higher kinded type_, usually in the context of an _applicative_.
 * `zero` and `op` (`operation`) are conventially used to support _monoids_. 

