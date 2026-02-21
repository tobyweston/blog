---
title: "SWTBot vs Window Licker"
subTitle: "A developer's comparison of rich client testing frameworks"
pubDate: "2009-03-15"
categories: 'java testing'
keywords: "swtbot, window licker, swtbot vs window licker, awt, swing, awt robot, selenium, rich clients"
description: "A comparison of SWTBot and Window Licker from a developer's perspective. Both are rich client testing frameworks used in a record/replay style but via a programmatic API. Think Selenium for desktop apps."
---

{% photo ../../../../../images/window-licker.png %}

The title is a bit misleading because these guys aren't really squaring off like Gozilla and Gigan, the projects aren't competing and this blog isn't really a full or fair comparison. For a start Window Licker doesn't yet support SWT and as its name suggests SWTBot does.
  
My comments are really based on having a go at [implementing some basic SWT support](http://groups.google.com/group/windowlicker-users/browse_thread/thread/6fb792261a9cd1e7) in Window Licker and adding some features to SWTBot so it shouldn't be taken as authoritative. This entry is more of an experience report after trying to contribute to both projects. I'll try to follow up with an API usage report when I've used both more with my applications.


## The Code

  
Window Licker supports Swing and Html (including Ajax) very elegantly and uses the Java [java.awt.robot](http://java.sun.com/j2se/1.4.2/docs/api/java/awt/Robot.html) package to take control of the mouse and keyboard and generate native events. SWTBot simulates events using manual notification. That is to say it calls the SWT widget `notifyListeners` method directly where as Window Licker fires native GUI events.

This wouldn't necessarily be much of a distinction but it does mean SWTBot doesn't always behave exactly as expected (for example, it doesn't handle text caret movement or clearing text fields). An application under test from Window Licker behaves much more like an application driven by a user whereas SWTBot doesn't always have to wait for visual ques to move along.

  
Window Licker feels like a more mature framework, its nicely componentised and test driven where as SWTBot seems more evolutionary and although there are plenty of nice abstractions in common with Window Licker, it is harder to test due to the lack interfaces/mocks. SWTBot's code base is sprawling and covers a lot of ground, Windows Licker feels more focused on the problem it tries to solve. Having said that, its much more straight forward contributing to SWTBot, I was able to contribute (and understand) more of the SWTBot code base upfront.

  
The other slight gripe I have with SWTBot is the project structure, its more suited to Eclipse than IntelliJ as its dependencies are provided via plugins rather than raw Jars. Window Licker comes with Eclipse and IntelliJ project files which is always nice. SWTBot also has several projects that make up the software, the build process isn't as obvious as others and it uses some generated code that you'll probably won't spot but still need to know about.
  

## The Project Hosting

  
SWTBot has recently moved to its new home on [Eclipse.org](http://www.eclipse.org/projects/project_summary.php?projectid=technology.swtbot) but the team lead hasn't deprecated the [old site](http://swtbot.sourceforge.net/index.html) and resources. Consequentially, it can be a bit confusing for a new user to follow when there are two subversion repositories, two sets of bug tracking instances, lots of mailings lists and so on. SWTBot has lots of broken links on the site.

Window Licker is much more low key, at the time of writing there is no pre-packaged release to download, it has a minimal site on [Google Code](http://code.google.com/p/windowlicker/) that invites you to just download the source and get stuck in. In lots of ways I prefer this approach.



## Conclusion

  
For me, SWTBot really lets itself down is how it's being run. We all realise that open source software often has to take a back seat to your day job but if you're going to release something open source and encourage participation (say by hosting it on Eclipse.org) you should really be able to take the helm and support your community. As such, I had a bit of a bad experience with SWTBot trying to get a feature committed. In short, I did a whole bunch of work after explicitly being asked to do so in order to get it committed, then when it was done, the team lead ignored it and committed a previous version I'd submitted. The previous version works fine, it did the job but i was asked to re-jig things to better fit in with the project's standards, yet it got dumped. See the [Bugzilla trail](https://bugs.eclipse.org/bugs/show_bug.cgi?id=259860#c28).

  
It's a shame because experiences like that just lower confidence in a project, I'm unlikely to want to push any changes back now. I guess though in summary, SWTBot's code was easier to contribute to (although I was working in one small area of a large project structure). Window Licker is probably the superior technically and in terms of code quality but was harder (for me) to work with. I was working on essentially cloning some of the core Licker functionality to work with SWT and found that I didn't fully understand all the abstractions and mechanisms. I suspect that in a pairing environment, it wouldn't be a problem but contributing via email and patches is unlikely to get the most out of collaboration.
