---
name: setter-vs-constructor-injection
title: Setter vs Constructor Injection
pubDate: 2010-05-01 09:18:00 +01:00
categories: java
sidebar : false
description: "Setter vs constructor injection. Explore the options here."
keywords: "setter vs constructor injection, spring, setter, getter, constructor, java"
---

So what is the argument for / against? It can be a tough one to describe as I recently discovered.
  
You can say that constructor injection forces an object to have its __dependencies set explicitly__ and setter injection is __open to forgetfulness or misuse__ but how powerful an argument is that really? Surely the tests would catch it if you miss a set call? Constructor injection does say upfront "this is what I need", so there's no "first call this, then this and don't forget this" - its explicit and you don't need to know about the internals that setters expose. That's useful. But on the small, how complex do the combination of set calls get?

If you use your IDE effectively, __constructor injection will have better rafactoring support__. There's no way an IDE will interpret adding a field to mean calling setter for it. However, if add a constructor parameter, the IDE can push a default value out to all usages.
  
I don't think that a __large number of constructor arguments__ justifies defecting to the setter camp as the real smell here is often that the class is doing too much and/or has too many dependencies. It's often cited that the reason there are lots of setters is because of particular __dependency injection framework leads you__ in that direction but why compromise (I should probably say, _comply_) because you're _told_ to? What if that compromises other design goals?

  
How about the way the system would __grow using constructors vs setters__? I think this is where the real argument lies. You can move forward perfectly happily with either approach, content with the fact that dependencies are isolated. Testing becomes simpler, more focused on the objects under test and the earth continues to orbit the sun. Its only much later when the system is all but grown up that you can look back and reflect. Have setters contributed to creating a system that is assembled in a complex, disheveled way? Are you leaning on external (ahem, xml) configuration to manage this? Alternatively, has a constructor centric approach left you with a system with a more concise assembly strategy? Which has more noise? You tell me...

  



