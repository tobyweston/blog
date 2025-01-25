---
name: inheritance-vs-composition
title: Inheritance vs Composition
pubDate: 2009-01-24 12:12:00 +00:00
categories: java object-oriented
sidebar : false
keywords: "inheritance vs composition, inheritance vs aggregation"
description: "Java's stack class isn't a stack at all! It favours inheritance over composition causing it to no longer be just a stack."
---

When interviewing, I often like to ask a candidate to discuss inheritance vs composition using a `Stack` as an example.
  

### Example 1.

``` java
public class EvilStack<T> extends Vector<T> {
    public T pop() {
        // ...
    }
    public void push(T item) {
        // ...
    }
}
```

### Example 2.

``` java
public class Stack<T> {
    private Vector<T> items = new Vector<T>();
    public T pop() {
        // ...
    }
    public void push(T item) {
        // ...
    }
}
```

  
Extending `Vector` as in example 1 weakens the encapsulation of the class. Suddenly, methods to get and insert elements at specific positions are available to clients of the stack. We move from trying to create a well behaved LIFO stack to creating a socially irresponsible monster: an `EvilStack`.

  
So I was surprised when looking at the Java source to see that `java.util.Stack` actually extends `Vector`! Naughty and things [aren't any better in Java 7 and 8](/blog/2013/01/10/stack-vs-deque).


