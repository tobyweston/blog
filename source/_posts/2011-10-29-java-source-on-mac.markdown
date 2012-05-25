---
name: java-source-on-mac
layout: post
title: Java source on Mac
time: 2011-10-29 11:11:00 +01:00
categories: java
sidebar : false
---

Mostly as a reminder to myself, getting the Java source on your Mac involves the following.

<!-- more -->

  1. Go to the [Apple Developer Connection downloads page](https://developer.apple.com/downloads), search for **Java for Mac OS X 10.x Developer Package** where 10.x matches your version of OS X. The developer bundle includes the source whereas the regular software update version does not.
  1. Download and install. Running `/Applications/Utilities/Java Preferences.app` should now show "Java SE 6 (System)" in the list.
  1. Open a Terminal.app window
  1. `cd $JAVA_HOME` (aka `/System/Library/Frameworks/JavaVM.framework/Home`)
  1. Setup a symlink to the source archive with `sudo ln -s /Library/Java/JavaVirtualMachines/1.6.0_26-b03-383.jdk/Contents/Home/src.jar`
  1. And for the JavaDoc, `sudo ln -s /Library/Java/JavaVirtualMachines/1.6.0_24-b07-334.jdk/Contents/Home/docs.jar`
  1. Now point your IDE of choice to the new source folder symlink.
  
Any update to Java will set things up to point to Maven 3, so if you use Maven 2, it'll break things with


    java.lang.NoClassDefFoundError: org/codehaus/plexus/classworlds/launcher/Launcher


Reset things by;

  1. `cd /usr/share`  
  1. `sudo mv maven maven.new` (a symlink which should incorrectly be pointing to `java/maven-3.0.3)`
  1. `sudo ln -s /maven2/install/folder maven`
  1. run `maven -version` to check its back up.
  1. Have a cup of tea.
  





