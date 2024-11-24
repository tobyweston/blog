---
title: "Automatically rebase on git pull"
series: 'Git'
pubDate: '2013-07-09'
categories: 'recipes git'
keywords: "git, rebase, pull, merge, intellij"
description: "Learn how to automatically rebase your git repository on every pull (including configuring IntelliJ IDEA)"
---

Automatically rebase your Git repository when you do a `pull`.


To configure your repository to always rebase when pulling;

```shell
git config branch.master.rebase true
```

which turns the relevant section of your '.git/config' from

```shell
[branch "master"]
  remote = origin
  merge = refs/heads/master
```

to

```shell
[branch "master"]
  remote = origin
  merge = refs/heads/master
  rebase = true
```

In IntelliJ IDEA, when doing up SCM update, it may ask you how to go about the update. Here you can override the setting above to do a regular merge (which is in fact a `git fetch` followed by a `git merge` or in one command, `git pull --no-rebase`), a rebase (`git fetch`, `git rebase` or `git pull --rebase`) or rely on the setting above in your config.
