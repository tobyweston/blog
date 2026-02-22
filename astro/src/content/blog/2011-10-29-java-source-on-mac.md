---
title: "Java source on Mac"
subTitle: "A quick guide to accessing Java source and Javadoc on macOS"
pubDate: "2011-10-29"
categories: 'tools'
keywords: "Java source code, Mac, Maven, M2_HOME, mvn, developer tools, IDE source attachment"
description: "How to get Java source code on your Mac for IDE source attachment. Covers Maven and environment configuration."
heroImage: "/images/heroes/mac-tools.jpg"
---

Mostly as a reminder to myself, getting the Java source on your Mac involves the following.


  1. Go to the [Apple Developer Connection downloads page](https://developer.apple.com/downloads).
  1. For Lion and above, search for **Java for Mac OS X (2006-2012) Developer Package**. The developer bundle includes the source whereas the regular software update version does not.
  1. For older versions (pre-Lion), search for **Java for Mac OS X 10.x Developer Package** where 10.x matches your version of OS X.
  1. Download and install.
  1. Open a Terminal.app window
  1. `cd $JAVA_HOME` (aka `/System/Library/Frameworks/JavaVM.framework/Home`)
  1. Setup a symlink to the source archive with `sudo ln -s /Library/Java/JavaVirtualMachines/1.6.0_26-b03-383.jdk/Contents/Home/src.jar`
  1. And for the JavaDoc, `sudo ln -s /Library/Java/JavaVirtualMachines/1.6.0_24-b07-334.jdk/Contents/Home/docs.jar`
  1. Now point your IDE of choice to the new source folder symlink.


## Maven

Any update to Java will set things up to point to Maven 3, so if you use Maven 2, it'll break things with


    java.lang.NoClassDefFoundError: org/codehaus/plexus/classworlds/launcher/Launcher


Reset things by;

  1. `cd /usr/share`  
  1. `sudo mv maven maven.new` (a symlink which should incorrectly be pointing to `java/maven-3.0.3)`
  1. `sudo ln -s /maven2/install/folder maven`
  1. run `mvn -version` to check its back up.
  1. Have a cup of tea.

This is most likely caused because you have an `M2_HOME` set, if you'd prefer to use Maven 3, remove the Maven 2 path setting with `export M2_HOME=`.


## Java Preferences.app

Prior to OS X 10.7, you could run the Java Preferences app `/Applications/Utilities/Java Preferences.app` to show your newly installed Java version. For example, after the install step above, you could check that "Java SE x (System)" was in the list.

However, Apple have recently [removed this app](http://reviews.cnet.com/8301-13727_7-57533880-263/java-preferences-missing-after-latest-os-x-java-update/) as they move away from in house support of Java.


