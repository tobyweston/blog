---
title: "Scala as a Functional OO Hybrid"
pubDate: "2012-04-03"
categories: 'scala functional-programming'
keywords: "Scala, functional programming, object-oriented, pure functions, side effects, referential transparency"
description: "Scala as a functional/OO hybrid: what does 'functional' really mean? Explores pure functions, side effects, and referential transparency in Scala."
heroImage: "/images/heroes/build-tools.jpg"
---

Scala is often described as a functional language but its as much object-oriented language as it is functional. In fact, functions in Scala _are_ objects. It's important to realise that Scala can be used to write programs in an _imperative_ style as well as a _functional_ style and to understand the context your working in. If you're clear about the style you're applying, you can get the most from the approach. Functional programming isn't a panacea and to build effective systems, you'll need to blend the approaches.


## Object-Oriented

Scala is a pure object-oriented language. There's no subverting it, there are no non-objects (such as Java's primitives like `int`) or static fields or methods which aren't members of an object (although there is the related idea of _companion object_). Every _value_ is an object including numeric types and _functions_. We have classes and traits and flexible mixin-based composition.

## Functional

Scala is also a functional language; it allows you define both _pure functions_ and _higher order functions_. It doesn't enforce this though which makes it even more important to understand if you're actually working with these ideas. Porting a Java application verbatim doesn't necessarily mean you're building with purely functional blocks.

Lets review these two ideas.

### Functions are First Class

Programming with higher order functions means that you can pass functions as arguments to other functions, create and return them or just store them. This allows us to build richer behaviour with function composition just like object composition in the object-oriented world. In practice, function composition tends to be finer grained but still allows us to test the _composites rather than the composition_. It's easier to test correctness of small functions like this especially when they are _pure functions_.

### Pure Functions

Another aspect of a functional language is that functions should not cause any side effects. They should operate by _transformation_ rather than _mutation_. That is to say a pure function should take arguments and return results but not modify the environment in which they operate. This [_purity of function_](http://en.wikipedia.org/wiki/Pure_function) is what enables [_referential transparency_](http://en.wikipedia.org/wiki/Referential_transparency_\(computer_science\)).

Although Odersky et al [1] describe referential transparency as literally being able to substitute a method call with its result without changing the semantics of a program, Subramaniam further relates the idea to facilitating concurrent programming [2].

## Final Thoughts

I think its important to bear these definitions in mind when working with Scala, if for no other reason than to be aware of the idioms available to each style and how best to leverage them.

A functional style can give great results for certain classes of problems but let's not forget that object-oriented solutions give huge advantages for other types of problems. It's easy to get caught up in the hype and think we've left object-oriented design behind when hybrid languages blur the lines, but if we're clear about what approach to use and when, we can blend approaches as appropriate. Just don't expect it to be easy!

## References

[1] [Programming in Scala](http://www.artima.com/shop/programming_in_scala), Martin Odersky et al, pg. 11-12.   
[2] [Functional Style of Programming](http://pragprog.com/magazines/2011-12/scala-for-the-intrigued) Venkat Subramaniam

