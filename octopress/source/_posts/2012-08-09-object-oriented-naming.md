---
layout: post
title: "Object Oriented Naming"
pubDate: 2012-08-09 09:25
comments: true
categories: java, object-oriented
sidebar: false
published: false
keywords: "java, object-oriented, variable naming"
description: ""
---

``` java
public interface TemplateProcessor {
    String process(Map<String, ?> context, String templateName);
}
```

Implemented using FreeMarker

``` java
public class FreemarkerTemplateProcessor implements TemplateProcessor {

}
```

When we use the templating engine, we're left in a quandary over what to call the instance of the `TemplateProcesspr`. We're calling it `templateProcessor` below but that's a terrible name. We know what the thing _is_, the type tells us that. We're clearly not representing what the thing _represents_ in an abstract sense.

``` java
public class ExampleClient {

	private TemplateProcessor templateProcessor;

	public ExampleClient(TemplateProcessor templateProcessor) {
		this.templateProcessor = templateProcessor;
	}
	
	public void example() {
		tempalteProcesser.process(data, "template.ftl");
	}
}

But what is a better name for the variable? `template`? `freemarker`? Both are better in the sense that the variable name represents what the thing actually represents not what it is. `tempalte` hints at something more as the second parameter is the actual "tempalte". `freemarker` isn't great becuase the `TemplateProcessor` could be anything, we could swap it out for Velocity for example.



Another (fairly contrived) example I like to use in the `User` class.  

``` java
User user = new User("dave");
```

Why not represent what the user object represents, not what it is.

``` java
User dave = new User("dave");
```

This instance of `User` _is_ actually `dave`, a concrete person; an instance of a `Human`.