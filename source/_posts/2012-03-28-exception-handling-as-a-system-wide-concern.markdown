---
name: exception-handling-as-a-system-wide-concern
layout: post
title: Exception Handling as a System Wide Concern
time: 2012-03-28 06:00:00 +00:00
categories: java rest object-oriented exceptions
comments: true
sidebar : false
series: Exception Handling
description: "Be more explicit about handling exceptions as a system wide concern. Examples of identifying boundaries to catch and deal with exceptions at appropriate & coherent points."
keywords: "exception handling, system wide policy for exception handling, java"
---

It's not ok to handle exceptions in an ad-hoc way. Exception handling should be a **system wide concern**. That means catching an exception, arbitrarily logging it before rethrowing isn't a good idea. We should be carefully considering _when_ and _how_ to handle exceptions. With a high level strategy, things just become easier. You focus exception handling to just a few places making it easy to test and easy to apply consistently.

In this post, we'll take a closer look with some examples.

<!-- more -->

To help make the strategy explicit, it's a good general approach to deal with exceptions at the boundaries of your system. However, recognising the boundaries can be tricky. The UI is an obvious boundary. Here, the user will likely be interested that something went wrong. Architectural "layers" can be more subtle. For example, any internal API is a candidate but you have to consider them carefully. Lets take a look at a few examples, in each case we'll identify the boundary, _when_ to catch exceptions and _how_ to deal with them. Effectively, we'll define a system wide strategy for each of the following.

* Low level exceptions which propagate to the UI
* An example of an externally facing API, in our case, a RESTful service
* Maintaining data atomicity in the face of failures


## The UI Boundary

A user probably isn't interested in seeing details of the majority of your exceptions. A user should certainly not be presented with a Java stack trace when visiting a public web site. 

Lets have a look at the example when a user's session times out. The server will generate a `SessionExpiredException` on subsequent requests but we don't want to relay this to the user.

For the _when_, most web UI frameworks have a convenient mechanism. In the servlet space, you can declaratively configure a page to be displayed based on an exception type.

{% codeblock lang:xml %}
<error-page>
    <exception-type>bad.robot.example.SessionExpiredException</exception-type>
    <location>/login</location>
</error-page>
<error-page>
    <exception-type>bad.robot.example.Defect</exception-type>
    <location>/internalServerError</location>
</error-page>
{% endcodeblock %}


For the _how_, the approach at this layer is to _translate_ un underlying exception into something appropriate. This could just mean something that is more presentable to the user. In the example above, when the server is asked to work with a session that has expired, it will generate the `SessionExpiredException`. This in turn causes the `login` page to be displayed prompting the user to log back in. No stack traces appear and we allow the user to continue working.

## The API Boundary

Lets consider a RESTful web service that allows a client to `GET` customer details via a URL. To get the most out of HTTP interoperability, the correct response to a request for unknown customer details is to return the HTTP response code `404` (Not Found). In the backend however, we throw a `CustomerNotFoundException`.

For the _when_, again, this layer is about _translation_. We would like to turn the `Exception` into a HTTP response code at the point at which the response is generated. We can propagate the exception up through the stack until the last possible point.

For [Jersey](http://jersey.java.net/), this means the _how_ is taken care of declaratively by providing an [`ExceptionMapper`](http://jersey.java.net/nonav/documentation/latest/user-guide.html#d4e435) as below.

{% codeblock lang:java %}
@Provider
public class NotFoundExceptionMapper implements ExceptionMapper<NotFoundException> {
    public Response toResponse(CustomerNotFoundException notFound) {
        return Response.status(404).entity(notFound.getMessage()).build();
    }
}
{% endcodeblock %}

The above turns a `CustomerNotFoundException` into the correct response code and adds a message to the response body. We encapsulate the `CustomerNotFoundException` by only allowing a single, narrow constructor.

{% codeblock lang:java %}
public class NotFoundException {
    public NotFound(Identifier identifier) {
        super(format("Could not find customer \"%s\"", identifier));
    }
}
{% endcodeblock %}


Then we can complete the task by defining a default exception handler to turn any unexpected exceptions into an internal server errors (HTTP `500`).

{% codeblock lang:java %}
@Provider
public class RuntimeExceptionMapper implements ExceptionMapper<Throwable> {
    public Response toResponse(Throwable exception) {
        return Response.status(500).entity(exception).build();
    }
}
{% endcodeblock %}

With this addition, we've implemented our system wide policy. All exceptions will be handled consistently thanks to the class hierarchy of `Throwable`. 

## The Database Transaction Boundary

When we're performing various database interactions in the context of a business operation, we'll likely want to maintain atomicity in the event of one of the interactions failing. The typical example is a bank account transfer. We'll credit one account then debit the other. If something goes wrong, we want to rollback. Otherwise we'd be left in an inconsistent state. 

Database transactions are the typical solution to this class of problem. We'll like to start a transaction and perform some _unit of work_ before finally committing. If a problem occurs during the execution, we should rollback. We don't want to do this ad-hoc with various catch statements. If we did, it would be hard to manage and to be sure we've got all the cases. We could even 'double up' and handle exceptions twice.

So for the _when_, unlike the declarative examples above, we can put a more imperative mechanism in place and ensure all database work uses the method below.

{% codeblock lang:java %}
public <T, E extends Exception> T run(UnitOfWork<T, E> unitOfWork) throws Throwable {
	Session session = sessionProvider.getCurrentSession();
	Transaction transaction = session.beginTransaction();
	try {
		T result = unitOfWork.execute(sessionProvider);
		transaction.commit();
		return result;
	} catch (Throwable e) {
		transaction.rollback();
		throw e;
	} finally {
		if (session.isOpen())
			session.close();
	}
}
{% endcodeblock %}

This also describes the _how_. We've chosen to handle the exception by rolling back the transaction and interestingly, rethrowing the exception. Although we've identified this database interaction as a boundary, by rethrowing the exception, we're recognising that there are additional boundaries to consider. In the context of a database call, for example, the exception could propagate up to the UI. We've handled the exception here to maintain data integrity _and_ allowed other exception handling policies to be applied. It's a good example of an _internal boundary_.

For example; two sales clerks try and update a customer's details at the same time in their web app causing a conflict. Hibernate detects the problem and throws a `OptimisticLockException`. Our database exception handling policy kicks in to rollback one of the transactions. It rethrows the exception which the web app redirects to an error page listing the diff and allowing the user to merge and retry.

See a [previous article]({{ root_url }}/blog/2012/01/29/transaction-management-without/) for more details about this kind of approach to transaction management.



## Some Parting Tips

We've talked about a lot here. Hopefully, the examples demonstrate the idea and here's a few parting tips.

* Identify the boundaries (and so _when_ to handle).
* Define a general handling approach for each boundary (_how_ to handle).
* Application specific exception subclasses should be _specialised_.
* Exceptions are objects too; think OO.
* Never catch an exception and rethrow verbatim. 
* However, if required, do _translate_ an exception into another _only_ at the boundaries.
* Don't forget that boundaries can be internal, just be explicit about where they are.

To see an example of more specialism in exception-types, see the next article [Building Better Exceptions]({{ root_url }}/blog/2012/03/29/building-better-exceptions/).

Remember though, there is no spoon. Feel free to discard these tips if they don't apply. After all, you may have different constraints or you may just know better.
