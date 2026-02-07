---
title: "Atomiticy of the Thread class'"
pubDate: "2009-12-10'"
categories: 'java concurrency tempus-fugit'
keywords: "thread, interrupt status flag, interrupt, state, RUNNABLE, WAITING, TIMED_WAITING, TERMINATED"
description: "Java's Thread seems not to maintain it's state (RUNNABLE, WAITING etc) atomically with it's interrupt status flag"
---

I had an interesting time getting a couple of tests running for [tempus-fugit](http://tempusfugitlibrary.org/) recently. It threw up a couple of interesting aspects about using threads that I hadn't come across before.
  
In one particular test, I wanted to show that interrupt is called on a thread and so followed what's becoming a common pattern for me.

    
``` java
@Test
public void sleepInterrupted() throws Exception {
   Thread thread = threadSleepsForever();
   thread.start();
   waitForStartup(thread);
   thread.interrupt();
   waitForShutdown(thread);
   assertThat(thread.isInterrupted(), is(true));
}  ```
    

The alternative patten is to wait for the assertion and avoid the wait for shutdown method above. Either way, the test above is testing that the thread created has been interrupted by checking the interrupt flag.
  
The test was failing for me even though I was able to show that the interrupt is called and the interrupt flag is set immediately after the sleeping thread is woken. However, when the test reached the assertion, it was false. Weird.

<!-- more -->

I setup another thread to just poll the sleeping thread for its status and it showed the following.

    thread.isInterrupted() = false, thread.getState() = RUNNABLE  
    thread.isInterrupted() = false, thread.getState() = RUNNABLE  
    thread.isInterrupted() = false, thread.getState() = RUNNABLE  
    thread.isInterrupted() = false, thread.getState() = TIMED_WAITING  
    thread.isInterrupted() = true, thread.getState() = RUNNABLE  
    thread.isInterrupted() = false, thread.getState() TERMINATED  
    

So my thread was interrupted! It seems to say that when a thread terminates, it will reset the interrupt status flag. Looking at the source, it looks like Java maintains the flag at the native level and not as a member of the `Thread` class.


``` java
private native void interrupt0();
```

Looking at another run, I got the following

  
    thread.isInterrupted() = false, thread.getState() = RUNNABLE
    thread.isInterrupted() = false, thread.getState() = RUNNABLE  
    thread.isInterrupted() = false, thread.getState() = RUNNABLE  
    thread.isInterrupted() = false, thread.getState() = TIMED_WAITING  
    thread.isInterrupted() = true, thread.getState() = TIMED_WAITING  
    thread.isInterrupted() = false, thread.getState() = TERMINATED  
    

This is even more interesting as it would suggest that an interrupt doesn't update the thread's state and the interrupt flag atomically.

  

> It would seem thread termination will reset the interrupt status flag and
that an interrupt doesn't update the interrupt status flag and state
atomically.


As an couple of caveats to the type of test above where I want to check the interrupt status flag, its a good idea to avoid side affects by using the terribly named method `Thread.interrupted` rather than `isInterrupted`. I also had to use a stubbed thread to reliably tell if the interrupt was called.

  
See the code [here](https://github.com/tobyweston/tempus-fugit/blob/master/src/test/java/com/google/code/tempusfugit/concurrency/ThreadUtilsTest.java).
  



