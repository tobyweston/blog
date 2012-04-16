---
name: building-better-exceptions
layout: post
title: Building Better Exceptions
time: 2012-03-28 06:00:00 +00:00
categories: java testing object-oriented
comments: true
published: false
---

In the [previous post]({{ root_url }}/blog/2012/03/28/exception-handling-as-a-system-wide-concern) in the series, we looked at being more explicit about a system's exception handling policies. By identifying the boundaries within your system, you issolate the points at which you handle exceptions. 

This post takes the idea further by talking about exceptions as _real_ objects and suggests only ever creating sub-classes of `RuntimeException` for your application exceptions. Once exception handling points are issolated, testing becomes more straightforward and we can reduce the noise checked exceptions promote.

<!-- more -->

## Exceptions are Objects

We tend to think of exceptions as beans; objects with a `message` that we get and display. It's easy to forget that exceptions are objects too. How often do you see this type of thing in the same codebase.

	throw new BadRequestException("the field 'customer' is missing from the request");
	throw new BadRequestException("'customer' is missing");
	throw new BadRequestException("can not parse request" );

It's an example of bad encapsulation in the `BadRequestException`. It's hard to tell if the examples above should be handled the same or differently. There's certainly an inconsitency between the wording of the first two. It's not clear where the message is going to end up? A better idea would be to create sub-classes for each.

	public class MissingFieldException extends BadRequestException {
		public MissingFieldException(Field field) {
			super();
			this.field = field;
		} 	
	}

All other constructors have been disabled so the exception can only be constructed as we intend. It can still be handled in a `catch` block built for `BadRequest` [and it's here that we would decide how to map the exception type to a presentable form]. We've intentionally avoided something like

	public MissingFieldException(Field field) {
		super("the field '" + "'" is missing from the request");
	} 		
	
becuase we're saying the message is completly unimportant to the exception. It's the handling that's important and its in the catch block that we can map to a message (if appropriate). For example, at the UI, we may map the	exception to a message for display but at an internal boundary, we may generate an event for support which maps to a different message.
	
Tell don't ask
Encapsulate



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
