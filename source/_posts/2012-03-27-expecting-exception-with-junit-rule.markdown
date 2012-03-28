---
name: expecting-exception-with-junit-rule
layout: post
title: Expecting Exceptions with a JUnit Rule
time: 2012-03-27 06:00:00 +00:00
categories: java 
comments: true
---

To make an assertion that an exception was thrown with JUnit, it's fairly common to use the try/fail/catch idom or the `expected` element of the `@Test` annotation. Dispite being more concise than the alternative, there is an argument that using `expected` doesn't support all the cases you may want to test. The examples being additional testing after an expected exception or testing the exception message. JUnit 4.7 introduces the next progression, a `@Rule` that offers the best of both worlds.

This articles wieghs up the pros and cons of each approach and takes a closer look at the syntax of each. 

<!-- more -->

## try/fail/catch

The typical pattern is to catch an exception or fail excplitily if it was never thrown. 

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

which will result in the following in the negative case.	
	
	java.lang.AssertionError: expected an exception
		at org.junit.Assert.fail(Assert.java:91)
		at bad.roboot.example.ExceptionTest.example1(ExceptionTest.java:20)
		...
	
The idiom has potential advantages in that it offers the oppertunity to assert against actual exception as well as performing additional work after the expectation. Aside from the noise, the major drawback however is that its very easy to forget to include the `fail` call. If genuienily doing test first, where we always run the test red, this wouldn't be a problem but all too often things slip through the net. In practice, I've seen far too many examples with a missing `fail` giving false positives.

## @Test (expected = NotFoundException.class)

Using the `expected` element, we can rewrite the test as follows.

    @Test (expected = NotFoundException.class)
    public void example2() throws NotFoundException {
        find("something");
		// ... this line will never be reached when the test is passing
    }

which will result in the following failure.	
	
	java.lang.AssertionError: Expected exception: bad.robot.example.NotFoundException

Much more concise, we've done away with all the noise at the price of not being able to assert against the exception. Do we care? We've also lost the ability to make more assertions after `find`. However, you might decide that smaller focused tests are infact a good thing. With this example, we're lead into writing a test focused on just one thing; that an exception is thrown when we call `find`.	
	
## @Rule public ExpectedException 

Using the `ExpectedException` we define a [JUnit rule](http://www.infoq.com/news/2009/07/junit-4.7-rules) we can setup an object with expectations which are asserted against after the test concludes. It has a similar feel to mocking with something like [JMock](http://www.jmock.org).

    @Rule public ExpectedException exception = ExpectedException.none();
    
    @Test
    public void example3() throws NotFoundException {
        exception.expect(NotFoundException.class);
        exception.expectMessage(containsString("exception message"));
        find("something");
		// ... this line will never be reached when the test is passing
    }

	java.lang.AssertionError: Expected test to throw (exception with message a string containing "exception message" and an instance of bad.robot.example.NotFoundException)
		at org.junit.rules.ExpectedException$ExpectedExceptionStatement.evaluate(ExpectedException.java:118)
		...
	
This allows us to assert on the expectation and the message of the exception. We still can't make additional assertions after the `find` call, but this may not be a bad thing. 	
	
Beware though that if you combine this with some `@RunWith` class annotations, you may get a false positive. Specifically, if you were to run with a class that extends `JUnit4ClassRunner` in the above example, the test would no longer fail. You'd get a false positive. 

For example, if you're using an old version of JMock, `@RunWith(JMock.class)` may exhibit this behaviour. Older versions of the `JMock.class` extend `JUnit4ClassRunner` which don't support rules whereas newer versions extend `BlockJUnit4ClassRunner` which does.


## Summary

The new rule offers a balance between concise syntax and function. In practice though if you're not interested in asserting against the exception's message, the `expected` element (in `example2`) offers the most straight forward solution. The rule comes with its own bagage. For the simple case `exception.expect(NotFoundException.class)`, the declarative nature of the rule means _magic_ just happens and there is new 'noise' in the test. You may or may not be comfortable with this.

In my next article [Never Assert Against Exception Messages], I describe a general exception handling approach which negates the need to assert against messages and so seemingly argues against using the new rule.
