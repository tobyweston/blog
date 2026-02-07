---
title: "Building Better Exceptions'"
pubDate: "2012-03-28'"
categories: 'java testing object-oriented exceptions'
keywords: "checked vs runtime exceptions, exception handling, java, LoD, tell don't ask, test exception message, never test exception message, testing exceptions, ports and adaptors"
description: "Isolate the internal boundaries within your system and isolate exception handling. Extend the idea and treat exceptions as real objects. Add behaviour, tell them do do things, don't ask"
---

In the [previous post](/blog/2012-03-28-exception-handling-as-a-system-wide-concern), we looked at being more explicit about a system's exception handling policies. By identifying the boundaries within your system, you isolate the points at which you handle exceptions.

This post takes the idea further by talking about exceptions as _real_ objects and suggests only ever creating subclasses of `RuntimeException` for your application exceptions. Once exception handling points are isolated, testing becomes more straightforward and we reduce the noise of checked exceptions. When we get it right, we should never need to assert against exception messages.

<!-- more -->

## Exceptions are Objects

We tend to think of exceptions as beans; objects with a `message` that we get and display. It's easy to forget that exceptions are objects too. How often do you see this type of thing in the same code base.

``` java
throw new BadRequestException("the field 'customer' is missing from the request");
throw new BadRequestException("'customer' is missing");
throw new BadRequestException("can not parse request" );
```

It's an example of bad encapsulation in the `BadRequestException` class. It's hard to tell if the examples above should be handled the same or differently. There's certainly an inconsistency between the wording of the first two. Are they the same error? It's also not clear where the message is going to end up? A better idea would be to create sub-classes for each.

``` java
public class MissingFieldException extends BadRequestException {
    public MissingFieldException(Field field) {
        super();
        this.field = field;
    }
}
```

All other constructors have been disabled so the exception can only be constructed as we intend. It can still be handled in a `catch` block built for `BadRequest` (and it's there that we would decide how to map the exception type to a presentable form). We've intentionally _avoided_ something like

``` java
public MissingFieldException(Field field) {
    super("the field '" + "' is missing from the request");
}
```
because the message is completely unimportant to the exception. It's the handling that's important and it's in the catch block that we can map to a message (if appropriate). We're encapsulating the internal details. For example, at the UI, we may map the exception to a message for display but at an internal boundary, we may generate an event for support staff that maps to a different message.

Applying object-oriented principles like encapsulation to exceptions means that they can do more than just be _caught_. As first class objects, they can carry _behaviour_ and so can be tested appropriately. How many _unit_ tests have you written for an `Exception` class?


## Tell. Don't ask

We can take this further and try to apply the [law of demeter](http://en.wikipedia.org/wiki/Law_of_Demeter) to our objects. Rather than _get_ something and perform conditional logic based on it, we should be able to _tell_ the object to do something. It can make decisions based on its internal, encapsulated data which means decision points are localised to appropriate places.

How do we apply this to exceptions? Well, now we've got nicely encapsulated data it's clear that the exception itself is responsible for _using_ it. In the example above, we've encapsulated a `field` object. The implication being that the exception may want to influence something based on it. This could be the simple case where the exception can _present itself to some object_, in this example an implementation of a `Description` interface.

``` java
public void applyTo(Description description) {
    description.append("the field").appendValue(field).append("is missing from the request");
}
```

## The Impact on Testing

If we handle exceptions _only_ at the boundaries, we do so based on _type_ in the `catch` block. Even at this point, we shouldn't ask for the internals of the exception and so we shouldn't have to _test against them_. The handler can _tell_ the exception rather than _ask_ and testing becomes much more straight forward.

> If a class throws an exception, _{" we should never need to test the content of the message in a unit test "}_ for that class. It's the class that would use the message that should be tested. However, if we've done things correctly, then no behaviour should depend on the message so what can we test?

The first part is to test that the handling class responds appropriately to the exception _type_ and that those exceptions are generated only at appropriate times. The second part is that if the handling class does depend on some internal details, we should encapsulate this, apply _tell don't ask_ and so can write simpler tests.

In this way, we're just applying the [ports and adaptors](/blog/2012/02/13/hexagonal-acceptance-testing) idea to write overlapping tests which combine for coverage but are still simple on their own.


## Only using Runtime Exceptions

If you isolate exception handling to a specific boundary, you emphasise the point at which exceptions are caught. If you're catching and dealing with exceptions in a single, well known place, why would you need to use checked exceptions?

Checked exceptions cause noise. That's all. Nothing else bad about them but they imply a defensive style of programming that has no place in the brave world of XP. The alternative, to throw only runtime exceptions, seems fraught with danger. What if you forget to catch it? If you've setup a exception handling as a system wide policy, you would have already established where to catch them and you'll have programmatically prevented that scenario.

 If that's truly the case, you can create application specific exceptions that sub-class `RuntimeException` and clean up the code base considerably. However, it's a potentially bad idea to actually throw `RuntimeException` as this subverts the explicit catching strategy. I generally consider `RuntimeException` as an abstract class. It doesn't make sense on its own because it implies any `catch` clause is too generic. Instead, create an root application exception that extends `RuntimeException`.

 ``` java
 public class BadRobotApplicationException extends RuntimeException {
    // ...
 }
 ```


In the next post [Scala Exception Handling](/blog/2012-03-30-scala-exception-handling), well take a look at how Scala embraces some of these ideas. For example, in Scala _all_ exceptions are based on `RuntimeException`.

