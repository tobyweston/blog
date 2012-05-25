---
name: swt-applications-on-mac-os-x
layout: post
title: SWT Applications on Mac OS X
time: 2008-12-29 12:03:00 +00:00
categories: java
comments: true
sidebar : false
---

I've had a couple of problems running SWT applications on Mac, in particular, getting balloon tool tips to appear and incorrect invalid thread access errors. It seems that the Mac specific VM option `-XstartOnFirstThread` is the cure to what ails ya! It even addresses the bug I reported [here](https://bugs.eclipse.org/bugs/show_bug.cgi?id=247218)!
  
It seems that by default, Java will not start on the main thread.
Cocoa/Carbon/[insert mac vodoo here] starts it all and as a consequence, the
SWT UI thread might get associated with it and not your main application
thread. Therefore, whenever the application tries to access it (even though it
looks like it owns it in your code), it may not and invalid thread access
hilarity will ensue.

  
The flip side to this is that AWT/Swing apps and plugins might have problems.

