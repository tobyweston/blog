---
title: "Type Safe Annotation'"
pubDate: "2010-01-04'"
categories: 'java concurrency tempus-fugit'
keywords: "java, annotation, goetz, enum annotation must be an enum constant"
description: "Why does Java insist that an enum annotation value must be an enum constant?"
---

<div>
    <script type="text/javascript">
    function trackOutboundLink(link, category, action) {

        try {
            _gaq.push(['_trackEvent', category , action]);
        } catch(err){}

        setTimeout(function() {
            document.location.href = link.href;
        }, 100);
    }
    </script>
</div>

A new year and another Java gripe! This time its annotations and the lack of anything useful by way of parameters. Implementing the Goetz annotations from <a href="http://amzn.to/TtEnWO" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">Concurrency In Practice</a>, I wanted to include an enum as a parameter type. Kind of like this

``` java
public @interface GuardedBy {
   Type value();

   public enum Type { FIELD, CLASS; }
}
```
<!-- more -->

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

  



