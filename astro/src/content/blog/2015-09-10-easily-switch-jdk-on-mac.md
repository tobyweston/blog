---
title: "Easily Switch JDK on Mac"
pubDate: '2015-09-10'
categories: 'tools'
keywords: "Java versions, Mac, java_home, JAVA_HOME, JDK switch, multiple Java versions, Mac JDK"
description: "Easily switch between Java versions on Mac using the java_home utility. Includes bash function to set JAVA_HOME for any installed JDK version."
---

I have several versions of Java installed on my Mac. Trouble is, I can never remember where any of them are. So switching Java versions using the `JAVA_HOME` environment variable was always a pain. Then I discovered the handy `java_home` command.

```bash
/usr/libexec/java_home -V
```
    
It shows the Java versions are available and where there are. For example, on my machine, the output looks like this.


```bash
Matching Java Virtual Machines (4):
    1.8.0, x86_64:	"Java SE 8"	/Library/Java/JavaVirtualMachines/jdk1.8.0.jdk/Contents/Home
    1.7.0_25, x86_64:	"Java SE 7"	/Library/Java/JavaVirtualMachines/jdk1.7.0_25.jdk/Contents/Home
    1.6.0_65-b14-466.1, x86_64:	"Java SE 6"	/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
    1.6.0_65-b14-466.1, i386:	"Java SE 6"	/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
```

If you use the alternative option `-v <version>`, you get the path to a specific version.

```bash
/usr/libexec/java_home -v 1.8
```
      
It shows my 1.8 version lives at `/Library/Java/JavaVirtualMachines/jdk1.8.0.jdk/Contents/Home`. 

## Switch it!

To switch between versions, I can just run the following.

```bash
export JAVA_HOME=`/usr/libexec/java_home -v 1.8` 
```    
    
You could also add an alias to switch to a specific version;

```bash
alias setjava8='export JAVA_HOME=`/usr/libexec/java_home -v 1.8`'
```

If you want to do something more sophisticated, you could try something like [this](http://raibledesigns.com/rd/entry/installing_openjdk_7_on_os#comment-1311684547000) or [this](http://nemecec.blogspot.co.uk/2012/04/os-x-switching-java-versions-easily.html).   
    
**Caveat:** I don't have Java on my path, if you do, switching versions using the environment variable may not work.    

