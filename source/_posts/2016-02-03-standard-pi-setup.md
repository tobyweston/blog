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
* Disable GUI via boot options, set to `B1 Console`
* Change hostname via Advanced options


### Setup Wifi

Modify the `/etc/network/interface` file to access a network (with hidden SSID).

    source-directory /etc/network/interfaces.d

    auto lo

    iface lo inet loopback
    iface eth0 inet dhcp

    auto wlan0
    allow-hotplug wlan0
    iface wlan0 inet dhcp
       wpa-scan-ssid 1
       wpa-ap-scan 1
       wpa-key-mgmt WPA-PSK
       wpa-proto RSN WPA
       wpa-pairwise CCMP TKIP
       wpa-group CCMP TKIP
       wpa-ssid "network-name"
       wpa-psk 72084.....654

    iface default inet dhcp


### Update the System

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get rpi-update


### Standard Software

    $ sudo apt-get install build-essential git avahi-daemon libavahi-client-dev


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


### Timezone

    sudo cp /usr/share/zoneinfo/Europe/London /etc/localtime