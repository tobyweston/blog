---
name: setter-vs-constructor-injection
layout: post
title: Setter vs Constructor Injection
time: 2010-05-01 09:18:00 +01:00
categories: java
comments: true
sidebar : false
---

So what is the argument for / against? It can be a tough one to describe as I recently discovered.
  
You can say that constructor injection forces an object to have its
dependencies set explicitly and setter injection is open to forgetfulness but
how powerful an argument is that really? Surely the tests would catch it if
you miss a set call? Constructor injection does say upfront "this is what I
need", so there's no "first call this, then this and don't forget this" - its
explicit and you don't need to know the internals that setters try and expose.
That's useful. But on the small, how complex do the combination of set calls
get?

  
I don't think that a large number of constructor arguments justifies defecting
to the setter camp as the real smell here is often that the class is doing too
much and/or has too many dependencies. It's often cited that the reason
there are lots of setters is because of particular dependency injection
framework leads you in that direction but why compromise (I should probably
say, _comply_) because you're _told_ to?

  
How about the way the system would grow using constructors vs setters? I think
this is where the real argument lies. You can move forward perfectly happily
with either approach, content with the fact that dependencies are isolated.
Testing becomes simpler, more focused on the objects under test and the earth
continues to orbit the sun. Its only much later when the system is all but
grown up that you can look back and reflect. Have setters contributed to
creating a system that is assembled in a complex, disheveled way? Are you
leaning on external (ahem, xml) configuration to manage this? Alternatively,
has a constructor centric approach left you with a system with a more concise
assembly strategy? Which has more noise? You tell me...

  



