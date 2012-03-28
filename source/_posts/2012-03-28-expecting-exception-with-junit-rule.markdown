---
name: expecting-exception-with-junit-rule
layout: post
title: Expecting Exceptions with a JUnit Rule
time: 2012-01-29 13:58:00 +00:00
categories: java 
comments: true
---

When expecting a method to throw an exception we used to use the try/fail/catch idom in JUnit. With the advent of JUnit 4, we generally switched to using the `expected (NotFoundException.class)` method along with the `@Test` annotation. Dispite being more concise that the alternative, there is an argument that it doesn't cover all the cases you might want to test (the examples being additional testing after an expected exception or testing the exception details). JUnit 4.7 introduces the next progression, a `@Rule` that offers the best of both worlds.

This articles describes the new syntax and wieghs up the pros and cons of each approach. It also offers a general approach to exception handling that if followed, means that when testing for exceptions, you need never assert on the contents of the exception message...

<!-- more -->

## try/fail/catch

The typical pattern is the catch an exception or fail the test excplitily if it was never thrown. For example.

    @Test
    public void expectingExceptionExample1() {
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
		at bad.roboot.example.ExceptionTest.expectingExceptionExample1(ExceptionTest.java:20)
		...
	
This idiom has one potential advantage in that it offers the opertunity to assert on the actual exception and potentially perform additional work after the expectation. The drawback however is that its very easy to forget to include the `fail` call. If genuniely doing test first, where we always run the test red, this wouldn't be a problem but all too often things slip through the net. In practice, I've seen far too many examples with a missing `fail` giving false positives.

## @Test (expected = NotFoundException.class)

    @Test (expected = NotFoundException.class)
    public void expectingExceptionExample2() {
        find("something");
    }

	java.lang.AssertionError: Expected exception: bad.robot.example.NotFoundException

## @Rule public ExpectedException 

    @Rule public ExpectedException exception = ExpectedException.none();
    
    @Test
    public void expectingExceptionExample3() {
        exception.expect(NotFoundException.class);
        exception.expectMessage(containsString("expected an exception"));
        find("something");
    }

	java.lang.AssertionError: Expected test to throw (exception with message a string containing "expected an exception" and an instance of bad.robot.example.NotFoundException)
		at org.junit.rules.ExpectedException$ExpectedExceptionStatement.evaluate(ExpectedException.java:118)
		...
	
Beware thought that if you combine this with some `@RunWith` class annotations, you may get a false positive. Specifically, if you were to run with a `JUnit4ClassRunner` in the above example, the test would no longer fail. You'd get a false positive. 

Watch out for versions of older versions of JMock excibiting this behavour. Older versions of the JMock running extend `JUnit4ClassRunner` which would cause the problem using `@RunWith(JMock.class)`. Newer version extend `BlockJUnit4ClassRunner` which works fine.

If the class in question extends `JUnit4ClassRunner` rather than `BlockJUnit4ClassRunner`, JUnit will ignore the rule.

## General Approach

We shouldn't care about the exception message. There, I've said it.

