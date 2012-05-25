---
name: running-junit-tests-in-parallel
layout: post
title: Running JUnit tests in parallel
time: 2009-12-29 19:03:00 +00:00
categories: java concurrency tempus-fugit
comments: true
sidebar : false
---

I've been playing with running tests in their own threads for a while now (in particular with reference to [GUI testing]({{ root_url }}/blog/2008/12/30/be-explicit-about-ui-thread-in-swt/)) and am settling on a warm fuzzy feeling towards my general approach. I'm trying to capture this warm feeling more explicitly in the [tempus-fugit](http://code.google.com/p/tempus-fugit/) project and today I was working on running tests in parallel with JUnit.
  
Looking more into recent versions of JUnit, there seems to be lots and lots of
integration points for you to play with. I've been playing with `Rules`,
`Statements` and `Runners` mostly and when creating your own
`BlockJUnit4ClassRunner`, I spotted you can override the scheduler which, er,
schedules the actual test methods to be run.

  
After experimenting with much less straight forward integrations, overriding
the scheduler gave the following.

{% codeblock lang:java %}
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
{% endcodeblock %}


This results in all the test methods within a given class running in parallel.
I'm excited about speeding up the execution time of my tests, next step would
be run all tests across classes in parallel! hmmm.

This is all available to use via the [tempus-fugit](http://code.google.com/p/tempus-fugit/) project by the way.
See the tempus-fugit [documentation](http://tempus-fugit.googlecode.com/svn/site/documentation/concurrency.html#Parallel_Tests)
for more details on the runner.


