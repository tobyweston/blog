---
layout: post
title: "Java Stack vs Deque"
date: 2013-01-10 12:12
comments: true
categories: java object-oriented
sidebar: false
published: false
keywords: "java stack, inheritance vs composition, inheritance vs aggregation, deque, LIFO"
description: ""
---

Java has long had a [badly written](blog/2009/01/24/inheritance-vs-composition/) implementation of a stack. The stack is a great example of single responsibility; it's supposed to implement LIFO and only LIFO behaviour. Java ignores this principle with the default implementation of `Stack`. It extends `Vector` and so is implemented in terms of inheritance rather than aggregation. It's _both_ a `Stack` and a `Vector`. They haven't made the situation any better when recently deprecating `Stack` in favour of `Deque`.

<!-- more -->

## Don't Use Deque

I can understand that Sun/Oracle never corrected the mistake given Java's principle of backwards compatibility but I was surprised when I noticed they recommend using Deque instead. From `Stack`s [documentation](http://docs.oracle.com/javase/7/docs/api/index.html?java/util/Stack.html)

	> A more complete and consistent set of LIFO stack operations is provided by the Deque interface and its implementations, which should be used in preference to this class.


A deque is a double ended queue, but definition it is **not** a stack. It allows LIFO **and** FIFO behaviour. I can't see why Sun/Oracle are so happy to abandon encapsulation like this.


## Why is this Important?

If you don't control what operations a stack class can perform, you open up the class for non-stack like uses. For example, you could insert objects into the middle of the stack. If client code starts using this behaviour, they create a dependency to it. The client code now depends on the _implementation_ and not the _role_ of your class. You won't be able to change your stack (to use a thread safe structure for example) without potentially forcing changes to clients. You could, however, argue that this is the client code's choice. For classes with well known semantics like the stack, any client using non-stack behaviour should appreciate the coupling and be able to make an informed decision. For more domain or business specific behaviours, it's very likely that they'll benefit by avoiding this coupling.


## Use Encapsulation

It seems like we should really use a `Stack` interface and composition to implement a stack. That way, we're able to substitute any implementation and expect our clients to still work. We won't be able to break encapsulation and expose methods we shouldn't.

For example,

{% codeblock lang:java %}
    public interface Stack<T> {
        void push(T object);
        T pop();
    }
{% endcodeblock %}

{% codeblock lang:java %}
public class DequeStack<T> implements Stack<T> {

    private final Deque<T> deque = new ArrayDeque<T>();

    @Override
    public void push(T object) {
        deque.addFirst(object);
    }

    @Override
    public T pop() {
        return deque.removeFirst();
    }
}
{% endcodeblock %}

It's important to note that I'm not saying use composition to enforce encapsulation. The example above restricts what can be done with the underlying `Deque`. It's _hiding the implementation details_ and so is using information hiding to achieve encapsulation. That's not to say that you can't achieve the same thing using inheritance.

For example, a `BoundedStack` is still a vehicle with four wheels that extends `Stack`?

{% codeblock lang:java %}
public class BoundedStack<T> extends DequeStack<T> {

    // ...

    @Override
    public void push(T object) {
        count++;
        if (count < UPPER_BOUND)
            deque.addFirst(object);
    }

    @Override
    public T pop() {
        count--;
        return deque.removeFirst();
    }
}
{% endcodeblock %}

{% wiki Stack_(abstract_data_type) %}


