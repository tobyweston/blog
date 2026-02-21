---
title: "Wrapping Exceptions is Dull"
pubDate: "2010-04-25"
categories: 'java tempus-fugit exceptions recipes'
keywords: "Java exception wrapping, checked exceptions, runtime exceptions, tempus-fugit, boilerplate, auto-wrap"
description: "Wrapping checked exceptions to rethrow as RuntimeExceptions is verbose boilerplate. Use tempus-fugit's Exceptions helper to wrap them automatically."
---

I'm totally bored of wrapping exceptions in Java,
  
```
try {
   // do something
} catch (BoredomException e) {
   // do something else
}
```
It's verbose, ugly and has nothing to do with what you're really trying to convey. It's just noise. For example, when using the _dreadful_ Google Data API to access my calendar, I wrapped a couple of underlying Google services to be able to mock. Each service wanted to throw a bunch of Google specific exceptions which I wanted to rethrow as application specific exceptions.

``` java
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
```

  
If I didn't delegate like this, every internal call would have to wrap and handle the google exceptions rather than my application specific one. There's no class hierarchy in Google's API here.

As I've done this a few times, I decided to add it to [tempus-fugit](http://tempusfugitlibrary.org/) as a `ExceptionWrapper` class. Using this class, you can wrap a `Callable` to rethrow any caught exception as some other (including the underlying exception as the `cause`).

  
So, in a similar way to the above, the client can ignore any declared
exceptions and just rethrow them in-line. For example,

``` java
wrapAnyException(new Callable<Object>() {
    @Override
    public Object call() throws ServiceException {
         // nasty code throwing a bunch of exceptions
    }
}, with(CalendarException.class));
```
when this is in-lined further, it hopefully becomes more succinct.

``` java
wrapAnyException(serviceCall(), with(CalendarException.class));
```
  
This will wrap any exception and rethrow as a new `CalendarException` to include as the cause any underlying exception. It uses reflection to create the new exception, and forces the syntactically sugary `with` by taking a `WithException` as the second parameter.

  
It's in [tempus-fugit](http://tempusfugitlibrary.org/), let me know if you find it useful.



