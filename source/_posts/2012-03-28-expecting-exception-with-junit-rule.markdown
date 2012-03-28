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

## @Test (expected = NotFoundException.class)

## @Rule public ExpectedException 

## General Approach

We shouldn't care about the exception message. There, I've said it.