---
name: isnotinstanceofsmell
title: is(not(instanceOf(smell)));
pubDate: 2009-07-29 19:17:00 +01:00
categories: java object-oriented
keywords: "instanceof, smell"
description: "The instanceof operator in Java isn't always a bad thing"
---

For some reason, common perception is that using `instanceof` is a bit of smell. I think its fallen in with a bad crowd and isn't really as bad as its cracked up to be. At the very least, we should consider _why_ its got a bad reputation.
  
For example, given the following, what's clearer in the following exception handling code?

      
``` java
try {
    ...
} catch (InvocationTargetException e) {
    if (RuntimeException.class.isAssignableFrom(e.getCause().getClass())) {
        throw new ApplicationException(...);
    }
    throw e.getCause();
}
```
or

``` java
try {
    ...
} catch (InvocationTargetException e) {
    if (e.getCause() instanceof RuntimeException) {
        throw new ApplicationException(...)
    }
    throw e.getCause();
}
```

<!-- more -->

There seems very little difference in the semantics of the two calls, both handle class hierarchies and both handle interfaces. I think the legitimate use for `Class.isAssignableFrom` is around scenarios where reflective-type checks are more suited (for example, where the class to check against is only known or may change at runtime). Using `Class.isInstance` is a similar alternative. The other point that the [API documentation](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Class.html#isAssignableFrom%28java.lang.Class) points out is that `isAssignableFrom` works with primitives whereas `instanceof` can not.

I suspect `instanceof` is seen as a bit antiquated but given the example above using `Class.isAssignableFrom` seems to just obfuscate things. The example needs to find out why a dynamic proxy throws an exception and because the [InvocationTargetException](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/reflect/InvocationTargetException.html) wraps the underlying cause, it kind of breaks checked exception handling and it feels like we need to do some conditional check. If there is a smell here, that's it. The above is trying to hide the symptom of the smell (`instanceof`) but the smell is still there, its just harder to see. I often catch similar whiffs when catching [ExecutionException](http://java.sun.com/j2se/1.5.0/docs/api/java/util/concurrent/ExecutionException.html).
  
More conventional cases where `instanceof` is a genuine smell may be around conditional logic making decisions based on class type where using polymorphism might be a better solution.




