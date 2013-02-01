---
name: loggin-is-still-evil-but
layout: post
title: Logging is still evil but...
time: 2011-06-22 21:14:00 +01:00
categories: java object-oriented mocking testing recipes
comments: true
sidebar : false
keywords: "logging, log4j, event driven vs logging, event driven"
description: "This post shows how to make assertions against Log4J and test your application's logging. If you can't avoid it, treat logging as a requirement and test against it."
---

In a [previous post]({{ root_url }}/blog/2010/10/18/logging-is-evil-but/), I was going on about how evil logging is. How it's often confused as a requirement and often badly misused. The upshot of the post was that if you're going to log stuff, in our case using Log4J, lets be honest about it and test it. We should be able to say upfront what's important to log, in what situations and at what log level. Sounds like a straight forward case of test first.
  
Mocking Log4J however can be a real pain. I've managed it in the past using Apache's logging abstraction and configuring it to use Log4J under the covers but in my previous post, I demonstrated a slightly easier way. A helper class called Log4J that we can use to represent the logging system and that we can make assertions against. Pretty cool so far.

<!-- more -->
  
There was one caveat, I wasn't entirely happy with the fact that the class would rely on your external Log4J configuration. To assert that a log message appeared at the level INFO for example, you'd have to make sure that the test environment sets up the appropriate class to log at that level. It made for a kind of integration / environmental test which in some cases might be a sensible test but for the most part, I kept seeing test failures down to configuration on different environments. Yuk.

  
So I updated the helper class to include a log level override which will ignore what the actual configuration says. This means you can write less brittle tests to say things like "ensure my log message is output at debug level regardless of the runtime configuration".

  
The updated class looks like this.

{% codeblock lang:java %}
public class Log4J {

    private final StringWriter writer = new StringWriter();
    private final Logger logger;
    private final String uuid = UUID.randomUUID().toString();

    public static Log4J appendTo(Logger logger) {
        return new Log4J(logger, ALL);
    }

    public static Log4J appendTo(Logger logger, Level level) {
        return new Log4J(logger, level);
    }

    private Log4J(Logger logger, Level level) {
        this.logger = logger;
        WriterAppender appender = new WriterAppender(new SimpleLayout(), writer);
        appender.setName(uuid);
        logger.addAppender(appender);
        logger.setLevel(level);
    }

    public void clean() {
        logger.removeAppender(uuid);
    }

    public void assertThat(Matcher<String> matcher) {
        org.junit.Assert.assertThat(writer.toString(), matcher);
    }
}
{% endcodeblock %}

  
Which means you can setup to expect a log level at say the ERROR level like this.

  
{% codeblock lang:java %}
private final Log4J logger = Log4J.appendTo(Logger.getLogger(Post.class), LogLevel.ERROR);
{% endcodeblock %}
  
The make assertions like this (which would fail if the matcher fails or because its not logged at the expected level.

{% codeblock lang:java %}
logger.assertThat(containsString(EXCEPTION_MESSAGE));
{% endcodeblock %}

I still think logging is evil and try _really_ hard not to use a single log statement but if you have to, I hope the helper class helps keep you honest in your tests ;) Have a look at the [previous post]({{ root_url }}/blog/2010/10/18/logging-is-evil-but/) for more details and extended examples.

