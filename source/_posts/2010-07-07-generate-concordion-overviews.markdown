---
name: generate-concordion-overviews
layout: post
title: Generate Concordion Overviews
time: 2010-07-07 22:01:00 +01:00
categories: java agile testing
comments: true
---

Customer authored acceptance tests are great. Getting your users to tell you exactly what they want
and don't want in the form of a _specification_ can be liberating. You'll thrash out the details and come up
 with _examples_ that can be exercised against the running system. Everybody wins.

I can't really comment on some of the BDD targeting frameworks like [JBehave](http://jbehave.org/),
[EasyB](http://www.easyb.org/) or [Cucumber](http://cukes.info/) but I do like using [Concordion](http://www.concordion.org/).
We try and use it in such as way to fit in with a BDD approach, it's actually flexible enough to use with almost any
approach.

It's frequently cited closest comparator is probably Fit but that's a little unfair. As I say, Concordion tries really
hard not to tie you into a particular approach, whereas Fit invariably leads you down a certain route. So to compare it
against the less flexible Fit, isn't really accurate.
  
Anyway, the point to this post isn't really to comment on Concordion but to advertise a little Ant task I wrote to
help auto-generate Concordion-friendly summary pages for your existing Concordion tests.

<!-- more -->
  
It's purpose is to collect your Concordion tests as an "overview page" which
itself is a Concordion specification. You'd run _just_ this specification as part of your build and it'll run all your
tests, generating a nice red / green overview page. You can fold it into your continuous integration process (Ant or
Maven) and publish the overview and related specifications straight to some HTTP server for your customers to review, every build, 24/7. Nice.


Check out the [user manual](http://badrobot.googlecode.com/svn/trunk/bad.robot/concordion-ant-task/manual/Overview.html), written as Concordion
specifications and download the binaries from the [bad.robot.repo repository](http://robotooling.com/maven/bad/robot/concordion-ant-task/).

[{% img ../../../../../images/concordion-ant-manual.png %}](http://badrobot.googlecode.com/svn/trunk/bad.robot/concordion-ant-task/manual/Overview.html)

  
As I mentioned Concordion, its only fair to mention
[Xcordion](http://code.google.com/p/xcordion/) (and more recently Xcordion2)
which is essentially a fork of Concordion. The main difference being a
philosophical one. If Concordion constrains some activities within the
specification (mostly to encourage certain principles), Xcordion is more of a
free for all. With great power comes great responsibility and all that. Whilst
Xcordion2 is being worked on, be prepared to build from source. You'll notice
a couple of features missing, at least in the short term.





