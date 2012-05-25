---
name: junit-and-threaded-tests-i-recently
layout: post
title: JUnit and Threaded Tests
time: 2008-12-17 18:52:00 +00:00
categories: java concurrency testing
comments: true
sidebar : false
---

I recently noticed a bit of a problem when playing with threads within JUnit. Take the following snippet as an example;
  
{% codeblock lang:java %}
@Test
public void exaple() {
    Thread thread = new Thread(new Runnable() {
        @Override
        public void run() {
            System.out.println("hello");
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                Thread.interrupt();
            }
            System.out.println("bye");
        }
    });
    assertThat(thread.isDaemon(), is(NON_DAEMON));
    thread.start();
}
{% endcodeblock %}

Here, the string "bye" is never shown, it would seem that when the test method
finishes it somehow messes with the threads...

  
Looking into things, it seems in my case that naughty Eclipse is muddying the
water! The `RemoteTestRunner` class which Eclipse uses to run the tests ends up
calling `System.exit(0)` after it's run all the tests to kill the parent Java
process. Even if we changed the daemon status of the thread, you'd get the
same behaviour, ie, no "bye" being shown.

  
So, in some situations it is possible to interrupt a thread in a JUnit test
bypassing the interrupt mechanism when running a test from Eclipse. IntelliJ
actually seems to have the same behaviour but I can't review to source to
confirm.

  
[{% img http://lh6.ggpht.com/_-uMxV_fCbC4/SVInGoVdYJI/AAAAAAAAC08/I4RV1KzCyPo/gibble_22x22.png %}](http://lh6.ggpht.com/_-uMxV_fCbC4/SVInGoVdYJI/AAAAAAAAC08/I4RV1KzCyPo/gibble_22x22.png)


