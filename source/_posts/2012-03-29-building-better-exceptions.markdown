---
name: building-better-exceptions
layout: post
title: Building Better Exceptions
time: 2012-03-28 06:00:00 +00:00
categories: java testing
comments: true
published: false
---

blar blar blar

<!-- more -->

## Exceptions are Objects

Tell don't ask
Encapsulate

To see an example of building more specific exception sub-types, see the next article [Building Better Exceptions]({{ root_url }}/blog/2012/03/29/building-better-exceptions/).

## The Impact on Testing

If we handle exceptions _only_ at the boundaries, we do so based on _type_ in the `catch` block. Even here, we shouldn't be concerned with the internals of the exception. The handler can _tell_ the exception rather than _ask_. We can start to be more specific with our exception types; our sub-classes can encapsulate, for example, the exception message.

A further inference is that we should _never need to test the content of the message in a unit test_ for a class that throws it. To test that a class throws an exception, we should do just that and nothing more. That's not to say that the boundary classes that actually _use_ the exception shouldn't be tested. It's at this point that, for example, we could test that messages originating within an exception appear on a UI. Applying OO goodness to an exception means it can carry more _behaviour_ and so the unit test for it can do more. How many _unit_ tests have you written for an `Exception` class?


## Only using Runtime Exceptions

As we saw in the [previous article]({{ root_url }}/2012/03/28/never-assert-against-exception-messages), if you issolate exception handling to a specific boundary, you emphasise the point at which exceptions are caught. If you're
catching and dealing with exceptions in a single, well known place, why would you need to use checked exceptions?

Checked exceptions cause noise. That's all. Nothing else bad about them but they imply a defensive style of
programming that has no place in the brave world of XP. The alternative, to throw only runtime exceptions, seems fraut
 with danger. What if you forget to catch it? If you've setup a exception handling as a system wide policy,
 you would have already established where to catch them and you'll have programmatically prevented that scenario.

 If that's truely the case, you can create application specific exceptions that sub-class `RuntimeException` and
 clean up the codebase consideribly. However, it's a potentially bad idea to actually through `RuntimeException`.
 Why???? I generally consider `RuntimeExceptoin` as an abstract class. It doesn't make sense on its own becuase it
 implies any `catch` clause is too generic. Instead, create an root application exception that extends
 `RuntimeException`.

 {% codeblock lang:java %}
 public class BadRobotApplicationException extends RuntimeException {
    // ...
 }
 {% endcodeblock %}

 and inherit your specialised exceptions from here.


## Summary

- identify the boundaries (and so _when_ to handle)
- define a general handling approach (the _how_ to handle)
- use subclasses of `RuntimeException` to keep the code clean, catch these _only_ at the boundaries
- application specific exception subclasses should contain the specificifty (for example,
the message hardcoded in the constructor).
- exceptions are objects too; think OO.
- Never rethrow an exception verbatim. 
- However, if required, do _translate_ an exception into another at boundaries.
