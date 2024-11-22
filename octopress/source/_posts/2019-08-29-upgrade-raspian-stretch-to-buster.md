---
layout: post
title: "Upgrade Raspbian Stretch to Buster"
date: 2019-08-29 20:18
comments: true
categories: pi
sidebar: false
published: true
keywords: "raspberry pi, pi, buster, stretch, raspbian. raspian, upgrade"
description: "Upgrade your Raspbian install from Stretch to Buster."
---

Upgrade your Raspbian install from Stretch to Buster. This is basically the same procedure as upgrading [Jessie to Stretch]({{ root_url }}/blog/2017/10/26/upgrade-raspian-jessie-to-stretch) that I covered previously.

<!-- more -->

## Prepare

Get up to date.

    $ sudo apt-get update && sudo apt-get upgrade -y

Verify nothing is wrong. Verify no errors are reported after each command. Fix as required (you're on your own here!).

    $ dpkg -C
    $ apt-mark showhold


## Prepare `apt-get` Sources

Update the sources to `apt-get`. This replaces "stretch" with "buster" in the repository locations giving `apt-get` access to the new version's binaries.
   
    $ sudo sed -i 's/stretch/buster/g' /etc/apt/sources.list    
    $ sudo sed -i 's/stretch/buster/g' /etc/apt/sources.list.d/raspi.list    
    
Verify this caught them all by running the following, expecting no output. If the command returns anything having previously run the `sed` commands above, it means more files may need tweaking. Run the `sed` command for each. The aim is to replace all instances of "stretch".

    $ grep -lnr stretch /etc/apt    

Speed up subsequent steps by removing the list change package. 

    $ sudo apt-get remove apt-listchanges


## Do the Upgrade

To update existing packages without updating kernel modules or removing packages, run the following.

    $ sudo apt-get update && sudo apt-get upgrade -y
    
Alternatively, to include kernel modules and removing packages if required, run the following (choose one, not both. See this [question](https://askubuntu.com/questions/81585/what-is-dist-upgrade-and-why-does-it-upgrade-more-than-upgrade) for details).
    
    $ sudo apt-get update && sudo apt-get full-upgrade -y
    
Cleanup old outdated packages.

    $ sudo apt-get autoremove -y && sudo apt-get autoclean

Verify with `cat /etc/os-release`.
    
    
## Update Firmware    

You've come this far, might as well get the latest firmware.

    $ sudo rpi-update    
