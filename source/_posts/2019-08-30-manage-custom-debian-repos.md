---
layout: post
title: "Creating Debian Repositories"
date: 2019-08-30 20:18
comments: true
categories: pi
sidebar: false
published: false
keywords: "raspberry pi, pi, buster, stretch, raspbian. debian, repositories"
description: "How to create your own Debian repository to distribute your software."
---

## Create a Repository

Create a repository called `badrobot-releases`. The `distribution` argument is `stretch`, `buster`, `stable` etc and will sit under the `dists` folder.

    $ aptly repo create -distribution=stable -component=temperature-machine badrobot-releases

Adding `.deb` packages to the repository (where `target` contains the `.dev` files).

    $ brew install gnupg
    $ aptly repo add badrobot-releases target

Check the repository has some packages.

    $ aptly repo show -with-packages badrobot-releases
    
    Name: badrobot-releases
    Comment: 
    Default Distribution: 
    Default Component: main
    Number of packages: 1
    Packages:
      temperature-machine_2.3_all
      
Publish to a local file system (without additional configuration, the default output will be `~/.aptly/public`).

    $ aptly publish repo badrobot-releases
    ERROR: unable to publish: unable to guess distribution name, please specify explicitly
    
    $ aptly -distribution=stable publish repo badrobot-releases
    Loading packages...
    ERROR: unable to publish: unable to figure out list of architectures, please supply explicit list
    
Nothing got created.

    $ ll ~/.aptly/public/dists/stable/    
    
Probably should have added those details in when creating the repository:

    aptly repo create -distribution=stable -component=temperature-machine badrobot-releases
    
but, this seems to work:

    $ aptly -distribution=stable -architectures=armhf publish repo badrobot-releases
    Loading packages...
    Generating metadata files and linking package files...
    Finalizing metadata files...
    Signing file 'Release' with gpg, please enter your passphrase when prompted:
    Clearsigning file 'Release' with gpg, please enter your passphrase when prompted:
    
    Local repo badrobot-releases has been successfully published.
    Please setup your webserver to serve directory '/Users/toby/.aptly/public' with autoindexing.
    Now you can add following line to apt sources:
      deb http://your-server/ stable main
    Don't forget to add your GPG key to apt with apt-key.
    
    You can also use `aptly serve` to publish your repositories over HTTP quickly.
    
The end result is:

    $ tree ~/.aptly/public/
    /Users/toby/.aptly/public/
    ├── dists
    │   └── stable                          <- distribution
    │       ├── Contents-armhf.gz
    │       ├── InRelease
    │       ├── Release
    │       ├── Release.gpg
    │       └── temperature-machine         <- component (defaults to main)
    │           ├── Contents-armhf.gz       
    │           └── binary-armhf            <- architecture
    │               ├── Packages
    │               ├── Packages.bz2
    │               ├── Packages.gz
    │               └── Release
    └── pool
        └── temperature-machine
            └── t
                └── temperature-machine
                    ├── temperature-machine_2.1_all.deb
                    └── temperature-machine_2.2_all.deb
    
    8 directories, 10 files

Compared to the current "robotooling" repository:

    $ tree ../robotooling/debian/
    ../robotooling/debian/
    ├── Packages
    ├── Packages.gz
    ├── en
    ├── en_GB
    ├── index.html
    └── stable
        ├── index.html
        ├── temperature-machine_2.1_all.changes
        ├── temperature-machine_2.1_all.deb
        ├── temperature-machine_2.2_all.changes
        └── temperature-machine_2.2_all.deb
    
    1 directory, 10 files
    
The contents of the `aptly` generated repo:

    $ cat Contents-all (.gz)
    FILE LOCATION
    etc/default/temperature-machine java/temperature-machine
    etc/temperature-machine java/temperature-machine
    lib/systemd/system/temperature-machine.service java/temperature-machine
    usr/bin/temperature-machine java/temperature-machine
    usr/share/man/man1/temperature-machine.1.gz java/temperature-machine
    usr/share/temperature-machine/bin/temperature-machine java/temperature-machine
    usr/share/temperature-machine/conf/application.ini java/temperature-machine
    usr/share/temperature-machine/conf/find_ip.sh java/temperature-machine
    usr/share/temperature-machine/lib/temperature-machine_2.12-2.3.jar java/temperature-machine
    usr/share/temperature-machine/logs java/temperature-machine
    
Packages file (`aptly` generated)

    $ cat main/binary-all/Packages
    Package: temperature-machine
    Priority: optional
    Section: java
    Installed-Size: 15968
    Maintainer: Toby Weston <toby@temperature-machine.com>
    Architecture: all
    Source: temperature-machine
    Version: 2.3
    Depends: openjdk-8-jdk
    Filename: pool/main/t/temperature-machine/temperature-machine_2.3_all.deb
    Size: 16370848
    MD5sum: c7a606bd6fbf00064f2f645dd4957f58
    SHA1: 8a1c9101ec9d18302cd2e9c34d4cdf0489e079e8
    SHA256: c5ad2d4bf15c3728f0851c3401ca71ad2da1fe11699b7d9c305515fe3c883149
    SHA512: db2f59e063ecbae5ac20793f2b8e2d531b0c6301f68b77099d838c0ba3b932fc0f7efc90b3ab783f338b915cbf02b1f7d7e70e3acb1928bd2838f583b25c9cf3
    Description: temperature data logger based on the DS18B20 sensor
     Homebrew temperature data logger based on the DS18B20 sensor.

Packages file (from "robotooling" / hand rolled)

    $ cat ~/code/github/robotooling/debian/Packages
    Package: temperature-machine
    Source: temperature-machine
    Version: 2.2
    Architecture: all
    Maintainer: Toby Weston <toby@temperature-machine.com>
    Installed-Size: 15968
    Depends: openjdk-8-jdk
    Filename: ./stable/temperature-machine_2.2_all.deb
    Size: 16370852
    MD5sum: f903a4980ab70910466633cd35b586f2
    SHA1: b71136d4f7ccbae89fc27c9a6da225ffdeaebd68
    SHA256: e3a20d91e2acd043d7021f52784425ac3454efbf48905f7c71b204c6d6c5d38b
    Section: java
    Priority: optional
    Description: temperature data logger based on the DS18B20 sensor
     Homebrew temperature data logger based on the DS18B20 sensor.

Release file

    $ cat ~/.aptly/public/dists/stable/temperature-machine/binary-armhf/Release 
    Origin: . stable
    Label: . stable
    Archive: stable
    Architecture: armhf
    Component: temperature-machine

Clean up published artifacts.

    $ aptly repo 

## Questions

### How's to backup the GPG key?

### How to handle the existing folder structure for upgrades?

### What instructions do I give my users?

See http://repo.aptly.info/ (you'll need to ensure they install the gpg key and upload it to some key server)

    $ apt-key adv --keyserver pool.sks-keyservers.net --recv-keys 00258F48226612AE

### How do I upload my key to a key server?

https://debian-administration.org/article/451/Submitting_your_GPG_key_to_a_keyserver

    $ gpg --send-keys 39E273602C8E7CE30DDDC32700258F48226612AE
    gpg: sending key 00258F48226612AE to hkps://hkps.pool.sks-keyservers.net
    gpg: keyserver send failed: No route to host
    gpg: keyserver send failed: No route to host
    $ echo $?
    2

Try an alternative (non default) key server:

    $ gpg --keyserver hkp://subkeys.pgp.net --send-keys 39E273602C8E7CE30DDDC32700258F48226612AE
    
Having listed the secret keys with:
    $ gpg --list-secret-keys
    
Can also upload manually via the website http://pool.sks-keyservers.net/#submit having exported the key:
   
    $ gpg --armor --export 00258F48226612AE
    
and search for it by email http://pool.sks-keyservers.net/pks/lookup?op=vindex&search=toby.weston%40gmail.com