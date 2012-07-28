---
layout: post
title: "Mountain Lion Carnage"
date: 2012-07-28 12:28
comments: true
categories: java
sidebar: false
published: false
keywords: "mountain lion, mac osx, 10.8, java, svn, git, git broken after mountain lion, svn broken after mountain lion"
description: "The Mountain Lion upgrade blasts Java, svn and git. Find out how to get them back"
---

After installing Mountain Lion, I discovered Java was gone along with Subversion and Git. I went through these steps to bring them back.

## Java

OSX will install this for you the first time you try and start up a Java app. It setups a symbolic link for `mvn` to point to Maven 3 which may need adjusting if you're still using Maven 2. See [this post]({{ root_url}}/2011/10/29/java-source-on-mac) for the fix.


## Git

On my machine, before the update, Git used to live in

    /usr/bin/git

Which I think was a symbolic link pointing to `/usr/local/git`. This gets wiped out by Mountain Lion, to preserve any tools using the old reference (IntelliJ IDEA), I created a new sym link.

    sudo ln -s /usr/local/git/bin/git /usr/bin/git


The `/usr/bin` folder is on my `$PATH` but you could also recreate a symlink from the local binaries folder to `/usr/local/bin` to get the terminal working again.

    sudo ln -s /usr/local/git/bin/git /usr/local/bin/git


## Subversion

[Apparently](http://www.sublimetext.com/forum/viewtopic.php?f=3&p=34790), Apple removed Subversion with 10.8 so there's nothing to do other than install it manually.

You can install Xcode which should put Subversion in `/Applications/Xcode.app/Contents/Developer/usr/bin/svn`.

Victor Quinn talks about [reinstalling Xcode](http://victorquinn.com/blog/2012/02/19/fix-git-svn-in-mountain-lion/).