---
name: swt-support-for-window-licker
title: SWT Support for Window Licker
pubDate: 2008-12-29 14:05:00 +00:00
categories: java
keywords: "SWT, WindowLicker, testing UI, swing/awt, webdriver"
description: "SWT Support for Window Licker, the rich UI testing, WebDriver-style framework"
---

[Window Licker](http://code.google.com/p/windowlicker/) is a framework designed to help you define your own API for GUI testing. It provides a driver style API that your Swing or Ajax applications plug into before you go about writing GUI tests in a language natural to your application.
  
We've been doing some driver based GUI testing for our web apps using [HtmlUnit](http://htmlunit.sourceforge.net/) so I was naturally interested in Window Licker with regard to rich client based testing. I've been trying to test my SWT based apps at the unit level as much as possible, but it's not always straight forward separating the behaviour of GUI classes from GUI elements. How do you test that all the validation behaviour is plumbed in correctly and fires at the right time in a text box? So, Window Licker seemed like a great candidate to getting some real user style testing. Great!

  
The bad news is that Window Licker doesn't yet support SWT. Boo! The good news is it gave me a great chance to have a go at implementing basic SWT support in Window Licker. Yey!

  
Check out the [patch](http://windowlicker-users.googlegroups.com/web/window-licker-swt-spike.patch) I wrote, or the [thread](http://groups.google.com/group/windowlicker-users/browse_thread/thread/6fb792261a9cd1e7) where it's discussed.
