---
layout: post
title: "Dealing with Exceptions as Monads"
date: 2014-05-27 05:12
comments: true
categories: java java8 exception-handling scala
sidebar: false
series: Exception Handling
published: false
keywords: "java 8, java, monads, either, option, monadically"
description: "Deal with exceptions monadically with Java 8 and the Either class"
---

In some [previous posts](http://baddotrobot.com/blog/categories/exceptions/), I wrote about treating exceptions as a system wide concern, in this post, I extend that idea and talk about consistently treating exceptions as monads and distinguish between real exception behaviour and just code that didn't return what you wanted. Pure functional languages often discourage the use of exceptions because when they are used to control execution flow, they introduce side-affects and violate [purity of function](http://baddotrobot.com/blog/2012/04/03/scala-as-a-functional-oo-hybrid/).

<!-- more -->

## Object-Oriented

The norm for object oriented code is to use exceptions to control execution flow. When you have a method that can return `true` or `false` _and_ throw an exception, it's as if it can return three things. It forces clients to have to reason about logic that has nothing to do with the function of the method. It's complicated and often makes it hard to treat exceptions consistently across the entire application.

? runtime vs checked ?

## Functional

So what can we learn from functional programing languages? Exceptions are a fact of life, unexpected things can happen with your code and you still need to deal with them. The subtlety here is that functional languages emphasize the *unexpected* part with exceptions. They try and discourage you from using exceptions for dealing with known branches of logic and instead use them like Java uses `Error`s. This means thinking of exceptions of _exceptional behaviour_ and not Java's notion of checked `Exceptions`. 

So how do languages like Scala discourage you using them like Java? They usually offer alternative mechanisms. Scala for example has the `Either` and `Try` classes. These classes allow you to express using the type system, that a method was successful or unsuccessful independently from the return value. As an additional bonus, because they are [monadic](http://debasishg.blogspot.co.uk/2008/03/monads-another-way-to-abstract.html), you can deal with exceptional and expected behaviour consistently in code. That means you can use the same structures to process the positive and the negative case without resorting to `catch` blocks.
  
## Either in Java
  
For example, let's say we have a method `getExpenses` to get this months expenses from my online accountant's web service. As it goes over HTTP, it could fail because of some network problem or it could fail because it couldn't unmarshall an object to an `Expense`. Once we have the list of `Expenses`, we can can produce a report (just using `System.out`).

???????

{% codeblock lang:java %}
Expenses expenses = new Expenses(transactions.stream().map(toExpense()).collect(toList()));
expenses.forEach((e) -> System.out.println(e));

{% endcodeblock %}



{% codeblock lang:java %}
List<Either<Pair<Expense, Throwable>, A>> results = getExpenses().collect(toList());

Stream<Pair<Expense, Throwable>> failures = results.stream().flatMap(either -> either.left());
failures.forEach(failure -> ... );

Stream<A> successes = results.stream().flatMap(either -> either.right());
successes.forEach(success -> ... );
{% endcodeblock %}
