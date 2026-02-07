---
title: "Less is More'"
pubDate: "2009-02-26'"
categories: 'java performance'
keywords: "OutOfMemory, threads, -Xmx, heap, number of threads, less heap, more threads, unable to create new native thread"
description: "Allocating less heap size to the JVM actually means you can create more native threads. "
---

[Dave Denton](https://twitter.com/#!/tarkaTheRotter) were chatting recently and he was trying to convince me that less is more when it comes to maximum heap size in Java. After I finally got the point, I was aghast! Shock, horror... creating threads in Java takes up non-VM managed memory!

> After running a few tests I confirmed that the lower the max heap size is, the more threads I could create. I can easily get a OutOfMemoryError when allocating memory for threads way before any real heap space is used.

The helpful message you'll get is.


    java.lang.OutOfMemoryError: unable to create new native thread

<!-- more -->

I ran a simple loop that would create threads that do nothing but sleep and watched how many could be created before the out of memory error above. I repeated this after setting the maximum heap size with `-Xmx`. Check out the results below, you can see that no real Java heap is used, still I get an out of memory error and am limited on the number of threads I can create. As a caveat, these results should in no way taken as representative on any other environment than my laptop running Java 1.6. Your mileage may vary.

  
{% gallery %}
../../../../../images/less-is-more/64.png: -Xmx 64m
../../../../../images/less-is-more/512.png: -Xmx 512m
../../../../../images/less-is-more/1512.png: -Xmx 1512m
{% endgallery %}

{% photo ../../../../../images/less-is-more/results.png default Heap size and the maximum number of threads created before failing %}


I'd always considered OS native threads or light weight processes to be effectively unbounded with the restrictions being on the resources they are associated with. This isn't the case though as clearly, the act of creating a thread that does nothing and has no real resources associated with it still requires OS memory allocation in my tests.


I thought this was really interesting as it demonstrates how small decisions can have a big impact on the run-time characteristics of a system. Being able to tune your application to suit your production requirements is always tricky. Large memory models and data manipulation can often require large heap sizes but if in addition, you want to create large numbers of threads, you might get into the murky world I've touched on here. Of course, thread pools are generally the way to go if you want to manage your resources properly, but that's another story all together.

  
I'm sure Google can tell you more, but see this [blog post](http://www.egilh.com/blog/archive/2006/06/09/2811.aspx) for another
description.




