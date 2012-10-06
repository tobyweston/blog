---
layout: post
title: "Sending Messages vs Method Invocation"
date: 2012-10-05 04:12
comments: true
categories: java object-oriented objective-c
sidebar: false
published: false
keywords: "message sending, objective-c, smalltalk, java, object-oriented, method invocation"
description: "What's the difference between sending an object a message and just invoking a method on an object? Why is a function different than a method?"
---

{% img right ../../../../../images/letter.jpg  'Send a message'%}

People often talk about sending a message in object-oriented languages whilst others talk about invoking methods on objects? What's the difference? Whilst we're on the topic, what's the difference between a function and a method? Is there a difference between an object reference and a pointer? What's a function pointer?

<!-- more -->


## Sending Messages

The terminology of sending a message to an object is partly historical. Languages like Smalltalk adopted it as a metaphor when working with objects. To understand why the metaphor is useful, we have to look at things before the advent of object oriented languages. In these days, procedural programming relied on subroutines (functions and procedures) to modify state. With no concept of "objects", state is simply associated with data structures. So applying a function to those structures would produce new state and applying a procedure would modify state.

With the arrival of "objects" to encapsulate state *and* behaviour, the messaging metaphor invites us to think about objects performing their own operations. Objects communicate by sending each other *messages*. Instead of calling a method as you would a function in procedural programming, you send a message to an object requesting it to perform one of its methods. This allows us to think about *methods* in more abstract terms. Rather than think about data structures and the functions (and procedures) that affect them, we can focus on _behaviours_ [2].

> So, sending messages helps us think in object-oriented terms rather than procedural or functional terms but there is also a more concrete, technical difference.

Sending a message means the receiving object decides how to handle a message whilst a call to a function (or procedure) is a more static thing [1]. In lanaguages like Java, the function (or procedure) lookup is still done, it's just done behind the scenes at runtime. By calling a method, for example, `person.eat(apple)`, the reference to `person` allows the JVM to associate the object with the procedure `eat`. This is called [dynamic dispatch](http://en.wikipedia.org/wiki/Dynamic_dispatch).

It's very similar in concept as the distinction between functions and methods.



## Functions vs Methods

Functions and procedures are [subroutines](http://en.wikipedia.org/wiki/Subroutine) disassociated from the data they act upon. Methods on the other hand are subroutines associated with objects. Functions are class level subroutines whereas methods are object level subroutines. For example, a *method* in Objective-C, is compiled down to a C *function* with additional parameters, one of which is the receiver object (`id`). It associates the function with this object.

Lets have a look at that in detail. For example, our method above would look like the following in Objective-C.

{% codeblock Objective-C Method lang:objc %}
- (void) eat:(Food*) food {
    // nom nom nom
}
{% endcodeblock %}


The equivalent C function, would look like this. It isn't associated with an instance of a class and would be globally available to all modules. It doesn't make sense in the object-oriented world as there is no noun associated with the action. There is no *thing* eating the food. The act of eating simply affects some data structure. A C function is equivalent to a static class method in Java [3]. 


{% codeblock C Function lang:c %}
void eat(Food* food) {
    // nom nom nom
}
{% endcodeblock %}


Objective-C would compile down the method above into a C function something like the following [3, pg 96-97][4]. The important thing to note is the `id` parameter, which is the receiving object of the message.

{% codeblock Objective C method compiled into a C Function lang:objc %}
void eat(id self, SEL _cmd, Food* food) {
    // nom nom nom
}
{% endcodeblock %}


## Object References

So where does object references come in?

Java uses *object references* not *pointers*. Pointers are just integer values, literally pointing to an address in memory. For example, with pointer arithmetic, you can manually zip around memory locations. Java prevents you from directly accessing memory locations like this. Because a pointer is really just a memory location, it can point to anything, a integer, a float, a `struct` or even to a function [3].

So when [Chisnall](https://www.informit.com/articles/printerfriendly.aspx?p=1571983) says "in Java, a message call looks like a call to a function pointer in a C structure", he's referring to a C structure that contains a pointer to a function being dereferenced and how Java's method invocation looks similar. You access a C structure using the dot notation, so a structure containing a pointer to our C function might look like the following.  

{% codeblock lang:c %}
struct person {
   int (* eat)(void *);
};
{% endcodeblock %}

and dereferencing it would look similar to Java

{% codeblock lang:c %}
person.eat
{% endcodeblock %}

### References

[1] [Objective-C for Java Programmers, Part 1, David Chisnall](https://www.informit.com/articles/printerfriendly.aspx?p=1568732)    
[2] [Object-Oriented Programming with Objective-C, Apple.](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/OOP_ObjC/Introduction/Introduction.html)    
[3] [Learn Objective-C for Java Developers, James Bucanek](http://www.amazon.co.uk/Learn-Objective-C-Java-Developers-Series/dp/1430223693/ref=sr_1_fkmr0_1?ie=UTF8&qid=1349518202&sr=8-1-fkmr0)    
[4] [Object-C Messages, Mike Ash](http://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)    

http://stackoverflow.com/questions/3036330/method-vs-function-vs-procedure-vs-class