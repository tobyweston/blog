---
name: be-more-expressive-with-builders
title: Be more Expressive with Builders
pubDate: 2009-01-06 17:07:00 +00:00
categories: java concurrency tempus-fugit
sidebar : false
keywords: "CountDownLatch, micro-DSL, DSL, builder pattern"
description: "Chain methods to create a micro-DSL and a more concise, human readable sequence of events in your code."
---

I came up with a neat little pattern that's helped me be more expressive in some (fairly specific) situations. Here I'll give you a feel for it using the `CountDownLatch` class as an example.
  

## CountDownLatch.await()

Using an instance of a `CountDownLatch`, we can wait for the latch to count down to zero, blocking the calling thread before continuing. When using a timeout, the method returns true if the count reached zero or false if the timeout expires. To make the timeout more explicit in my application code, I started with the following.

``` java
public void waitForStartup() throws InterruptedException, TimeoutException {
    if (!startup.await(5, SECONDS))
        throw new TimeoutException();
}

public void waitForShutdown() throws InterruptedException, TimeoutException {
    if (!shutdown.await(5, SECONDS))
        throw new TimeoutException();
}
```

## Using a Builder with Static Constructor

To be more concise, I wanted to wrap the logic above in some kind of helper class. Thanks to lovely static imports, a private constructor and a static factory method called `await()`, I was able to express the same thing with the following.

  
``` java
public void waitForStartup() throws InterruptedException, TimeoutException {
    await(startup).with(TIMEOUT);
}

public void waitForShutdown() throws InterruptedException, TimeoutException {
    await(shutdown).with(TIMEOUT);
}
```

The `with(...)` method is the thing that actually wraps the call to the `await()` method on the latch. I created a `Duration` class in the above case to capture the timeout constant.

  
This can be a neat little pattern which when used sparingly can lead to little nuggets of really readable code. However, the helper class that employs the static factory can feel unnatural as the method names don't really represent their function but **rather their context within the DSL that the class defines**.

Using a private constructor and verifying the internal state is essential to ensure that the DSL can't be used incorrectly. Basically, if there are very few methods and you make sure they can only be called in a sensible order, I'd suggest its a good pattern to follow. The finished class is shown below in full.

  
``` java
public class CountDownLatchWithTimeout {

    private final CountDownLatch latch;

    private CountDownLatchWithTimeout(CountDownLatch latch) {
        this.latch = latch;
    }

    public static CountDownLatchWithTimeout await(CountDownLatch latch) {
        return new CountDownLatchWithTimeout(latch);
    }

    public void with(Duration timeout) throws InterruptedException, TimeoutException {
        if (!latch.await(timeout.inMillis(), MILLISECONDS))
            throw new TimeoutException();
    }
}
```
  


