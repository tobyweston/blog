---
title: "Deprecated Annotation"
pubDate: "2009-01-22"
categories: 'java'
keywords: "Java, @Deprecated, annotation, Javadoc, API design, Sun, deprecation"
description: "Why didn't Sun add a value property to the @Deprecated annotation so you can describe what to use instead? A look at the annotation and its limitations."
---

Why didn't Sun add a `value` property to the `@Deprecated` annotation? Instead of
  

``` java
@Documented
@Retention(RetentionPolicy.RUNTIME)
public @interface Deprecated {
}
```

which kind of implies we should do the following.


``` java
@Deprecated
/** @deprecated use {@link Foo} instead */
public class GoneOff {
   // ...
}
```

why can't we have


``` java
@Documented
@Retention(RetentionPolicy.RUNTIME)
public @interface MyDeprecated{
   public abstract String value() default "";
}
```

which means we can use


``` java
@MyDeprecated("use Foo instead")
public class GoneOff {
   // ...
}
```





