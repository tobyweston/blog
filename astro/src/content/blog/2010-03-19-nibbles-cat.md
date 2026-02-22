---
title: "Nibbles the Cat & Concurrency"
pubDate: "2010-03-19"
categories: 'java-concurrency'
keywords: "Java deadlock, deadlock detection, DeadlockDetector, tempus-fugit, thread management, example"
description: "A concrete deadlock example in Java showing how two threads can deadlock acquiring the same locks in opposite orders. Demonstrates DeadlockDetector in action."
---

I recently introduced a deadlock into our performance monitoring. I inadvertently prevented a statistic collection daemon I wrote from shutting down thanks to some unlucky timing and a bad synchronisation policy. Because the synchronisation that was involved was distributed across a couple of classes (including some external classes) it wasn't obvious where they clashed. It got me thinking more about deadlocks and how many times we _actually _see them in real systems. In the end, I created a `DeadlockDetector` class.
  
I'm talking here about Java level deadlocks and to illustrate the point, poor old `Nibbles` got himself into quite a pickle. The situation is like this; `Nibbles` has been abducted and the `Kidnapper` and `Negotiator` threads have started a dialogue.

``` java
public void potentialDeadlock() {
     new Kidnapper().start();
     new Negotiator().start();
}
```

However, in the process of negotiation it becomes apparent that the  `Kidnapper` is unwilling to release poor `Nibbles` until he has received the `Cash` and the `Negotiator` is unwilling to part with the `Cash` until he has poor `Nibbles` back in his arms.

  
By synchronising on nibbles below, the  `Kidnapper` is holding onto him (more specifically his monitor) until the end of the synchronised block. However, within this block the  `Kidnapper` is trying to take the cash. The access to this method is itself synchronised on the cash, meaning that no one else can access the cash whilst the  `Kidnapper` is grabbing it. Meanwhile, the `Negotiator` is synchronising on the cash, holding onto it (or again, more specifically, it's monitor) until the end of the synchronised block then within that block, it requires nibbles. We can start to see the potential for deadlock.

``` java
public class Kidnapper extends Thread {
   public void run() {
      synchronized (nibbles) {
         synchronized (cash) {
            take(cash);
         }
      }
   }
}

public class Negotiator extends Thread {
   public void run() {
      synchronized (cash) {
         synchronized (nibbles) {
            take(nibbles);
         }
      }
   }
}
```

The deadlock detector displays this woeful situation as follows.

    Deadlock detected
    =================

    "Negotiator-Thread-1":
      waiting to lock Monitor of com.google.code.tempusfugit.concurrency.DeadlockDetectorTest$Cat@ce4a8a
      which is held by "Kidnapper-Thread-0"

    "Kidnapper-Thread-0":
      waiting to lock Monitor of com.google.code.tempusfugit.concurrency.DeadlockDetectorTest$Cash@7fc8b2
      which is held by "Negotiator-Thread-1"


  
If you fire up the example and point jconsole at it, you'll get similar results from the Thread tab. You can see how tempus-fugit tests the `DeadlockDetector` class [here](https://github.com/tobyweston/tempus-fugit/blob/master/src/test/java/com/google/code/tempusfugit/concurrency/DeadlockDetectorTest.java) and to find out more about see the project [documentation](http://tempusfugitlibrary.org/documentation/threading/deadlock/).

Oh and don't worry, `Nibbles` was released and the `Kidnapper` arrested in the end.





