---
layout: post
title: "Scala Exception Handling"
date: 2012-03-30 22:47
comments: true
categories: java scala exceptions
sidebar : false
series: Exception Handling
---

We're very used to Java's notion of checked exceptions. If we want to force the developer to consider exceptional behaviour then we typically throw a checked exception. The problem is that despite our best intentions, we can't force the developer to actually deal with the exception sensibly. Java tries to help by forcing a compilation error onto the developer so they at least forced to choose a course of action. The trouble is though it's all too tempting to swallow exceptions or just rethrow. We tend to either bury our heads in the sand or litter our code with addition noise.

Scala has taken a different approach. Scala has done away with checked exceptions; all exceptions are effectively `RuntimeException`s and so its left to the developer to decide when to handle them. This obviously leads to less noise but puts more responsibility on the developer. Scala makes it easy to avoid the issue but without a clear system wide policy for exception handling, we can still get into trouble.

In a [previous post]({{ root_url }}/blog/2012/03/29/building-better-exceptions), I've described a general approach to understanding _when_ and _how_ to deal with exceptions in Scala or Java. In this post, we'll take a quick look at Scala's syntax around exceptions and how pattern matching is employed.

<!-- more -->

## Exceptions

Scala essentially treats all exception types as `RuntimeException`. This means it doesn't _force_ you to handle exceptions. Instead, it combines _pattern matching_ with a single `catch` block to handle exceptions. For example

{% codeblock lang:scala %}
try {
  val url = new URL("http://baddotrobot.com")
} catch {
  case e: MalformURLException => println("bad url " + e)
  case e: IOException => println("other IO problem " + e)
  case _ => println("anything else!")
} finally {
  // cleanup
}
{% endcodeblock %}


Any cleanup can be achieved using the `finally` block as expected. This works exactly the same way as in Java but perhaps a more idiomatic alternative is to use the _[loan pattern](https://wiki.scala-lang.org/display/SYGN/Loan)_. You can see an example of the pattern in Java form in the `ExecuteUsingLock` [class](https://github.com/tobyweston/tempus-fugit/blob/master/src/main/java/com/google/code/tempusfugit/concurrency/ExecuteUsingLock.java) in [tempus-fugit](http://tempusfugitlibrary.org/).

Throwing exceptions is done in the same way as Java, as in the example below.

{% codeblock lang:scala %}
def load(url: String) {
  // ...
  throw new IOException("failed to load")
}
{% endcodeblock %}

However, anyone calling this method won't be forced by the compiler to catch the exception. If you intend to call your Scala code from Java however, you can force checked exceptions using the `throws` annotation but this still won't affect Scala clients.

{% codeblock lang:scala %}
@throws(classOf[java.io.IOException])
def load(url: String) {
  // ...
}
{% endcodeblock %}

Interestingly, Scala treats `throw` as an expression with a return type of `Nothing`. You can use it in place of any other expression even though the result wont actually evaluate to anything.


## Pattern Matching

Pattern matching is a bit like a switch statement but unlike Java's switch statement, pattern matching in Scala can be used to match any kind of constant as well as other things (like _case objects_). It's not restricted to just primitives and enums as with Java (although Java 1.7 brought `String` [support to switch](http://docs.oracle.com/javase/7/docs/technotes/guides/language/strings-switch.html)).

Pattern matching is applied to the exception type when using `catch` above but it's also used in its vanilla form. For example, as described in [Programming in Scala](http://www.artima.com/shop/programming_in_scala_2ed), we can work out what to have with dinner in the example below.

{% codeblock lang:scala %}
def accompaniment(dinner: String) {
  dinner match {
    case "fish" => println("chips")
    case "sausage" => println("mash")
    case "sheep" => println("cheese")
    case _ => println("beans?")
  }
}
{% endcodeblock %}

Notice that there is no need for a `break` statement and that each match expression results in a value. So we can take advantage of resulting value and rewrite the above to the following.

{% codeblock lang:java %}
def anotherAccompaniment(dinner: String) {
  val accompaniment =
    dinner match {
      case "fish" => "chips"
      case "sausage" => "mash"
      case "sheep" => "cheese"
      case _ => "beans goes with anything!"
    }
  println(accompaniment)
}
{% endcodeblock %}


## Conclusion

The whole thing is generally neater than the Java equivalent but as I keep banging on about, we still need to carefully consider where to apply the `catch` when handling exceptions. When using Scala, it's even more important to understand where potential exceptions will bubble up and how to [handle them as a system wide concern]({{ root_url}}/2012/03/28/exception-handling-as-a-system-wide-concern).
