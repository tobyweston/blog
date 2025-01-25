---
name: running-junit-tests-in-parallel
layout: post
title: Running JUnit tests in parallel
pubDate: 2009-12-29 19:03:00 +00:00
categories: java concurrency tempus-fugit recipes
comments: true
sidebar : false
keywords: "testing, concurrency, parallel tests, run concurrently, multi threaded tests"
description: "Use JUnit to run tests in parallel."
---

I've been playing with running tests in their own threads for a while now (in particular with reference to [GUI testing](/blog/2008/12/30/be-explicit-about-ui-thread-in-swt/)) and am starting to feel comfortable with my approach. Today I was working on running tests in parallel with JUnit.

<!-- more -->

Looking more into recent versions of JUnit, there seems to be lots of integration points for you to play with. I've been playing with `Rules`, `Statements` and `Runners` mostly and when creating your own `BlockJUnit4ClassRunner`, I spotted you can override the scheduler which schedules the actual test methods to be run.


After experimenting with much less straight forward integrations, overriding the scheduler gave the following.

``` java
public class ConcurrentTestRunner extends BlockJUnit4ClassRunner {

    public ConcurrentTestRunner(Class type) throws Exception {
        super(type);
        setScheduler(new ConcurrentScheduler());
    }

    private static class ConcurrentScheduler implements RunnerScheduler {

        private ExecutorService executor;

        public ConcurrentScheduler() {
            executor = newCachedThreadPool(new ThreadFactory() { ... });
        }

        public void schedule(Runnable childStatement) {
            executor.submit(childStatement);
        }

        public void finished() {
            shutdown(executor).waitingForCompletion(seconds(10));
        }
    }
}
```

This results in all the test methods within a given class running in parallel. I'm excited about speeding up the execution time of my tests, next step would be run all tests across classes in parallel.

This is all available to use via the [tempus-fugit](http://tempusfugitlibrary.org/) project by the way.


