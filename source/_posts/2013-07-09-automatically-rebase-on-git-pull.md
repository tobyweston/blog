---
layout: post
title: "Automatically rebase on git pull"
series: Git
date: 2013-07-09 17:29
comments: true
categories: recipes git
sidebar: false
published: true
keywords: "git, rebase, pull, merge, intellij"
description: "Learn how to automatically rebase your git repository on every pull (including configuring IntelliJ IDEA)"
---

Automaticaaly rebase your Git repository when you do a `pull`.

<!-- more -->

To configure your repository to always rebase when pulling;

```
git config branch.master.rebase true
```

which turns the relevant section of your '.git/config' from

```
[branch "master"]
  remote = origin
  merge = refs/heads/master
```

to

```
[branch "master"]
  remote = origin
  merge = refs/heads/master
  rebase = true
```

In IntelliJ IDEA, when doing up SCM update, it may ask you how to go about the update. Here you can override the setting above to do a regular merge (which is in fact a `git fetch` followed by a `git merge` or in one command, `git pull --no-rebase`), a rebase (`git fetch`, `git rebase` or `git pull --rebase`) or rely on the setting above in your config.
