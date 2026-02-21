---
title: "JMock to Scalamock Cheat Sheet"
pubDate: '2015-05-09'
categories: 'scala testing'
keywords: "JMock, Scalamock, Scala, mocking, Specs2, cheat sheet, test doubles, mock objects"
description: "Quick reference cheat sheet mapping JMock idioms to their Scalamock equivalents. Useful when migrating Java tests to Scala or learning Scalamock."
---

An abbreviated set of JMock examples with their Scalamock equivalents.


## Mock Objects & the "Context"

```java
private final Mockery context = new JUnit4Mockery();

private final ScheduledExecutorService executor = context.mock(ScheduledExecutorService.class);
private final ScheduledFuture future = context.mock(ScheduledFuture.class);
```

```java
"A test with a mock context in scope" in new MockContext {
  val executor = mock[ScheduledExecutorService]  
  val future = mock[ScheduledFuture[Any]]
  // ...
}
```

## Returns

```java 
// java
context.checking(new Expectations() {{ braces }}
    oneOf(executor).shutdownNow(); will(returnValue(asList(waiting)));
    oneOf(waiting).cancel(true);
}});
```
```scala
// scala
(executor.shutdownNow _).expects().returning(asList(waiting)).once
(waiting.cancel _).expects(true).once
```
**Notes:**  

 * `expects()` is required for zero argument method call expectations.  
 * You can leave off `once`; it will default to the same behaviour  


## Allowing / Ignoring

```java
// java
context.checking(new Expectations() {{ braces }}
    allowing(executor).scheduleWithFixedDelay(with(any(Runnable.class)), with(any(Long.class)), with(any(Long.class)), with(any(TimeUnit.class))); will(returnValue(future));
    oneOf(future).cancel(true);
}});
```
```scala
// scala
(executor.scheduleWithFixedDelay _).expects(*, *, * , *).returning(future)
(future.cancel _).expects(true).once
```
**Notes:**  

* You could also add `.anyNumberOfTimes` after the `returning` call but it's unnecessary.  
* There's no way to distinguish the _intention_ of allowing and ignoring interactions in Scalamock.  
 

## Default Values

JMock will return a default value (as a dynamic proxy) if you set up an expectation but leave off a `returnValue`. In the example below, we don't care if it returns anything so if the code under test relies on a value, but the test does not, we don't have to express anything in the test.

```java
oneOf(factory).create();
```
If the underlying code were to check, say, that the result of `factory.create()` was not an empty list with `if (result.isEmpty())`, JMock would return something sensible and we'd avoid a `NullPointerException`. You might argue that this side affect should be captured in a test but leaving it off makes the intention of expectation clearer; we only care that `create` is called, not what it returns.

Scalamock will return `null` by default. So the above example would give a `NullPointerException` and you're required to do something like this. Notice we're using a `stub` and not a `mock` here.

```scala
val result = stub[Result]
(factory.create _).expects().once.returning(List(result))

```
## Any / Wildcards

JMock uses `with` and Hamcrest the matcher `IsAnything` (`any`) to match anything. The type is used by the compiler.

```java
context.checking(new Expectations() {{ braces }}
    ignoring(factory).notifyObservers(with(any(SomeException.class)));
    oneOf(factory).notifyObservers(with(any(AnotherException.class)));
}}
```
In the Scala version, use a [type ascription](http://docs.scala-lang.org/style/types.html#ascription) to give the compiler a hand in the partially applied method call;

```scala
(factory.notifyObservers(_: SomeException)).expects(*).anyNumberOfTimes
(factory.notifyObservers(_: SomeException)).expects(*).once
```
**Notes:**  

* `AnotherException` is a subtype of `SomeException` but `any` will match on literally anything. Using subtypes like this in JMock is a bit of a smell as a test won't fail if a different subtype is thrown at runtime. It may be useful to express intent.  
* [You can't replicate the subtype line](http://stackoverflow.com/questions/30162263/scalamock-wildcard-argument-match-on-subtype) in Scalamock; (`(factory.notifyObservers(_: AnotherException))` doesn't compile.  


 
## Throwing Exceptions

```java
final Exception exception = new RuntimeException();
context.checking(new Expectations() {{ braces }}
    oneOf(factory).create(); will(throwException(exception));
    oneOf(factory).notifyObservers(exception);
}});
```
```scala
val exception = new Exception
(factory.create _).expects().throws(exception).once
(factory.notifyObservers(_: Exception)).expects(exception).once
```

**Notes:** 

 * In Scalamock, `throws` and `throwing` are interchangeable.
 * Again, `once` is optional.