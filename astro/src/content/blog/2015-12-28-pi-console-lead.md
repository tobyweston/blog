---
title: "Pi Console Lead"
pubDate: '2015-12-28'
categories: 'raspberry-pi'
keywords: "Raspberry Pi Zero, console lead, Adafruit, serial connection, headless Pi setup, Mac, El Capitan, PL2303"
description: "Set up a headless Raspberry Pi Zero using an Adafruit console lead. Step-by-step guide for Mac users on El Capitan/Sierra using the Prolific PL2303 driver."
heroImage: "/images/heroes/raspberry-pi.jpg"
---

Without an ethernet port, the Pi Zero doesn't lend itself to being setup without a monitor and keyboard. This post shows how to configure your wifi using the Adafruit console lead without having to plug in a monitor or keyboard.

The Adafruit Console Lead uses the [PL2303TA](http://www.prolific.com.tw/US/ShowProduct.aspx?pcid=41) (a USB-to-serial/parallel converter chip) to talk to the Pi over GPIO pins 8 and 10 via USB. You can use this kind of USB to serial communication on plenty of devices but with the Pi, it's handy to use the `screen` application to effectively open a "telnet-like" terminal to your Pi.


Most of the guides on the internet point you to older versions of the drivers, but to get things working on the Mac with El Capitan or Sierra, I've found [v1.6 of the Prolific driver](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41) is the only working option.


It's not hard to build you're own cable from the basic components or you could try [eBay for parts for under £2/$2](http://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.XPL2303TA.TRS0&_nkw=PL2303TA&_sacat=0) but I can't say if they use genuine Prolific chips or counterfeit.


## Create a Screen

```bash
$ ls -la /dev/tty.usb*
crw-rw-rw-  1 root  wheel   17,   4 28 Dec 19:49 /dev/tty.usbserial
```

Startup screen and point it to your Pi (`115200` is the baud rate to communicate with).

```bash
screen /dev/tty.usbserial 115200
```

You might need to hit the `enter` key to wake things up, but you should see a regular Linux login prompt.

By default, the console width is 30 characters and wraps on a single line. It's pretty annoying when you paste a long command, so you can increase it for you session with the following

```bash
stty cols 130
```

When you fire up the `screen` window manager, you can use `Ctrl` + `A` (![Option](/images/ks_control.gif) + `A`) to enter "command mode", hitting a subsequent key will execute a command. For example, `Ctrl` + `A` followed by a `?` will show you some helpful commands.

Here are some reminders of useful commands.

| Command(s)        | Description
|-------------------|------------------------
| Get some help     | `Ctrl + A, ?`
| Kill a session    | `Ctrl + A, Ctrl + \`


## Initial Setup

You might want to setup you're wireless from within `screen`. Connecting to a non-hidden network is straight forward. Setting things up for a hidden network is [a little more involved](http://www.dafinga.net/2013/01/how-to-setup-raspberry-pi-with-hidden.html).

Check you `/etc/network/interfaces` file and ensure it has a `wlan0` section. For open networks, something like this.

```bash
source-directory /etc/network/interfaces.d

auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet dhcp
   wpa-ssid "Guest Network"
   wpa-psk "passphrase"
```

...and for hidden networks, something like this.

Modify the `/etc/network/interfaces` file to access a network (with hidden SSID).

```bash
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
   wpa-psk 12484.....654

iface default inet dhcp
```

## Summary

Using the console lead is an easy way to use a telnet-like terminal to setup your Pi when you don't want to connect a monitor and keyboard. As an alternative, you could try a [headless setup mounting an SD card](http://davidmaitland.me/2015/12/raspberry-pi-zero-headless-setup/), whereby you'd mount an SD Card (with a raspian image) onto a unix-like machine and modify the file system directly.

See my post on [common Pi setup](/blog/2017-03-01-standard-pi-setup) for more notes and tips on general Pi setup.
