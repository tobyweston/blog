---
title: "Catching Multiple Exceptions (and rethrowing them all!)"
pubDate: "2011-08-29"
categories: 'java exceptions recipes'
keywords: "rethrowing multiple exceptions, exception handling in java"
description: "Learn how to catch multiple exceptions, ignore and continue processing before finally retesting and rethrowing them all."
---

Sometimes, we may want to catch an exception, temporarily ignoring it to continue work before rethrowing it when its more appropriate to do so. I recently saw a slight variation of this whereby the developer wanted to (potentially) catch multiple exceptions, perform some processing then throw. However, it left the question that if more than one was caught, which exception should we actually rethrow. We certainly don't want to loose any information and should really allow the client to catch the exception in a standard way.

This got me thinking about how we should deal with this kind of thing. In the end, I came up with the idea of a collection class to capture the `Exceptions` and a sub-class of `Exception` to represent an exception containing other, embedded exceptions. When you're done collecting exceptions, you can just check and rethrow as a new exception type.

<!-- more -->
  
For example, the domain cleaning class below can throw an exception during the `deleteAll` method. Rather than abandon the cleanup of subsequent objects, we can employ this tactic to continue the cleanup and throw an exception containing the underlying problems when we're done.


``` java
public class DomainCleaner {

    public static void clean(Domain domain) throws CompositeException {
        Exceptions exceptions = new Exceptions();
        clean(domain.customers(), exceptions);
        clean(domain.suppliers(), exceptions);
        clean(domain.invoices(), exceptions);
        exceptions.checkAndThrow();
    }

    private static void clean(Repository repository, Exceptions exceptions) {
        try {
            ((TestRepository) repository).deleteAll();
        } catch (RepositoryException e) {
            exceptions.add(e);
        }
    }

}
```    

We simply add to the exception collection class (`exceptions.add(e)`) and then when we're done, we can check it and throw a composite exception if needed with `exceptions.checkAndThrow()`.

  
So far, we've only been interested in the fact that multiple exception can be handled and so haven't needed to programmatically query for specific exception types. For example, we've only needed this up until now.


``` java
try {
   // ... something that calls checkAndThrow()
} catch (CompositeException e) {
   // ... this is enough for now
}
```

The details of the classes are below.


``` java
public class Exceptions implements java.lang.Iterable<Exception> {

    private final List<Exception> exceptions = new ArrayList<Exception>();

    public void add(Exception exception) {
        exceptions.add(exception);
    }

    @Override
    public Iterator<Exception> iterator() {
        return exceptions.iterator();
    }

    public void checkAndThrow() throws CompositeException {
        if (!exceptions.isEmpty())
            throw new CompositeException(this);
    }
}
```
The `toString()` implementation below outputs the embedded exceptions in a way that is consistent with how you'd expect to see regular exceptions.

  
``` java
public class CompositeException extends Exception {

    private final Exceptions exceptions;

    public CompositeException(Exceptions exceptions) {
        super("composite exception was thrown with embedded exceptions (see details)");
        this.exceptions = exceptions;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (Exception exception : exceptions)
            builder.append('\t').append(new ExceptionToString(exception).toString()).append('\n');
        return String.format("%s\n{composite exceptions=\n%s}\n%s", this.getClass().getName(), builder.toString(), super.toString());
    }
}
```    
