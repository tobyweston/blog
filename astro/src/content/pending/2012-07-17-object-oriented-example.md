---
layout: post
title: "An Object Oriented Example"
pubDate: 2012-07-17 18:58
comments: true
categories: java object-oriented
sidebar: false
published: false
keywords: "OO, object-oriented, stop watch"
description: ""
---

When we model a domain, we often try and model the real world. Sometimes that's helpful, other times we work too hard to model ...


<!-- more -->

## Identifying the Object

Let's say we're interested in timing how long it takes to update to our stock levels within our system.

    public class BadlyImplementedTimedStockControlSystem implements StockControlSystem {   
        @Override
        public void update(StockLevel stock) {
            Date start = new Date();
            // do some processing
            Date end = new Date();
            Long took = end.getTime() - start.getTime();
        }
    }    

This works but violates the single responsibility principle; our `StockControlSystem` is now responsible for both updating stock levels and timing itself as it does so. If we try and seperate these responsbilities, we may decide that one belongs to a `StopWatch`. We've identified a new _role_.

A naive stop watch interface might look like the following.

	public interface StopWatch {
	    Date start();
	    Date stop();
	}

Which would leave the client to calculate the difference between start and stop time.	
	
or

	public interface StopWatch {
	    void start();
	    void stop();
	    Duration elapsedTime();
	}
	
	
What about looping whilst not timed out? eg to re-assess a timeout?

## Encapsulation?
	
It's a shame that we can actually get the elapsed time but lets go with it for now. Why do I say its a shame? Any kind of _getter_ like `elapsedTime` can (but not always) be a smell that some internal data has leaked from the object. In our case, the timing result is returned allowing clients to access it. This doesn't mean to say its breaking encapsulation or data hiding principles as there are lots of geuine reasons why clients may need access to it but lets make sure.

What are the kind of things a client might like to do with a timing result? It might want to work out if a timeout has been reached or perhaps calculate some average timings? For example, we may want to observe the time taken to make a request to update our stock control system;

    public class TimedStockControlSystem implements StockControlSystem {
        private final StopWatch timer = new ThreadLocalStopWatch();
        @Override
        public void update(StockLevel stock) {
            timer.start();
            // do some processing
            timer.stop();
            Duration time = timer.elapsedTime();
        }
    }
    
Extending this to allow the class to expire a timeout (lets say an alert should be made if things took too long).

    public class AlertOnLongRunningRequestsStockControlSystem implements StockControlSystem {
    
        private final StopWatch timer = new ThreadLocalStopWatch();
        private final Duration timeout = Duration.seconds(30);
    
        @Override
        public void update(StockLevel stock) {
            timer.start();
            // do some processing
            timer.stop();
            Duration time = timer.elapsedTime();
            if (time.greaterThan(timeout))
                alert();
        }
    }
    
but that means the `StockControlSystem` has to know about the `StopWatch`. It would be nicer to abstract this  
    
    public interface RequestObserver {
        Request started();
        public interface Request {
            Duration finished();
        }
    }

    
    public void updateStock(StockLevel stock) {
        RequestObserver timer = new RequestTimer(new ThreadLocalStopWatch(new RealClock()));
        Request request = timer.started();
        // do some processing
        Duration time = request.finished();
    }
    
    
In this next example, the `RequestObserver` has been implemented to record throughput of all the stock updates. It provides extra methods `getRequestsPerSecond` and `getTotalRequests`. 
    
    private static final RequestObserver timer = createThreadSafeThroughput();
    
    public void updateStock(StockLevel stock) {
        Request request = timer.started();
        // do some processing
        Duration time = request.finished();
    }

We're able to use this class without changing the `updateStock` method which is all well and good but how to we take advantage of these extra methods? We're treating this as any other `RequestObserver` which only returns the duration of a single call. The answer lies in what's going to want to use this extra information.

For example, the same instance used int he `StockControlSystem` could be registered with another component responsible for periodically monitoring or reporting on the throughput. JMX comes to mind here. 



   