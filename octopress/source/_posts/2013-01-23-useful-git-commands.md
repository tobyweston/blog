---
layout: post
title: "Useful Git Commands"
series: Git
pubDate: 2013-01-23 19:55
comments: true
categories: recipes git
sidebar: false
published: true
keywords: "git, tips, delete remote branch, remove branch, github, ssh, https"
description: "Some git commands I find useful but keep forgetting like removing a remote branch."
---

<a id="top"></a>More as a reminder to myself than anything, here's a bunch of Git commands I fund useful.

 - [Create a branch on a remote (pushing a branch to a remote)](/blog/2013/01/23/useful-git-commands#create_remote_branch)
 - [Delete a remote branch](/blog/2013/01/23/useful-git-commands#delete_remote_branch)
 - [Switch from HTTP to git/ssh](/blog/2013/01/23/useful-git-commands#switch_to_ssh)
 - [Set upstream branch](/blog/2013/01/23/useful-git-commands#set_upstream_branch)
 - [Abbreviated status](/blog/2013/01/23/useful-git-commands#status)
 - [Useful Git aliases](/blog/2013/01/23/useful-git-commands#alias)


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

which is short hand for `git push origin :feature_branch`. The colon looks out of place but its really just the everyday syntax of `git push <remote> <local branch>:<remote branch>` with a empty string representing the local branch. Effectively, it's saying, take no branch from my local branch and push it to the remote branch.



More on remote branches from [git ready](http://gitready.com/beginner/2009/02/02/push-and-delete-branches.html)

[« Back to the list](#top)



## <a id="switch_to_ssh"></a>Switch from HTTPS to git/ssh

If you're using HTTPS as your fetch url (check your `.git/config` file), you'll likely be asked for your username and password on each push. Switch to git/ssh with the following (assuming you've [setup ssh](https://help.github.com/articles/generating-ssh-keys)).

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

Trying a `git pull` after [switching from HTTPS to git/ssh above](#switch_to_ssh) will give you an error.

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

``` sh
$ git status -sb
## master...origin/master [ahead 1]
 M LegoWars/BattleShip.h
 M LegoWars/BattleShip.m
```

## <a id="alias"></a>Useful Git aliases and config

Set the proxy, your user name and a couple of useful configurations. Feed straight in from the shell.

``` sh
git config --global http.proxy myproxy:8080
git config --global user.email me@email.com
git config --global user.name me
git config --global color.ui true
```

Some useful aliases.

``` sh
git config --global alias.last "log -1 HEAD"
git config --global alias.st "status -sb"
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"
```


## Recommended Reading

<div>
    <script type="text/javascript">
    function trackOutboundLink(link, category, action) {

        try {
            _gaq.push(['_trackEvent', category , action]);
        } catch(err){}

        setTimeout(function() {
            document.location.href = link.href;
        }, 100);
    }
    </script>
</div>

<a href="http://www.amazon.co.uk/gp/product/1934356727/ref=as_li_ss_il?ie=UTF8&camp=1634&creative=19450&creativeASIN=1934356727&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">![](http://ecx.images-amazon.com/images/I/41iwlU4g9yL._SL160_.jpg 'Pragmatic Guide to Git (Pragmatic Programmers)' %}</a>
<a href="http://www.amazon.co.uk/gp/product/1934356158/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1934356158&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">![](http://ecx.images-amazon.com/images/I/519CeNsejdL._SL160_.jpg 'Pragmatic Version Control Using Git' %}</a>

 * <a href="http://www.amazon.co.uk/gp/product/1934356727/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1934356727&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">Pragmatic Guide to Git (Pragmatic Programmers)</a>, Travis Swicegood
 * <a href="http://www.amazon.co.uk/gp/product/1934356158/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1934356158&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">Pragmatic Version Control Using Git: 1 (Pragmatic Starter Kit)</a>, Travis Swicegood
 * <a href="http://www.amazon.co.uk/gp/product/1430218339/ref=as_li_ss_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=1430218339&linkCode=as2&tag=baddotrobot-21" onClick="trackOutboundLink(this, 'Outbound Links', 'amazon.com'); return false;">Pro Git (Expert's Voice in Software Development)</a>, Scott Chacon
