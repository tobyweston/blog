---
layout: post
title: "Standard Pi Setup"
date: 2016-02-03 19:01
comments: true
categories: 
sidebar: false
published: false
keywords: ""
description: ""
---

Common things to do when you first setup a Pi.

<!-- more -->

## Shopping List

Wifi setup


### rpi-config

* Extend the file system

### Update the System

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get rpi-update


### Standard Software

    $ apt-get install build-essential git avahi-daemon libavahi-client-dev


### Disable GUI

Do via `raspi-config` boot options, set to `B1 Console`


### Change hostname




### Bash Setup

Add the following to `~/.bashrc`

    # some more ls aliases
    alias ll='ls -lv --group-directories-first'
    alias la='ls -A'
    #alias l='ls -CF'

    # Toby's ones
    alias path='echo -e ${PATH//:/\\n}'
    alias libpath='echo -e ${LD_LIBRARY_PATH//:/\\n}'
    alias du='du -kh'    # Makes a more readable output.
    alias df='df -kTh'

### Vi setup

    $ echo 'set nocompatible' > ~/.vimrc