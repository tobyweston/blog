---
name: deprecated-annotation
layout: post
title: Deprecated Annotation
time: 2009-01-22 15:25:00 +00:00
categories: java
comments: true
sidebar : false
---

Why didn't Sun add a `value` property to the `@Deprecated` annotation? Instead of
  

    
{% codeblock lang:java %}
@Documented
@Retention(RetentionPolicy.RUNTIME)
public @interface Deprecated {
}
{% endcodeblock %}


which kind of implies we should do the following.


{% codeblock lang:java %}
@Deprecated
/** @deprecated use {@link Foo} instead */
public class GoneOff {
   // ...
}
{% endcodeblock %}


why can't we have


{% codeblock lang:java %}
@Documented
@Retention(RetentionPolicy.RUNTIME)
public @interface MyDeprecated{
   public abstract String value() default "";
}
{% endcodeblock %}


which means we can use


{% codeblock lang:java %}
@MyDeprecated("use Foo instead")
public class GoneOff {
   // ...
}
{% endcodeblock %}






