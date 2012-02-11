---
name: generate-concordion-overviews
layout: post
title: Generate Concordion Overviews
time: 2010-07-07 22:01:00 +01:00
categories: java agile testing
comments: true
---

Creating customer authored acceptance tests is awesome! I love it. Getting your users to tell you exactly what they want (and don't want) in a form that they can (ghost) write can make for a world that even the Care Bears are jealous of.
  
I can't comment on some of the BDD targeting frameworks like
[JBehave](http://jbehave.org/), [EasyB](http://www.easyb.org/) or
[Cucumber](http://cukes.info/) but I do like using
[Concordion](http://www.concordion.org/). We try and use it in such as way to
fit in with a BDD approach, its flexible enough to use in almost any approach
in fact. That's probably why I like it so much. It's frequently cited closest
comparator is probably Fit but that's a little unfair. As I say, Concordion
tries really hard not to tie you into a particular approach, so to compare it
against Fit (which leans towards the inflexible in my view), doesn't serve as
a fair comparison.

  
Anyway, the point to this post isn't really to comment on Concordion but to
advertise a little Ant task I wrote to help auto-generate Concordion-friendly
summary pages for your existing Concordion tests.

<!-- more -->
  
It's purpose is to collect your Concordion tests as an "overview page" which
itself is a Concordion specification. You'd run just this specification and it
would in turn run all your tests, giving you a nice red / green overview. You
can fold it into your continuous itegration process (Ant or Maven) and publish
the overview and related specifications straight to some HTTP server for your
customers to review, per-build, 24/7. Nice.

  

Check out the [user manual](http://badrobot.googlecode.com/svn/trunk/bad.robot/concordion-ant-task/manual/Overview.html), written as Concordion
specifications and download the binaries from [Google Code](http://code.google.com/p/badrobot/downloads/list).

[](http://code.google.com/p/badrobot/wiki/ConcordionAntTask)

[{% img http://4.bp.blogspot.com/_-uMxV_fCbC4/TDTpijCjrxI/AAAAAAAAEoA/ZYmfILds2MY/s640/concordion.png %}](http://4.bp.blogspot.com/_-uMxV_fCbC4/TDTpijCjrxI/AAAAAAAAEoA/ZYmfILds2MY/s1600/concordion.png)

  
As a closing note, as I mentioned Concordion, its only fair to mention
[Xcordion](http://code.google.com/p/xcordion/) (and more recently Xcordion2)
which is essentially a fork of Concordion. The main difference being a
philosophical one. If Concordion constrains some activities within the
specification (mostly to encourage certain principles), Xcordion is more of a
free for all. With great power comes great responsibility and all that. Whilst
Xcordion2 is being worked on, be prepared to build from source. You'll notice
a couple of features missing, at least in the short term.





