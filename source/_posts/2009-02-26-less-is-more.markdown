---
name: less-is-more
layout: post
title: Less is More
time: 2009-02-26 19:20:00 +00:00
categories: java performance
comments: true
---

[Denton](https://twitter.com/#!/tarkaTheRotter) was trying to
convince me the other day that less is more when it comes to maximum heap size in Java. After I finally got the point, I was aghast! Shock, horror... creating threads in Java takes up non-VM managed memory!

> After running a few tests I confirmed that the lower the max heap size is,
the more threads I could create. I can easily get a OutOfMemoryError when
allocating memory for threads way before any real heap space is used.

The helpful message you'll get is.

  

    java.lang.OutOfMemoryError: unable to create new native thread

  

I ran a simple loop that would create dozy threads (they sleep a lot) and
watched how many threads could be created before the out of memory error
above. I repeated this after setting the maximum heap size. Check out the
results below, you can see that no real Java heap is used, still I get an out
of memory error and am limited on the number of threads I can create. As a
caveat, these results should in no way taken as representative on any other
environment than my laptop running Java 1.6. Your mileage may vary.

  

[{% img http://4.bp.blogspot.com/_-uMxV_fCbC4/SabxCtNlpUI/AAAAAAAADCM/er62bS1oW9Y/s400/64.PNG %}](http://4.bp.blogspot.com/_-uMxV_fCbC4/SabxCtNlpUI/AAAAAAAADCM/er62bS1oW9Y/s1600-h/64.PNG)

[{% img http://2.bp.blogspot.com/_-uMxV_fCbC4/SabxJsaTCWI/AAAAAAAADCU/WM7e4EBwsSU/s400/512.PNG %}](http://2.bp.blogspot.com/_-uMxV_fCbC4/SabxJsaTCWI/AAAAAAAADCU/WM7e4EBwsSU/s1600-h/512.PNG)

[{% img http://1.bp.blogspot.com/_-uMxV_fCbC4/SabxQc8DBkI/AAAAAAAADCc/-O6ApHci_q4/s400/1512.PNG %}](http://1.bp.blogspot.com/_-uMxV_fCbC4/SabxQc8DBkI/AAAAAAAADCc/-O6ApHci_q4/s1600-h/1512.PNG)

[{% img http://4.bp.blogspot.com/_-uMxV_fCbC4/Sab0EHyHXyI/AAAAAAAADCk/6ur4CTR3svI/s400/results.PNG %}](http://4.bp.blogspot.com/_-uMxV_fCbC4/Sab0EHyHXyI/AAAAAAAADCk/6ur4CTR3svI/s1600-h/results.PNG)


I'd always considered OS native threads or light weight processes to be
effectively unbounded with the restrictions being on the resources they are
associated with. I don't think this is really the case though as clearly, the
act of creating a thread that does nothing and has no real resources
associated with it (other than any native voodoo) requires OS memory
allocation in my tests.


I thought this was really interesting as it demonstrates how small decisions
can have a big impact on the run-time characteristics of a system. Being able
to tune your application to suit your production requirements is always
tricky. Large memory models and data manipulation can often require large heap
sizes but if in addition, you then want to create large numbers of threads,
you might get into the murky world I've touched on here. Of course, thread
pools are generally the way to go if you want to manage your resources
properly, but that's another story all together.

  
I'm sure Google can tell you more, but see this [random blog](http://www.egilh.com/blog/archive/2006/06/09/2811.aspx) for another
description.




