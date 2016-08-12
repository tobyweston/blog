---
layout: post
title: "Type Classes in Scala"
date: 2016-08-13 18:42
comments: true
categories: scala
sidebar: false
published: false
series: Scala Implicits
keywords: ""
description: ""
---

In the previous post on implicits, we talked about ...

<!-- more -->


From the [Neophytes Guide](http://danielwestheide.com/blog/2013/02/06/the-neophytes-guide-to-scala-part-12-type-classes.html)

* A type class `C` defines behaviour
* Type `T` must support behaviour defined in `C` to be a "member" of `C`
* if `T` is a "member", it isn't by means of inheritance
* any type (like `T`) can just supply implementations of `C` behaviour

Type classes provide ad-hoc inheritance (see [Wikipedia](http://bit.ly/1kr6C8E#Ad_hoc_polymorphism)).


## Step 1: Define Behaviour (as a trait)

Always take a paramaterised type.

```scala
object Example {
  trait NumberLike[T] {
    def plus(x: T, y: T): T
    def divide(x: T, y: Int): T
    def minus(x: T, y: T): T
  }
}
```
## Step 2: Provide Default Implementations

Provide some default implementations of your type class trait in its companion object. Usually, these are singletons (`object`) but could be `val`s. They are **always** `implicit`.

```scala
object NumberLike {
  implicit object NumberLikeDouble extends NumberLike[Double] {
    def plus(x: Double, y: Double): Double = x + y
    def divide(x: Double, y: Int): Double = x / y
    def minus(x: Double, y: Double): Double = x - y
  }
  
  implicit object NumberLikeInt extends NumberLike[Int] {
    def plus(x: Int, y: Int): Int = x + y
    def divide(x: Int, y: Int): Int = x / y
    def minus(x: Int, y: Int): Int = x - y
  }
}
```

## Calling Type Classes

Execute the behaviour of the type class (`C`) where a implementation can be found.


```scala
def mean[T](xs: Vector[T])(implicit number: NumberLike[T]): T = {
  number.divide(xs.reduce(number.plus), xs.size)
}
```

So, if an implicit parameter can be found for a given type, Scala will use the implementation to provide the behaviour. In the example below, the `NumberLikeInt` is used from the defaults.

    scala> println(Statistics.mean(Vector(1, 2, 3, 6, 8)))
    4
    
Without an implicit in scope, you'd get an error

    Error:(42, 26) could not find implicit value for parameter number: NumberLike[Int]
      println(Statistics.mean(Vector(1, 2, 3, 6, 8)))
      
      
Another way of writting the generic method is to use context bounds (ie, use `T: NumberLike`).

```scala
def mean2[T: NumberLike](xs: Vector[T]) = {
  val number = implicitly[NumberLike[T]]
  number.divide(xs.reduce(number.plus), xs.size)
}
```
