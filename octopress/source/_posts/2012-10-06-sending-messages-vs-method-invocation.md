---
layout: post
title: "Sending Messages vs Method Invocation"
pubDate: 2012-10-06 12:12
comments: true
categories: java object-oriented objective-c
sidebar: false
published: true
keywords: "message sending, objective-c, smalltalk, java, object-oriented, method invocation"
description: "What's the difference between sending an object a message and just invoking a method on an object? Why is a function different than a method?"
---

{% img right ../../../../../images/letter.jpg  'Send a message'%}

In object-oriented languages, some people talk about sending messages whilst others talk about invoking methods. In this post, we'll take a look at the conceptual difference in terminology and the more concrete, technical differences. Whilst we're on the topic, we'll look at the difference between a function and a method and discuss the difference between an object reference and a pointer. 

<!-- more -->


## Sending Messages

The terminology of sending a message to an object is partly historical. Languages like Smalltalk adopted it as a metaphor when working with objects. To understand why the metaphor is useful, we have to look at things before the advent of object oriented languages. In these days, procedural programming relied on subroutines (functions and procedures) to modify state. With no concept of "objects", state is simply associated with data structures. So applying a function to those structures would produce new state and applying a procedure would modify state.

With the arrival of "objects" to encapsulate state *and* behaviour, the messaging metaphor invites us to think about objects performing their own operations. Objects communicate by sending each other *messages*. Instead of calling a function directly in procedural programming, you send a message to an object requesting it to perform one of it's own subroutines. This allows us to think about *methods* in more abstract terms. Rather than think about data structures and the functions (and procedures) that affect them, we can focus on _behaviours_ [2].

> So sending messages helps us think in object-oriented terms rather than procedural or functional terms; we think in terms of behaviours rather than data structures. However, there is also a more concrete, technical difference.

Sending a message means the receiving object decides how to handle a message whilst a call to a function (or procedure) is a more static or class level notion [1]. In lanaguages like Java, the function (or procedure) lookup is still done, it's just done behind the scenes at runtime. By calling a method, for example, `person.eat(apple)`, the reference to `person` allows the JVM to associate the object with the procedure `eat`. It's a process called [dynamic dispatch](http://en.wikipedia.org/wiki/Dynamic_dispatch).

It's very similar in concept to the distinction between functions and methods.



## Functions vs Methods

Functions and procedures are [subroutines](http://en.wikipedia.org/wiki/Subroutine) disassociated from the data they act upon. Methods on the other hand are subroutines associated with objects. Functions are class level subroutines whereas methods are object level subroutines. For example, a *method* in Objective-C, is compiled down to a C *function* with additional parameters, one of which is the receiver object (`id`). It associates the function with this object.

Lets have a look at that in detail. For example, our method above would look like the following in Objective-C.

``` objective-c
- (void) eat:(Food*) food {
    // nom nom nom
}
```

The equivalent C function, would look like this. It isn't associated with an instance of a class and would be globally available to all modules. It doesn't make sense in the object-oriented world as there is no noun associated with the action. There is no *thing* eating the food. The act of eating simply affects some data structure. A C function is equivalent to a static class method in Java [3]. 


``` c
void eat(Food* food) {
    // nom nom nom
}
```

Objective-C would compile down the method above into a C function something like the following [3, pg 96-97][4]. The important thing to note is the `id` parameter, which is the receiving object of the message.

``` objective-c
void eat(id self, SEL _cmd, Food* food) {
    // nom nom nom
}
```

## Object References

So where does object references come in?

Java uses *object references* not *pointers*. Pointers are variables who's *value* is an address in memory. With pointer arithmetic, you can manually manipulate this value to zip around memory locations. Java prevents you from directly accessing memory locations directly like this. Because a pointer is really just a memory location, it can point to anything, a integer, a float, a `struct` or even to a function [3]. Java's object references point to objects only.

So in [1] when [Chisnall](https://www.informit.com/articles/printerfriendly.aspx?p=1571983) says "in Java, a message call looks like a call to a function pointer in a C structure", he's referring to a C structure that contains a pointer to a function being dereferenced and how Java's method invocation syntax looks similar. You access a C structure using the dot notation, so a structure containing a pointer to our C function might look like the following.  

``` c
struct person {
   int (*eat)(void *);
};
struct person person;
```
and dereferencing it would look similar to Java

``` c
person.eat(apple)
```

In the context of his article, Chisnall is highlighting that Objective-C makes it's syntax as distinct as possible when talking about message sending. It's a useful idea as it makes the terminology of sending messages explicit and baked into the way you work with the language. With Java, you have to work harder to conceptually take up the metaphor. Java's terminology is around calling a method so it brushes over some of these subtleties.

## Roundup

For me, the challenge of working with object-oriented designs is keeping my object-oriented head on. It's easy to slip into a procedural or functional way of coding but when the domain fits, I find that object-oriented solutions just *click*. To that end, I jump on any tool that helps remind me to think in terms of objects and their intercommunication, behaviours not accessors (tell don't ask). I find the message sending metaphor useful in doing just that.  

## References

<div>
    <script type="text/javascript">
    function trackOutboundLink(link, category, action) {

        try {
            _gaq.push(['_trackEvent', category , action]);
        } catch(err){}

        setTimeout(function() {
            document.location.href = link.href;
        }, 100);
    }
    </script>
</div>

[1] Objective-C for Java Programmers, [Part 1](https://www.informit.com/articles/printerfriendly.aspx?p=1568732), [Part 2](https://www.informit.com/articles/printerfriendly.aspx?p=1571983), David Chisnall   
[2] [Object-Oriented Programming with Objective-C](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/OOP_ObjC/Introduction/Introduction.html), Apple.      
[3] <a href="http://amzn.to/Tm1Sh1" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">Learn Objective-C for Java Developers</a>, James Bucanek
[4] [Object-C Messages](http://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html), Mike Ash

