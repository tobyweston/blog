---
name: unmarshalling
layout: post
title: Un/Marshalling
time: 2010-05-01 09:35:00 +01:00
categories: java
comments: true
sidebar : false
---

This post should probably be titled "Why I don't like Unmarhsalling frameworks". They just hack me off. I mean really,
who wants to have to use the Java objects that they make you use? It's not that they don't represent as objects the data that the frameworks unmarshall, they do. It's more that the underlying data may or may not match your systems view of the domain. I don't want to have to run some process to generate `Foo.java` only to convert it to `MyFoo.java`, I'd rather go straight to `MyFoo`.
  
I was using Castor to do the former some time ago. It sounded like a good
idea, and I got going really quickly. However, I quickly didn't like the
objects its produced so had to modify the `mapping.xml` to "tailor" the
marshalling. Still fine, this was ok for a while but soon enough I descended
into Castor mapping hell. I seriously spent days trying to tweak things and
had to compromise the model in the end.

  
After reflection, I thought I'd try and dump Castor. I replaced the
marshalling with merging to a template and produced cleaner XML in under an
hour. The unmarshalling, replaced with manually parsing the XML and inserting
elements directly into objects. I couldn't believe how much less pain I was
feeling!

  
For me, the overhead of maintaining these more "manual" approaches is far less
than working around any framework mismatches. If you're lucky enough to find
an marhsalling framework that can grow with you, fair play, but I'm heavily
biased towards a more manual approach these days. Down with [insert your
framework here].



