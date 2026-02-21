---
title: "Type Safe Annotation"
pubDate: "2010-01-04"
categories: 'java concurrency tempus-fugit'
keywords: "Java annotation, enum annotation, type safety, concurrency, @GuardedBy, Goetz, compile-time check"
description: "Java insists enum annotation values must be enum constants, preventing type-safe runtime checks. Explores why this is and what it means for concurrency annotations."
---

A new year and another Java gripe! This time its annotations and the lack of anything useful by way of parameters. Implementing the Goetz annotations from [Concurrency In Practice](http://amzn.to/TtEnWO), I wanted to include an enum as a parameter type. Kind of like this

``` java
public @interface GuardedBy {
   Type value();

   public enum Type { FIELD, CLASS; }
}
```

So far so good. I then wanted to somehow parameterise the enum constants themselves to give extra information.

``` java
public @interface GuardedBy {
   Type value();

   public enum Type {
      CLASS, FIELD;

      public static Type FIELD(String field) {
         return FIELD;
      }

      public static Type CLASS(String type) {
         return CLASS;
      }
   }
}
```
  
Here's where the trouble began.

Using the static constructor method is fine when I want to create an instance of a type but not when I want to annotate some method. For example,

    
``` java
@GuardedBy(GuardedBy.Type.CLASS("more info")) // javac cries
public void foo() {
   GuardedBy.Type type = GuardedBy.Type.CLASS("more info"); // fine
}
```
  
The compiler very quickly complains that the attribute value must be constant. Specifically,

    
    an enum annotation value must be an enum constant

  
To get round things, you can just create several attributes for the annotation. Rather than have a nice `CLASS` type which can optionally have a description, I was forced to have one attribute of type and another to capture the additional information.

    
``` java
public @interface GuardedBy {
   Type value();
   String details() default "";

   public enum Type { CLASS, FIELD; }
}
```
  
Shame on you Java! I'd love to know more about why things are like this, so if you can help, please post a comment.

  



