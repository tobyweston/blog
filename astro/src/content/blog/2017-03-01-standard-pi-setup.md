---
title: "Standard Pi Setup"
pubDate: "2017-03-01"
categories: 'raspberry-pi'
keywords: "Raspberry Pi setup, Raspbian, SD card, Pi Zero W, headless setup, SSH, new Pi configuration"
description: "Standard Raspberry Pi setup steps: flash Raspbian, enable SSH, configure Wi-Fi, and get your Pi ready for headless use."
---

Here"s some common things to do when you first setup a Pi.


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

The `8192cu` based wifi dongles will often go to sleep if they're not getting any traffic. This means broken terminal sessions and general annoyances. Prevent it happening by adding the following to `/etc/modprobe.d/8192cu.conf`. Create the file if it doesn't already exist ([reference](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=44044&start=350)).

    options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
    
You can check if you have the `8192cu` module loaded with `lsmod`. If you don't see it in the list, don't bother!


## Update the System

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo rpi-update


## Standard Software

    $ sudo apt-get install build-essential git avahi-daemon libavahi-client-dev oracle-java8-jdk

## Install SBT 

For Scala development.

    $ cd /usr/local/bin
    $ sudo wget https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-launch/0.13.13/sbt-launch.jar
    $ sudo chown pi sbt-launch.jar
    $ sudo chgrp pi sbt-launch.jar

Create a file `/usr/local/bin/sbt` (change the owner and group as above) and paste the following in (take note that the max memory is set to 512 MB for the Pi Zero). Change the owner and group as above.

    #!/bin/bash
    SBT_OPTS="-Xms512M -Xmx512M"
    java $SBT_OPTS -jar `dirname $0`/sbt-launch.jar "$@"

Note that there's not much memory on the Pi, so limit `sbt`s consumption. In this case, the 512MB limit suits the Pi Zero.

Then make it executable.

    chmod u+x /usr/local/bin/sbt


## Bash Setup

Add the following to `~/.bashrc`

    # some more ls aliases
    alias ll='ls -lavh --group-directories-first'
    alias la='ls -A'
    #alias l='ls -CF'

    # Toby's ones
    alias path='echo -e ${PATH//:/\\n}'
    alias libpath='echo -e ${LD_LIBRARY_PATH//:/\\n}'
    alias du='du -kh'    # Makes a more readable output.
    alias df='df -kTh'


## Disable Activity LED

Add the following to `/boot/config.txt` (tested on the Pi Zero only).

    # disable the activity LED (intended for the Pi Zero)
    dtparam=act_led_trigger=none
    dtparam=act_led_activelow=on


## Share Disk with Mac OSX

    sudo apt-get install netatalk


## `vi` setup

    $ echo 'set nocompatible' > ~/.vimrc


## Timezone

    sudo cp /usr/share/zoneinfo/Europe/London /etc/localtime
    