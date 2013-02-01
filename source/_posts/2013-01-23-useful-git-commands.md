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

<a id="top"></a>More as a reminder to myself than anything, here's a bunch of git commands I fund useful.

 - [Create a branch on a remote (pushing a branch to a remote)]({{ root_url }}/blog/2013/01/23/useful-git-commands#create_remote_branch)
 - [Delete a remote branch]({{ root_url }}/blog/2013/01/23/useful-git-commands#delete_remote_branch)
 - [Switch from HTTP to git/ssh]({{ root_url }}/blog/2013/01/23/useful-git-commands#switch_to_ssh)
 - [Set upstream branch]({{ root_url }}/blog/2013/01/23/useful-git-commands#set_upstream_branch)
 - [Abbreviated status]({{ root_url }}/blog/2013/01/23/useful-git-commands#status)


<!-- more -->

## <a id="create_remote_branch"></a>Create a branch on a remote (pushing a branch to a remote)

Having created a new feature branch locally, you can push to a remote, creating a new branch destination using.

    git push -u origin feature_branch

The `-u` sets upstream tracking and is optional.

[« Back to the list](#top)


## <a id="delete_remote_branch"></a>Delete a remote branch

Having pushed your feature branch,

    git push origin feature_branch

delete locally,

    git branch -d feature_branch

then delete remotely,

    git push origin --delete feature_branch

which is short hand for the full for `git push origin :feature_branch`. The colon looks out of place but its really just the everyday syntax of `git push <remote> <local branch>:<remote branch>` with a empty string representing the local branch. Effectively, it's saying, take no branch from my local branch and push it to the remote branch.



More on remote branches from [git ready](http://gitready.com/beginner/2009/02/02/push-and-delete-branches.html)

[« Back to the list](#top)



## <a id="switch_to_ssh"></a>Switch from HTTPS to git/ssh

If you're using HTTPS as you fetch url (check you `.git/config` file), you'll likely be asked for your username and password on each push. Switch to git/ssh with the following (assuming you've [setup ssh](https://help.github.com/articles/generating-ssh-keys)).

    git remote rm origin
    git remote add origin git@github.com:tobyweston/playground


This will alter your `.git/config` file from

    [remote "origin"]
        url = https://github.com/tobyweston/playground.git
        fetch = +refs/heads/*:refs/remotes/origin/*

to

    [remote "origin"]
        url = git@github.com:tobyweston/playground.git
        fetch = +refs/heads/*:refs/remotes/origin/*

but won't associate the remote branch with a local one. You'll need to [set an upstream branch](#set_upstream_branch) for that.

[« Back to the list](#top)


## <a id="set_upstream_branch"></a>Set upstream branch

Trying a `git pull` after the above will give you an error. Set the upstream thing (plurasight ref)

    You asked to pull from the remote 'origin', but did not specify
    a branch. Because this is not the default configured remote
    for your current branch, you must specify a branch on the command line.

Set the upstream branch with

    git branch --set-upstream master origin/master

which should report back,

    Branch master set up to track remote branch master from origin.

and change your `.git/config` file from

    [remote "origin"]

to

    [branch "master"]
        remote = origin
        merge = refs/heads/master


Do the same for any other remote branches.

[« Back to the list](#top)


## <a id="status"></a>Abbreviated status

The standard `git status` output

``` sh
$ git status
# On branch master
# Your branch is ahead of 'origin/master' by 1 commit.
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   LegoWars/BattleShip.h
#	modified:   LegoWars/BattleShip.m
#
```
The abbreviated `git status -sb` version

{% codeblock lang:sh %}
$ git status -sb
## master...origin/master [ahead 1]
 M LegoWars/BattleShip.h
 M LegoWars/BattleShip.m
{% endcodeblock %}