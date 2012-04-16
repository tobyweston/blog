---
name: wrapping-exceptions-is-dull
layout: post
title: Wrapping Exceptions is Dull
time: 2010-04-25 18:19:00 +01:00
categories: java tempus-fugit exceptions
comments: true
---

I'm totally bored of wrapping exceptions in Java,
  
{% codeblock lang:java %}
try {
   // do something
} catch (BoredomException e) {
   // do something else
}
{% endcodeblock %}

It's verbose, ugly and has nothing to do with what you're really trying to
convey. It's just noise (more or less). For example, when using the just
_dreadful_ Google Data API to access my calendar, I wrapped a couple of
underlying Google services to be able to mock. Each service wanted to throw a
bunch of Google specific exceptions which I, of course, wanted to rethrow as
application specific. Boring...

{% codeblock lang:java %}
public O call() throws CalendarException {
    try {
        return service.call();  // the call to the google service
    } catch (MalformedURLException e) {
        throw new CalendarException(BAD_URL_MESSAGE, e);
    } catch (IOException e) {
        throw new CalendarException(IO_EXCEPTION_MESSAGE, e);
    } catch (AuthenticationException e) {
        throw new CalendarException(AUTHENTICATION_MESSAGE, e);
    } catch (ServiceException e) {
        throw new CalendarException(SERVICE_EXCEPTION_MESSAGE, e);
    }
}
{% endcodeblock %}


  
If I didn't delegate like this, every service call would have to wrap and
handle the google exceptions. As I've done this a few times, I decided to add
it to [tempus-fugit](http://code.google.com/p/tempus-fugit/) as a
`ExceptionWrapper` class. Using this class, you can wrap a `Callable` to
rethrow any caught exception as some other (including the underlying exception
as the `cause`).

  
So, in a similar way to the above, the client can ignore any declared
exceptions and just rethrow them in-line. For example,

{% codeblock lang:java %}
wrapAnyException(new Callable<Object>() {
    @Override
    public Object call() throws ServiceException {
         // nasty code throwing a bunch of exceptions
    }
}, with(CalendarException.class));
{% endcodeblock %}

when this is in-lined further, it hopefully becomes more succinct.

{% codeblock lang:java %}
wrapAnyException(serviceCall(), with(CalendarException.class));
{% endcodeblock %}

  
This will wrap any exception and rethrow as a new `CalendarException` to
include as the cause any underlying exception. It uses reflection to create
the new exception, and forces the syntactically sugary `with` by taking a
`WithException` as the second parameter.

  
It's a candidate feature for tempus-fugit 1.1 for now, and will go in for sure
if it gets some millage. Let me know if you find it useful. Source is
[here](http://code.google.com/p/tempus-fugit/source/browse/trunk/tempus-fugit/src/main/java/com/google/code/tempusfugit/ExceptionWrapper.java) with
the test [here](http://code.google.com/p/tempus-fugit/source/browse/trunk/tempus-fugit/src/test/java/com/google/code/tempusfugit/ExceptionWrapperTest.java).




