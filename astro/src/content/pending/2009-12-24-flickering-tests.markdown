---
name: flickering-tests
layout: post
title: Flickering Tests and a JUnit Rule
pubDate: 2009-12-24 15:55:00 +00:00
categories: java concurrency tempus-fugit
comments: true
sidebar : false
keywords: "flickering tests, nondeterminism, intermittent tests, java, intermittent, junit"
description: "Repeat intermittently failing tests automatically with a JUnit rule."
---

Occasionally I'll see flickering tests. Sometimes they're green, sometimes they're red and this can happen without any code changes. What bugs me the most is that when trying to fix the problem, I can never be sure that I haven't just been lucky and the green I'm seeing isn't really a false positive. I'll have to manually run the test several times before my confidence grows.
  
In an attempt to ease the situation, I created an `@Intermittent` annotation with a corresponding JUnit `Rule` and `Runner`. Now, I can mark up a suspect test and get JUnit to do the repetition. Joy.


``` java
@Test
@Intermittent
public void flickering() {
   // ...
}
```
You can then use the `IntermittentRule` to run the test method repeatedly.

      
``` java
public class FlickeringTest {

    @Rule public IntermittentRule rule = new IntermittentRule();

    @Test
    @Intermittent
    public void flickering() {
        // ...
    }
}
```
Or use the `@RunWith` annotation to run the test using the `IntermittentTestRunner`.

``` java
@RunWith(IntermittentTestRunner.class)
public class FlickeringTest {

    @Rule public IntermittentRule rule = new IntermittentRule();

    @Test
    @Intermittent
    public void flickering() {
        // ...
    }
}
```
What's interesting here is the way in which the `Rule` and `Runner` interact with
JUnit. Newer versions of JUnit have introduced the idea of `Rule`s and
`Statement`s. Using a `Rule` allows access to the underlying `Statement` which in
our case is the action to run the test method. So we're able to run the
underlying statement again and again. Nice.

  
The `Runner` however can hook into JUnit's framework in a different way. It can
access more than one statement and so can position itself slightly differently.
What this means for us is that when using the `Rule` above, any `@Before` or `@After`
methods will only be run once but the test method will run multiple times.
Using the `Runner` above however, will run any `@Before` or `@After` methods
once for each test repetition.

  
The code is available as part of the [tempus-fugit](http://tempusfugitlibrary.org/) library, feel free to look around.



