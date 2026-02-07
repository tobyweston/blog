---
title: "Upgrade Raspbian Jessie to Stretch'"
pubDate: "2017-10-26'"
categories: 'pi'
keywords: "raspberry pi, pi, stretch, jessie, raspbian. raspian, upgrade'"
description: "Upgrade your Raspbian install from Jessie to Stretch."
---

Upgrade your Raspbian install from Jessie to Stretch.


## Prepare

Get up to date.

    $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get dist-upgrade

Verify nothing is wrong. Verify no errors are reported after each command. Fix as required (you"re on your own here!).

    $ dpkg -C
    $ apt-mark showhold

Optionally upgrade the firmware.

    $ sudo rpi-update    

## Prepare `apt-get`

Update the sources to `apt-get`. This replaces "jessie" with "stretch" in the repository locations giving `apt-get` access to the new version's binaries.
   
    $ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list    
    $ sudo sed -i 's/jessie/stretch/g' /etc/apt/sources.list.d/raspi.list    
    
Verify this caught them all. Run the following, expecting no output. If the command returns anything having previously run the `sed` commands above, it means more files may need tweaking. Run the `sed` command for each.

    $ grep -lnr jessie /etc/apt    

Speed up subsequent steps by removing the list change package. 

    $ sudo apt-get remove apt-listchanges


## Do the Upgrade

    $ sudo apt-get update && sudo apt-get upgrade -y
    $ sudo apt-get dist-upgrade -y
    
Cleanup old outdated packages.

    $ sudo apt-get autoremove -y && sudo apt-get autoclean

Verify with `cat /etc/os-release`.
    
    
## Update Firmware    

You've come this far, might as well get the latest firmware.

    $ sudo rpi-update    
