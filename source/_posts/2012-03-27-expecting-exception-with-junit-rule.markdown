---
name: expecting-exception-with-junit-rule
layout: post
title: Expecting Exceptions JUnit Rule
time: 2012-03-27 06:00:00 +00:00
categories: java testing exceptions
comments: true
---

To make an assertion that an exception was thrown with JUnit, it's fairly common to use the try/fail/catch idiom or
the `expected` element of the `@Test` annotation. Despite being more concise than the alternative,
there is an argument that using `expected` doesn't support all the cases you may want to test. The examples being
to perform additional testing after the exception or testing against the actual exception message. 

JUnit 4.7 introduces the next progression, a `@Rule` that offers the best of both worlds. This articles weighs up the pros and cons of each approach and takes a closer look at the syntax of each.

<!-- more -->

## The try/fail/catch Idiom

The typical pattern is to catch an exception or fail explicitly if it was never thrown.

{% codeblock lang:java %}
@Test
public void example1() {
    try {
        find("something");
        fail();
    } catch (NotFoundException e) {
        assertThat(e.getMessage(), containsString("could not find something"));
    }
    // ... could have more assertions here
}
{% endcodeblock %}


which would highlight a failure in the following way.	
	
	java.lang.AssertionError: expected an exception
		at org.junit.Assert.fail(Assert.java:91)
		at bad.roboot.example.ExceptionTest.example1(ExceptionTest.java:20)
		...
	
The idiom has potential advantages in that it offers the opportunity to assert against the actual exception as well as performing additional work after the expectation. Aside from the noise, the major drawback however is that its very easy to forget to include the `fail` call. If genuinely doing test first, where we always run the test red, this wouldn't be a problem but all too often things slip through the net. In practice, I've seen far too many examples with a missing `fail` giving false positives.

## @Test (expected = Exception.class)

Using the `expected` element, we can rewrite the test as follows.

{% codeblock lang:java %}
@Test (expected = NotFoundException.class)
public void example2() throws NotFoundException {
    find("something");
    // ... this line will never be reached when the test is passing
}
{% endcodeblock %}

which will result in the following failure.	
	
	java.lang.AssertionError: Expected exception: bad.robot.example.NotFoundException

Much more concise, we've done away with all the noise at the cost of not being able to assert against the exception
message. We've also lost the ability to make more assertions after `find`. However, you might decide that smaller focused tests are in fact a good thing. Using this syntax, we're lead into writing a test focused on just one thing; that an exception is thrown when we call `find`. 

The test feedback has also become clearer.
	
## ExpectedException Rule

Using an instance of `ExpectedException`, we define a [JUnit rule](http://www.infoq.com/news/2009/07/junit-4.7-rules)
that allows us to setup expectations that are checked after the test concludes. It has a similar feel to
setting up expectations in mocking frameworks like [JMock](http://www.jmock.org).

{% codeblock lang:java %}
@Rule public ExpectedException exception = ExpectedException.none();

@Test
public void example3() throws NotFoundException {
    exception.expect(NotFoundException.class);
    exception.expectMessage(containsString("exception message"));
    find("something");
    // ... this line will never be reached when the test is passing
}
{% endcodeblock %}

Which would show the failure below.

	java.lang.AssertionError: Expected test to throw (exception with message a string containing "exception message" and an instance of bad.robot.example.NotFoundException)
		at org.junit.rules.ExpectedException$ExpectedExceptionStatement.evaluate(ExpectedException.java:118)
		...
	
The rule allows us to assert the exception is thrown and make assertions against the message. We still can't make
additional assertions after the `find` method call, but this may not be a bad thing.
	
Beware though that if you combine the rule with certain `@RunWith` classes,
you may get a false positive. Specifically, if you were to run with a class that extends `JUnit4ClassRunner` in the
above example, the test would no longer fail. You'd get a false positive.

For example, if you're using an old version of JMock and use `@RunWith(JMock.class)` you may see this. Older versions of the `JMock.class` extend `JUnit4ClassRunner`. `JUnit4ClassRunner` ignores rules whereas the newer `BlockJUnit4ClassRunner` supports rules and newer versions of `JMock.class` extends this runner.


## Summary

The new rule offers a balance between concise syntax and function. In practice though if you're not interested in asserting against the exception's message, the `expected` element offers the most straight forward syntax. In the next article [Exception Handling as a System Wide Concern]({{ root_url }}/blog/2012/03/28/exception-handling-as-a-system-wide-concern/), I describe a general exception handling approach which negates the need to assert against exception messages.

The `ExpectedException` rule comes with its own baggage. The declarative nature of the rule means _magic_ just happens and so there is a new kind of "noise" to cope with in the test. You may or may not be comfortable with this.

I'd love to hear which approach you prefer, so feel free to post a comment below.
