---
name: type-safe-annotation
layout: post
title: Type Safe Annotation
time: 2010-01-04 20:51:00 +00:00
categories: java concurrency tempus-fugit
comments: true
sidebar : false
---

A new year and another Java gripe! This time its annotations and the lack of anything useful by way of parameters. Implementing the Goetz annotations from [Concurrency In Practice](http://www.amazon.co.uk/Java-Concurrency-Practice-Brian-Goetz/dp/0321349601?ie=UTF8&tag=diyfiesta&link_code=btl&camp=213689&creative=392969), I wanted to include an enum as a parameter type. Kind of like this

{% codeblock lang:java %}
public @interface GuardedBy {
   Type value();

   public enum Type { FIELD, CLASS; }
}
{% endcodeblock %}


So far so good. I then wanted to somehow parameterise the enum constants themselves to give extra information.

{% codeblock lang:java %}
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
{% endcodeblock %}

  
Now, here's where the trouble began.

<!-- more -->

Using the static constructor method is
fine when I want to create an instance of a Type but not when I want to
annotate some method. For example,

    
{% codeblock lang:java %}
@GuardedBy(GuardedBy.Type.CLASS("more info")) // javac cries
public void foo() {
   GuardedBy.Type type = GuardedBy.Type.CLASS("more info"); // fine
}
{% endcodeblock %}

  
The compiler very quickly complains that the attribute value must be constant.
Specifically,

    
    an enum annotation value must be an enum constant

  
To get round things, you can just create several attributes for the
annotation. Rather than have a nice `CLASS` type which can optionally have a
description, I was forced to have one attribute of type and another to capture
the additional information. grrrr.

    
{% codeblock lang:java %}
public @interface GuardedBy {
   Type value();
   String details() default "";

   public enum Type { CLASS, FIELD; }
}
{% endcodeblock %}

  
Shame on you Java for leading me on a merry dance! I'd love to know more about
why things are like this, so if you've got any more details, feel free to post
a comment.

  



