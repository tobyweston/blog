---
name: never-assert-against-exception-messages
layout: post
title: Never Assert Against Exception Messages
time: 2012-03-28 06:00:00 +00:00
categories: java 
comments: true
---

It's not ok to handle exceptions ad-hoc. To get the most out of it, exception handling should be a **system wide
concern**. That means catching an exception, arbitrarily logging something before rethrowing isn't a good idea. We
should be carefully considering _when_ and _how_ to handle exceptions. With a top level strategy, things just become easier.

To help make the strategy explicit, it's a good general approach to deal with exceptions at the boundaries of your
system. However, recognising the boundaries can be tricky. The UI is an obvious boundary. Here,
the user will likely be interested that something went wrong. Architecture "layers" can be more subtle. For example,
any internal API is a candidate. Lets take a look at a few examples, in each case we'll identify the
boundary, when to catch exceptions and how to handle them. Effectively, we'll define a system wide strategy for each
of the following.

* Low level exceptions which propogate to the UI
* An example of an externally facing API, in our case, a RESTful service
* Maintaining data atomicity in the face of failures

<!-- more -->

### UI Boundary

When, how

### API Boundary

When, how

### Database Transaction Boundary

When, how


## Only using Runtime Exceptions

Translating or respond. (?)

## The Impact on Testing

If we handle exceptions _only_ at the boundaries, we do so based on _type_ in the `catch` block. Even here,
we shouldn't be concerned with the internals of the exception. The handler can _tell_ the exception rather than _ask_
. We can start to be more specific with our exception types; our sub-classes can encapsulate, for example,
the exception message. To see an example of building more specific exception sub-types,
see the next article [Building Better Exceptions]().

A further inference is that we should never need to test the content of the message in a unit test for a class
that throws it. To test that a class throws an exception, we should do just that and nothing more. That's not to say
that the boundary classes that actually _use_ the exception shouldn't be tested. It's at this point that, for example,
we could test that messages originating within an exception appear on a UI but this is more of an _itegration_ test.
Applying OO goodness to the exception type also means that the unit test for the exception itself can exercise more and
 do so in a de-coupled way. Nom nom nom.


## Summary

- identify the boundaries (and so _when_ to handle)
- define a general handling approach (the _how_ to handle)
- use subclasses of `RuntimeException` to keep the code clean, catch these _only_ at the boundaries
- application specific exception subclasses should contain the specificifty (for example,
the message hardcoded in the constructor).
- exceptions are objects too; think OO.
