---
layout: post
title: "Standard Pi Setup"
date: 2017-03-01 19:01
comments: true
categories: pi
sidebar: false
published: true
keywords: "pi, pi zero, zero w, raspian"
description: "Some common setup for a new Pi"
---

Here's some common things to do when you first setup a Pi.

<!-- more -->

## Raspian Image

Download your image and [burn to an SD card](https://www.raspberrypi.org/documentation/installation/installing-images/). You can't go far wrong with a [SanDisk 16GB microSDHC memory card](http://amzn.to/1T6zIc9)for £6.99.

## `raspi-config`

* Expand the file system
* Disable GUI via boot options, set to `Boot Options` then `B1 Console`
* Change hostname via Advanced options


## Setup Wifi

Modify the `/etc/network/interfaces` file to access a network (with hidden SSID).

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

## Prevent Wifi Sleeping

The `8192cu` based wifi dongles will often go to sleep if they're not getting any traffic. This means broken terminal sessions and general annoyances. Prevent it happening by adding the following to `/etc/modprobe.d/8192cu` (create the file if it doesn't already exist).

    options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
    
You can check if you have the `8192cu` module loaded with `lsmod`. If you don't see it in the list, don't bother!


## Update the System

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo rpi-update


## Standard Software

    $ sudo apt-get install build-essential git avahi-daemon libavahi-client-dev


## Bash Setup

Add the following to `~/.bashrc`

    # some more ls aliases
    alias ll='ls -lvh --group-directories-first'
    alias la='ls -A'
    #alias l='ls -CF'

    # Toby's ones
    alias path='echo -e ${PATH//:/\\n}'
    alias libpath='echo -e ${LD_LIBRARY_PATH//:/\\n}'
    alias du='du -kh'    # Makes a more readable output.
    alias df='df -kTh'


## Share Disk with Mac OSX

    sudo apt-get install netatalk


## `vi` setup

    $ echo 'set nocompatible' > ~/.vimrc


## Timezone

    sudo cp /usr/share/zoneinfo/Europe/London /etc/localtime
    
    
## SBT on the Pi Zero

There's not much memory, so limit `sbt`s consumption.

    sbt -J-Xmx512m -J-Xms256m
