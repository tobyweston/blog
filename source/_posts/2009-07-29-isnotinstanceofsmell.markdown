---
name: isnotinstanceofsmell
layout: post
title: is(not(instanceOf(smell)));
time: 2009-07-29 19:17:00 +01:00
categories: java object-oriented
comments: true
---

For some reason, common perception is that using `instanceof` is a bit of smell. I think its fallen in with a bad
crowd and isn't really as bad as its cracked up to be. At the very least, we should consider _why_ its got a bad
reputation.
  
For example, given the following, what's clearer in the following exception
handling code?

      
{% codeblock lang:java %}
try {
    ...
} catch (InvocationTargetException e) {
    if (RuntimeException.class.isAssignableFrom(e.getCause().getClass())) {
        throw new ApplicationException(...);
    }
    throw e.getCause();
}
{% endcodeblock %}

or

{% codeblock lang:java %}
try {
    ...
} catch (InvocationTargetException e) {
    if (e.getCause() instanceof RuntimeException) {
        throw new ApplicationException(...)
    }
    throw e.getCause();
}
{% endcodeblock %}


<!-- more -->

There seems very little difference in the semantics of the two calls, both
handle class hierarchies and both handle interfaces. I think the legitimate
use for `Class.isAssignableFrom` is around scenarios where reflective-type
checks are more suited (for example, where the class to check against is only
known or may change at runtime). Using `Class.isInstance` is a similar
alternative. The other point that the [API documentation](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/Class.html#isAssignableFrom%28java.lang.Class)
points out is that `isAssignableFrom` works with primitives whereas `instanceof`
can not.

  
I wonder if the bad reputation `instanceof` suffers from is more due to often
being seen in the company of strange conditional logic than anything else. The
kind of stuff that seems to go against your Mumma's good advice. It may just
have fallen in with a bad crowd but is itself a good kid at heart...

  
I suspect `instanceof`, being around since forever, is seen as a bit antiquated
but given the example above using `Class.isAssignableFrom` seems to just
obfuscate things. The example needs to find out why a dynamic proxy throws an
exception and because the [InvocationTargetException](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/reflect/InvocationTargetException.html) wraps the
underlying cause, it kind of breaks checked exception handling and it feels
like we need to do some conditional check. If there is a smell here, that's
it. The above is trying to hide the symptom of the smell (`instanceof`) but the
smell is still there, its just harder to see. I often catch similar whiffs
when catching [ExecutionException](http://java.sun.com/j2se/1.5.0/docs/api/java/util/concurrent/ExecutionException.html).

  
More conventional cases where `instanceof` is a genuine smell may be around
conditional logic making decisions based on class type where using polymorphism
might be a neater solution. It's this kind of thing that your Mumma warned
you about and I suspect its this is the real smell that's rubbed off on poor
downtrodden `instanceof`.

{% img http://4.bp.blogspot.com/_-uMxV_fCbC4/SVInGoVdYJI/AAAAAAAAC08/I4RV1KzCyPo/s320/gibble_22x22.png %}


