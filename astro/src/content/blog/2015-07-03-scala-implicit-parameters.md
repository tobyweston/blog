---
title: "Implicit Parameters in Scala"
pubDate: '2015-07-03'
categories: 'scala'
keywords: "Scala implicits, implicit parameters, implicit values, Scala compiler, context bounds, type class"
description: "Scala implicit parameters allow the compiler to automatically supply values marked implicit. Introduction to the three categories of Scala implicits."
series: 'Scala Implicits'
---

Scala "implicits" allow you to omit calling methods or referencing variables directly but instead rely on the compiler to make the connections for you. For example, you could write a function to convert from and `Int` to a `String` and rather than call that function _explicitly_, you can ask the compiler to do it for you, _implicitly_.  

In the next few posts, we'll look at the different types of implicit bindings Scala offers and show some examples of when they can be useful.


There are three categories of "implicits";

1. **[Implicit parameters](/blog/2015-07-03-scala-implicit-parameters)** (aka implicit values) will be automatically passed values that have been marked as `implicit`
1. **[Implicit functions](/blog/2015-07-14-scala-implicit-functions/)** are `def`s that will be called automatically if the code wouldn't otherwise compile
1. **Implicit classes** extend behaviour of existing classes you don't otherwise control (akin to [categories](https://developer.apple.com/library/prerelease/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html) in Objective-C)



## Implicit Parameters

At it's simplest, an implicit parameter is just a function parameter annotated with the `implicit` keyword. It means that if no value is supplied when called, the compiler will look for an implicit value and pass it in for you.

``` scala
def multiply(implicit by: Int) = value * by
```
You tell the compiler what it can pass in implicitly but annotating values with `implicit`

``` scala
implicit val multiplier = 2
```
and call the function like this

``` scala
multiply
```
The compiler knows to convert this into a call to `multiply(multiplier)`. If you forget to define an implicit `var`, you'll get an error like the following.

    error: could not find implicit value for parameter by: Int
           multiply
           ^

## Implicit `val`, `var` or `def`

You can ask the compiler to call your function with an implicit `val` (like we've just seen), a `var` or even another `def`. So, we could have written a function that returns an `Int` and Scala would attempt to use that instead.

``` scala
implicit def f: Int = if (monday) 4 else 2
```
The compiler would try to resolve this as `multiply(f())`.

However, you can't have more than one in scope. So if we have both the `multipler` value and `f` function defined as implicit and call `multiply`, we'd get the following error. 

    error: ambiguous implicit values:
     both value multiplier of type => Int
     and method f of type => Int
     match expected type Int
           multiply
           ^



## Syntax

You can only use `implicit` once in a parameter list and all parameters following it will be implicit. For example;

``` scala
def example1(implicit x: Int)                       // x is implicit
def example2(implicit x: Int, y: Int)               // x and y are implicit
def example3(x: Int, implicit y: Int)               // wont compile 
def example4(x: Int)(implicit y: Int)               // only y is implicit
def example5(implicit x: Int)(y: Int)               // wont compile
def example6(implicit x: Int)(implicit y: Int)      // wont compile
```

## Example

As an example, the test below uses [Web Driver](http://www.seleniumhq.org/projects/webdriver/) (and specifically an instance of the `WebDriver` class) to check that a button is visible on screen. The `beVisible` method creates a `Matcher` that will check this for us but rather than pass in the `driver` instance explicitly, it uses an implicit `val` to do so.

``` scala
class ExampleWebDriverTest extends mutable.Specification {

  implicit val driver: WebDriver = Browser.create.driver
  
  "The checkout button is visible" >> {
    val button = By.id("checkout")
    // ...
    button must beVisible           // reads better than 'must beVisible(driver)'   
  }
  
  def beVisible(implicit driver: WebDriver): Matcher[By] = new Matcher[By] {
    def apply[S <: By](t: Expectable[S]) = result(
      t.value.isDisplayed,
      s"${t.value.toString} is visible",
      s"${t.value.toString} is not visible",
      t)
  }
}
```
## Roundup

Implicit parameters are useful for removing boiler plate parameter passing and can make your code more readable. So if you find yourself passing the same value several times in quick succession, they can help hide the duplication.

The Scala library often use them to define default implementations that are "just available". When you come to need a custom implementation, you can pass one in explicitly or use your own implicit value. A good example here is the `sorted` method on [`SeqLike`](http://www.scala-lang.org/api/2.11.7/#scala.collection.SeqLike) class. 

The really useful stuff though comes when we combine implicit parameters with the other types of "implicits". Read more in the series to build up a picture.
