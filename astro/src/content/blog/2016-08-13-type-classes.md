---
title: "Type Classes in Scala"
pubDate: "2016-08-13"
categories: 'scala'
keywords: "Scala type classes, ad-hoc polymorphism, implicits, type class pattern, Scala, functional programming"
description: "Type classes in Scala provide ad-hoc polymorphism without inheritance. Learn the pattern using implicits and understand when type classes beat traditional OOP."
series: 'Scala Implicits'
---

Type classes provide [ad-hoc inheritance](http://bit.ly/1kr6C8E#Ad_hoc_polymorphism) which means that we can use them to create polymorphic functions that can be applied to arguments of different types. This is a fancy way of saying that we can create common behaviour for classes without resorting to traditional (`extends`) polymorphism.

From the [Neophytes Guide](http://danielwestheide.com/blog/2013/02/06/the-neophytes-guide-to-scala-part-12-type-classes.html), Daniel Westheide describes type classes, slightly paraphrased, as follows.


> A type class `C` defines behaviour.  
> Type `T` must support behaviour defined in `C` to be a "member" of `C`.  
> If `T` is a "member", it isn"t inherent to that type (if `T` has `C`'s behaviour, it isn't native to that type via `extends` or otherwise).  
> Instead, anyone can supply implementations of `C` behaviour for type `T` and this infers that `T` is a "member" of `C`.



## How to Create Type Classes

1. Define behaviour `C` as a trait
1. Provide default implementations for your types (e.g. `T` above)
1. Call the behaviours of `C` in a common way (optionally extending "members" like `T` with implicit classes)


## Example from the Neophytes Guide

> The type class here is `NumberLike` providing abstract `plus`, `divide` and `minus` behaviours.  
> Types `Int` and `Double` are "members" of `NumberLike`.  
> `Int` and `Double` don't natively have the behaviors of `NumberLike`.  
> Instead, the implementations on the `NumberLike` object provides them.  


### Step 1: Define Behaviour (as a trait)

Notice the paramaterised type `[T]`.

```scala
object Example {
  trait NumberLike[T] {
    def plus(x: T, y: T): T
    def divide(x: T, y: Int): T
    def minus(x: T, y: T): T
  }
}
```

### Step 2: Provide Implementations

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

### Step 3a. Call the Type Class

The whole point of the pattern is to be able to provide common behaviour to classes without tight coupling or even by modifying them at all. So far, we've created specific behaviours for our classes (like `plus` above) conforming to our "contract" type class `C`. 

To call that behaviour, we use Scala's `implicit` semantics to find an appropriate implementation. It binds a concrete type of `T` (let's say `Int`) with it's corresponding type class (`NumberLikeInt`). It means we only need one method for all number-like types.

```scala
object Statistics {
  def mean[T](numbers: Seq[T])(implicit number: NumberLike[T]): T = {
    number.divide(numbers.reduce(number.plus), numbers.size)
  }
}
```

So, if an implicit parameter can be found for a given type, Scala will use that implementation. The `NumberLikeInt` is used below.

```bash
scala> println(Statistics.mean(List[Int](1, 2, 3, 6, 8)))
4
```

Without an implicit in scope, you'd get an error

```bash
Error:(42, 26) could not find implicit value for parameter number: NumberLike[Int]
  println(Statistics.mean(Seq(1, 2, 3, 6, 8)))
```
      
      
#### Context Bounds      
      
Another way of writing the generic method is to use context bounds (ie, use `T: NumberLike`).

```scala
object Statistics {
  def mean[T: NumberLike](numbers: Seq[T]) = {
    val number = implicitly[NumberLike[T]]
    number.divide(numbers.reduce(number.plus), numbers.size)
  }
}
```

### Step 3b. Call the Type Class (with an Implicit Class)

As a simple extension, you can extend "member" types directly using an `implicit` class. For example, we can add the `mean` method to any sequence of `NumberLike`s.

```scala
implicit class SeqNumberOps[T](numbers: Seq[T]) {
  def mean(implicit number: NumberLike[T]): T = {
    number.divide(numbers.reduce(number.plus), numbers.size)
  }
}
```

and call `mean` directly.

```scala
import NumberOps

val numbers = List[Int](1, 5, 32, 43, 4)
println(numbers.mean)
```

or like this for `Double`.

```scala
val numbers = List[Double](3.2, 4.2, 3.0, 4.4)
println(numbers.mean)
```



## Another Example

### Step 1: Define Behaviour

A basic "decoder" interface that uses an `Either` to return a result as either successful or unsuccessful.

```scala
trait StringDecoder[A] {
  def fromString(string: String): Either[String, A]
}
```

### Step 2: Provide Implementations

We could provide an implementation to decode a string to a valid `Colour` type. Unsupported colours produce a "left" result.

```scala
implicit val colourTypeStringDecoder = new StringDecoder[Colour] {
  def fromString(value: String) = {
    val colours = List("red", "green", "yellow")
      if (colours.contains(value)) Right(Colour(value)) 
      else Left(s"$value is not a valid colour, chose one of ${colours.mkString(", ")}")
  }
}
```


### Step 3. Call the Type Classes

With an implicit class extending `String`, any string value can be decoded to a type `A`.

```scala
object StringSyntax {
  implicit class StringDecoderOps(value: String) {
    def decodeTo[A](implicit decoder: StringDecoder[A]) = {
      decoder.fromString(value)
    }
  }
}
```

Then anywhere you have a string and you want to decode it, just go ahead.

```scala
"red".decodeTo[Colour]      // right
"square".decodeTo[Colour]   // Left(square is not a valid colour, chose one of red, green, yellow)
```