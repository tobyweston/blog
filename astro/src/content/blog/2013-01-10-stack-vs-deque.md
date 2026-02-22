---
title: "Java Stack vs Deque"
subTitle: "Why Oracle's recommendation breaks encapsulation and how to fix it"
pubDate: '2013-01-10'
categories: 'java'
keywords: "Java Stack, Deque, ArrayDeque, data structures, LIFO, collection framework, stack implementation"
description: "Java's Stack class is a legacy class with known problems. Use Deque (specifically ArrayDeque) instead for a proper last-in-first-out stack implementation."
heroImage: "/images/heroes/architecture.jpg"
---

Java has long had a [badly written](/blog/2009-01-24-inheritance-vs-composition/) implementation of a stack. The stack is a great example of single responsibility; it's supposed to implement LIFO and only LIFO behaviour. Java ignores this principle with the default implementation of `Stack`. It extends `Vector` and so is implemented in terms of inheritance rather than aggregation. It's _both_ a `Stack` *and* a `Vector`. They haven't made the situation any better when recently deprecating `Stack` in favour of `Deque`.


## Don't Use Deque

I can understand that Sun/Oracle never corrected the mistake given Java's principle of backwards compatibility but I was surprised when I noticed they recommend using Deque instead.

> A more complete and consistent set of LIFO stack operations is provided by the Deque interface and its implementations, which should be used in preference to this class.   
> — <cite>Oracle Documentation for Stack http://docs.oracle.com/javase/7/docs/api/index.html?java/util/Stack.html </cite>

A deque is a double ended queue, by definition it is **not** a stack. It allows LIFO *and* FIFO behaviour. I can't see why Sun/Oracle are so happy to abandon encapsulation like this.


## Why is this Important?

If you don't control what operations a stack class can perform, you open up the class for non-stack like uses. For example, you might be able to insert objects into the middle of the stack. If client code starts using this behaviour, there's immediately a  dependency on it. The client code now depends on the _implementation_ and not the _role_ of your class. You won't be able to swap out the implementation of your stack without potentially forcing changes to clients.

You could argue that this is the client code's choice. For classes with well known semantics like the stack, any client using non-stack behaviour should appreciate the coupling and be able to make an informed decision. For more domain or business specific behaviours however, it's very likely that clients will benefit by avoiding this coupling. Forcing clients to depend on defined roles rather than implementation allows for flexibility of substitution.


## Use Encapsulation

It seems like we should really use a `Stack` abstraction to define the _role_ and composition to implement the stack. That way, we're able to substitute any implementation and expect our clients to still work. We won't be able to break encapsulation by exposing methods we shouldn't and we'll allow clients to substitute alternative implementations.

For example:

``` java
public interface Stack<T> {
    void push(T object);
    T pop();
}
```
``` java
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
```
It's important to note that I'm not saying use composition to enforce encapsulation though. The example above restricts what can be done with the underlying `Deque`. It's _hiding the implementation details_ and exposing the role through an interface. It's using information hiding to achieve encapsulation. That's not to say that you can't achieve the same thing using inheritance.

For example, the naive `BoundedStack` implementation below is still a `Stack`. It inherits it, it has an "is a" relationship with `Stack`. Any stack implementation most certainly does not have a "is a" relationship with list (`Vector`) or double ended queue (`Deque`).

``` java
public class BoundedStack<T> extends DequeStack<T> {

    // ...

    @Override
    public void push(T object) {
        if (count < UPPER_BOUND) {
            count++;
            deque.addFirst(object);
        }
    }

    @Override
    public T pop() {
        count--;
        return deque.removeFirst();
    }
}
```

## Related

See [Information Hiding](https://en.wikipedia.org/wiki/Information_hiding) on Wikipedia.
