---
layout: post
title: "Useful Git Commands"
date: 2013-01-23 19:55
comments: true
categories: 
sidebar: false
published: false
keywords: "git, tips"
description: "Some git commands I find useful but keep forgetting."
---

More as a reminder to myself than anything, here's a bunch of git commands I fund useful.

### Create a branch on a remote (pushing branch to remote)

### Delete a remote branch


### Switch out HTTPS to git/ssh

git remote rm origin
git remote add origin git@github.com:tobyweston/playground


### Set upstream branch

Trying a `git pull` after the above will give you an error. Set the upstream thing (plurasight ref)

git branch --set-upstream master origin/master
