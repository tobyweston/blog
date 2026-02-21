---
title: "Upgrade Raspbian"
subTitle: "Stretch to Buster"
pubDate: "2019-08-29"
categories: 'pi'
keywords: "Raspbian Buster, Raspbian Stretch, Raspberry Pi upgrade, apt-get dist-upgrade, Raspbian upgrade"
description: "Step-by-step guide to upgrading Raspbian from Stretch to Buster on your Raspberry Pi."
---

Upgrade your Raspbian install from Stretch to Buster. This is basically the same procedure as upgrading [Jessie to Stretch](blog/2017-10-26-upgrade-raspian-jessie-to-stretch/) that I covered previously.

## Prepare

Get up to date.

```bash
$ sudo apt-get update && sudo apt-get upgrade -y
```

Verify nothing is wrong. Verify no errors are reported after each command. Fix as required (you"re on your own here!).

```bash
$ dpkg -C
$ apt-mark showhold
```


## Prepare `apt-get` Sources

Update the sources to `apt-get`. This replaces "stretch" with "buster" in the repository locations giving `apt-get` access to the new version's binaries.

```bash
$ sudo sed -i 's/stretch/buster/g' /etc/apt/sources.list    
$ sudo sed -i 's/stretch/buster/g' /etc/apt/sources.list.d/raspi.list    
```

Verify this caught them all by running the following, expecting no output. If the command returns anything having previously run the `sed` commands above, it means more files may need tweaking. Run the `sed` command for each. The aim is to replace all instances of "stretch".

```bash
$ grep -lnr stretch /etc/apt    
```

Speed up subsequent steps by removing the list change package. 

```bash
$ sudo apt-get remove apt-listchanges
```

## Do the Upgrade

To update existing packages without updating kernel modules or removing packages, run the following.

```bash
$ sudo apt-get update && sudo apt-get upgrade -y
```

Alternatively, to include kernel modules and removing packages if required, run the following (choose one, not both. See this [question](https://askubuntu.com/questions/81585/what-is-dist-upgrade-and-why-does-it-upgrade-more-than-upgrade) for details).

```bash
$ sudo apt-get update && sudo apt-get full-upgrade -y
```

Cleanup old outdated packages.

```bash
$ sudo apt-get autoremove -y && sudo apt-get autoclean
```

Verify with `cat /etc/os-release`.
    
    
## Update Firmware    

You've come this far, might as well get the latest firmware.

```bash
$ sudo rpi-update    
```