---
title: 'Scala to Haskell and FP Cheatsheet'
pubDate: '2018-02-04'
categories: 'haskell, scala'
published: false
keywords: "haskell, scala, flatmap, point, >>=, FP Cheat Sheet"
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

## FP Cheat Sheet

Some general terms and their meanings.

`cons` stands for _construct_ as is typically used when talking about non-empty lists in FP. List construction methods in Scala are `::` and `:::` and methods ending in `:` are associated to the right, meaning, they're used to add elements to the start of a list.
`snoc` is `cons` backwards, so append an element to the end of a list.

<dl>
  <dt><strong><code>cons</code></strong></dt>
  <dd><code>cons</code> stands for _construct_ as is typically used when talking about non-empty lists in FP. List construction methods in Scala are <code>::</code> and <code>:::</code> and methods ending in <code>:</code> are associated to the right, meaning in this case, they're used to add elements to the start of a right hand parameter list.</dd>
  </dl>
  <dl>
  <dt><strong><code>snoc</code></strong></dt>
  <dd><code>snoc</code> is <code>cons</code> backwards, so append an element to the end of a list.</dd>
</dl>
