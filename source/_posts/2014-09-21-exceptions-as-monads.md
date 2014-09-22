---
layout: post
title: "Dealing with Exceptions as Monads"
date: 2014-09-21 05:12
comments: true
categories: java java8 exception-handling scala
sidebar: false
series: Exception Handling
published: true
keywords: "java 8, java, monads, either, scala, try, scalaz, option, monadically"
description: "Functional languages often discourage the use of exceptions because they can subvert control execution flow; they introduce side-affects. By using the type system to capture exceptional behaviour and dealing with exceptions monadically, it's much easier to provide system wide consistently.
"
---

In some [previous posts](http://baddotrobot.com/blog/categories/exceptions/), I wrote about treating exceptions as a system wide concern. In this post, I extend that idea and talk about distinguishing between exceptional behaviour and just code that didn't return what you wanted.

Pure functional languages often discourage the use of exceptions because when they are used to control execution flow, they introduce side-affects and violate [purity of function](http://baddotrobot.com/blog/2012/04/03/scala-as-a-functional-oo-hybrid/). By using the type system to capture exceptional behaviour and dealing with exceptions monadically, it's much easier to provide that system wide consistently I've been talking about.

<!-- more -->

## Object-Oriented

***The norm for object oriented code is to use exceptions to control execution flow.*** When you have a method that can return `true` or `false` _and_ throw an exception, it might as well be returning three things. It forces clients to have to reason about logic that has nothing to do with the function of the method. It's complicated and often makes it hard to treat exceptions consistently across the entire application.


## Functional

***So what can we learn from functional programing languages?*** Exceptions are a fact of life, unexpected things can happen with your code and you still need to deal with them. The subtlety here is that functional languages emphasize the *unexpected* part with exceptions. They try and discourage you from using exceptions for dealing with known branches of logic and instead use them like Java uses `Error`s (ie as non-recoverable). This means thinking of exceptions of _exceptional behaviour_ and not Java's notion of checked `Exceptions`.

***So how do languages like Scala discourage you using them like Java?*** They usually offer alternative mechanisms. Scala for example has the [`Either`](http://www.scala-lang.org/api/2.11.1/#scala.util.Either) and [`Try`](http://www.scala-lang.org/api/2.11.1/#scala.util.Try) classes. These classes allow you to express using the type system, that a method was successful or unsuccessful, independently from the return value. As an additional bonus, because they are [monadic](http://debasishg.blogspot.co.uk/2008/03/monads-another-way-to-abstract.html), you can deal with exceptional and expected behaviour consistently in code. That means you can use the same structures to process the positive and the negative case without resorting to `catch` blocks.
  
## Either in Java
  
For example, let's say we have a method `uploadExpenses` that uploads this months expenses to my online accountant's web service. It uploads a single expense at a time, so it could fail because of some network problem or if the web service rejects an individual `Expense`. Once done, I'd like to produce a report (just using `System.out` in our example).

### Traditional Exception Throwing

In a traditional exception throwing version below, the `uploadExpenses` call can break after only some expenses have been uploaded. With no report, it would be hard to work out which were successfully uploaded. You're also left to deal with the exceptions. If other code depends on this, it may make sense to propagate the exception to an [appropriate system boundary](http://baddotrobot.com/blog/2012/03/28/exception-handling-as-a-system-wide-concern/) but dealing with exceptions consistently for the entire system is a real challenge.

{% codeblock lang:java %}
try {
    List<Expense> expenses = ...
    Expenses uploaded = uploadExpenses(expenses).collect(toList()));    // <- can throw exceptions
    uploaded.forEach((e) -> System.out.println(e));
} catch (HttpProblem e) {
    // what to do?
} catch (DuplicateExpenseFound e) {
    // what to do?
}
{% endcodeblock %}


### Using Eithers

On the other hand, if we use an `Either` we can make the `uploadExpenses` call return _either_ a successfully upload `Expense` or a tuple detailing the expense that failed to upload along with the reason why. Once we have a list of these, we can process them in the same way to produce our report. The neat thing here is that the exceptional behaviour is encoded in the return type; clients know that this thing could fail and can deal with it without coding alternative logic.


{% codeblock lang:java %}
List<Expense> expenses = ...
List<Either<Pair<Expense, Throwable>, Expense>> results = uploadExpenses(expenses).collect(toList());

Stream<Pair<Expense, Throwable>> failures = results.stream().flatMap(either -> either.left());
failures.forEach(failure -> System.out.println(failure));

Stream<Expense> successes = results.stream().flatMap(either -> either.right());
successes.forEach(success -> System.out.println(success));
{% endcodeblock %}

In this way, having the semantics baked into the return types is what forces clients to deal with the exceptional behaviour. Dealing with them monadically ensures that we can deal with them consistently. For a naive implementation, have a look at my [gist](https://gist.github.com/tobyweston/caefc3b5ec36348387e5) and for fuller implementations, see [Scala's version](https://github.com/scala/scala/blob/2.11.x/src/library/scala/util/Either.scala) or the [TotallyLazy](https://code.google.com/p/totallylazy/source/browse/src/com/googlecode/totallylazy/Either.java) and [Functional Java](https://functionaljava.ci.cloudbees.com/job/master/javadoc/fj/data/Either.html) versions in Java.