---
layout: post
title: "Scala Learning Curve"
date: 2014-11-25 07:09
comments: true
categories: scala
sidebar: false
published: false
keywords: "scala, scala learning curve, training, pluralsight"
description: "Scala's learning curve; expect a quick ramp up but a shallower increase (slow down) as you adopt more sophisticated and advanced functional features."
---

If you've just started to learn Scala and are wondering what to expect, it's fairly typical to experience a quick ramp up followed by a slower adoption of the more sophisticated features. In this post, I take about what I think is a typical learning curve. 

Taken from my forthcoming [Pluralsight](www.pluralsight.com) course, the chart below shows experience (or time) along the `x` axis and some measure of "learning" on the `y`. 

{% img ../../../../../images/learning_curve.png %}


<!-- more -->

## Milestone 1

When you first start, you can expect getting up to speed with the language to be a fairly steep incline. That's not to say that it's difficult to get to the first plateau, so by "steep", I really mean "short"; you can expect a relatively quick increment in learning.

You'll probably sit here for a bit applying what you've learnt and I see this as the first milestone; to be able to build object-oriented or imperative applications using language specific constructs and features but without necessarily adopting functional programming. Just like learning any other language in the Java/C family.
    

## Milestone 2

I see the next milestone as adopting functional programming techniques. 

This is much more challenging and likely to be a shallower curve. Typically this will involve using traditional architecture design but implementing functional programming techniques in the small. You can think of this approach as ["functional in the small, OO in the large"](http://www.johndcook.com/blog/2009/03/23/functional-in-the-small-oo-in-the-large/). Starting to embrace a new functional way of thinking and unlearning some of the traditional techniques can be hard, hence the shallower incline.

Concrete examples here are more than just language syntax, so things like [higher order and pure functions](http://baddotrobot.com/blog/2012/04/03/scala-as-a-functional-oo-hybrid/), [referential transparency](http://en.wikipedia.org/wiki/Referential_transparency_(computer_science)), immutability and side-affect free, more declarative coding; all the things that are typically offered by [pure](http://en.wikipedia.org/wiki/Pure_function) functional languages. The key thing here is that they're applied in small, isolated areas.


## Milestone 3

The next challenge is working towards a more cohesive functional design; this really means adopting a functional style at a system level; architecting the entire application as functions and abandoning the object-oriented style completely. 

Aiming for something like a Haskell application. So, all the concrete functional programming mechanisms above apply but throughout the system. Not to isolated areas but lifted to application-wide concerns. Picking up advanced libraries like Scalaz seems to go hand-in-hand at this point in the curve.


## As a Continuum

{% img ../../../../../images/continuum.png %}


You can also think of adoption as more of a continuum with traditional imperative programming on the left and pure functionally programming on the right. Haskell for example forces you down a functional design. As Scala is an OO/FP hybrid, it can only give you the tools, it can't enforce functional programming; you need discipline and experience in Scala to avoid mutating state. Haskell will physically stop you.

So as you start out on the continuum, you might be using Java and as you move to the right, libraries like [Functional Java](http://www.functionaljava.org/), [Totally Lazy](https://code.google.com/p/totallylazy/) and even [Java 8 features](https://leanpub.com/whatsnewjava8) help you adopt a more functional style. There gets a point though that a language switch, to Scala, helps even more. Functional idioms become a **language feature rather than a library feature**. The syntactical sugar of for-comprehensions are a good example.

##

As you carry on, using libraries like Scalaz makes it easier to a progress towards pure FP but remember that reaching the far right or top right quadrant of the learning curve isn't the goal in and of itself.
