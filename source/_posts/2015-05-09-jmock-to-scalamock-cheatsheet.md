---
layout: post
title: "JMock to Scalamock Cheat Sheet"
date: 2015-05-09 12:41
comments: true
categories: scala java mocking testing
sidebar: false
published: false
keywords: "JMock, Scala, Scalamock, Specs2"
description: "JMock to Scalamock Cheat Sheet"
---

<!-- more -->

## Mock Objects & the "Context"

{% codeblock lang:java Mocks and Mockery: Java / JMock %}
private final Mockery context = new JUnit4Mockery();

private final ScheduledExecutorService executor = context.mock(ScheduledExecutorService.class);
private final ScheduledFuture future = context.mock(ScheduledFuture.class);
{% endcodeblock %}


{% codeblock lang:scala Mocks and Mockery: Scala / Scalamock & Specs2 %}
"A test with a mock context in scope" in new MockContext {
  val executor = mock[ScheduledExecutorService]  
  val future = mock[ScheduledFuture[Any]]
  // ...
}
{% endcodeblock %}

## Returns

{% codeblock lang:java Return a value: Java / JMock %}
context.checking(new Expectations() {{ braces }}
    oneOf(executor).shutdownNow(); will(returnValue(asList(waiting)));
    oneOf(waiting).cancel(true);
}});
{% endcodeblock %}

{% codeblock lang:scala Return a value: Scala / Scalamock %}
(executor.shutdownNow _).expects().returning(asList(waiting)).once
(waiting.cancel _).expects(true).once
{% endcodeblock %}

**Notes:**  
 * `expects()` is required for zero argument method call expectations.


## Allowing

{% codeblock lang:java Allowing: JMock / Java %}
context.checking(new Expectations() {{ braces }}
    allowing(executor).scheduleWithFixedDelay(with(any(Runnable.class)), with(any(Long.class)), with(any(Long.class)), with(any(TimeUnit.class))); will(returnValue(future));
    oneOf(future).cancel(true);
}});
{% endcodeblock %}

{% codeblock lang:scala Allowing: Scala / Scalamck %}
(executor.scheduleWithFixedDelay _).expects(*, *, * , *).returning(future)
(future.cancel _).expects(true).once
{% endcodeblock %}

**Notes:**  
 * You could also add `.anyNumberOfTimes` after the `returning` call but it's unnecessary. 