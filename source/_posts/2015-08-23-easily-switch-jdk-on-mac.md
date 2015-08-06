---
layout: post
title: "Easily Switch JDK on Mac"
date: 2015-08-23 19:47
comments: true
categories: 
sidebar: false
published: false
keywords: ""
description: ""
---

I have several version of Java installed on my Mac. Trouble is, I can never remember where any of them are to switch between them when setting my `JAVA_HOME` environment variable. That is, until I discovered the following handy command.

    /usr/libexec/java_home -V
    
It shows me what Java versions are available and where there are. For example, on my machine, the output looks like this.

<!-- more -->

    Matching Java Virtual Machines (4):
        1.8.0, x86_64:	"Java SE 8"	/Library/Java/JavaVirtualMachines/jdk1.8.0.jdk/Contents/Home
        1.7.0_25, x86_64:	"Java SE 7"	/Library/Java/JavaVirtualMachines/jdk1.7.0_25.jdk/Contents/Home
        1.6.0_65-b14-466.1, x86_64:	"Java SE 6"	/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
        1.6.0_65-b14-466.1, i386:	"Java SE 6"	/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
        
If you use the alternative option `-v <version>`, you get the path to a specific version. So,
 
    /usr/libexec/java_home -v 1.8
      
shows me that my 1.8 version lives at `/Library/Java/JavaVirtualMachines/jdk1.8.0.jdk/Contents/Home`. 

To switch between versions, I can just run the following.

    export JAVA_HOME=`/usr/libexec/java_home -v 1.8` 
    
    
**Caveat:** I don't have Java on my path, if you do, switching just the environment variable may not work.    


## Script it FTW!    

