---
title: "Don't name classes 'Impl'"
pubDate: "2023-01-01"
categories: 'java'
keywords: "java naming conventions, implementation classes, interfaces, code naming, software design, maintainability, readability"
description: "Naming your implementation classes with a 'Impl' postfix, obscures intent and hurts maintainability. Learn why descriptive names matter for understanding behavior and composing flexible applications."
---

As part of my 5 Coding Habits that are Hurting you series, I'm trying to call out when habits in code often lead to hidden costs. Today is the turn of the infamous Impl class names.

# Reusing Behaviour

What's the main reason to have an interface in Java? or trait in Scala? or protocol in Swift? or whatever the equivalent is in your language of choice? It's often to define a contract for behaviour that can be implemented by one or more classes. The interface defines the _what_ and the implementation defines the _how_. This is a fundamental principle of object-oriented design. It allows us to separate concerns, promote code reuse, and create flexible and maintainable systems.

If your not sure why you're creating interfaces or if you generally postfix the name of your implementation with `Impl`, then you've probably picked up a habit. Guess what? Its hurting you.

Interfaces are great to define **behavior** that can be reused. Classes with actual implementation (say abstract classes) can be used to reuse behaviour and **implementation**. So the implication is that you should use interfaces to define behaviour and then supply **concrete implementations** that very likely differ in implementation but conform to the same contract. It's super useful when defining dependencies or collaborators to components. You can then compose application behaviour (the broader sense of how a system behaves) by swapping out implementations. The build on this is to use **test doubles** to help you test without having to assemble large complex apps in your test code.

So, for example, if you have a behaviour capturing collection semantics, say a stack.

```java
interface Stack<A> {
    void push(A element);
    A pop();
}
```
...and if you name your implementation like this.

```java
class StackImpl implements Stack
```

...you're doing yourself (and team) a disservice. What would you name another implementation? `Stack2Impl`? How do they differ? I should be able to tell from the name.

How you name things is so important. What is the single more important thing you want to convey in the name? Is it that it's an _implementation_? I know it's an implementation, it says it right there in the class declaration and my IDE will help discover that fact.

Is it important that the name convey the mechanics of the implementation? For example, should I reveal my `Stack` is based on an `Array`?

```java
class ArrayStack implements Stack
```

...and an alternative implementation is of fixed size?

```java
class FixedSizeStack implements Stack
```

From a testing context, I could clarify what kind of test double I'm using:

```java
class StackStub implements Stack
```

If may not be obvious why this is hurting you, but it's about **maintainability** and **readability**. By naming your class `Impl`, you're not revealing anything that isn't trivial for the reader to discover. You're forcing them to look at the specific implementation to understand if the implementation might be a good fit for their use case. A subtle side effect of the non-descriptive naming is that it can encourage you not to think about the interface as a placeholder for behaviour. It will likely mean that you're not thinking about alternatives and probably not using the interface as a way to compose flexible applications - setting up dependencies that can be swapped out easily. This in turn means testing is hard and the system inflexible to change.