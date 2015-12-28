---
layout: post
title: "Pi Console Lead"
date: 2015-12-28 19:52
comments: true
categories: 
sidebar: false
published: false
keywords: "Headless Pi Zero setup on El Captain (Mac OSX)"
description: "Without an ethernet port, the Pi Zero doesn't lend itself to setting up without a monitor, this post shows how to configure your wifi using the Adafruit console lead"
---

The Adafruit Console Lead uses the [PL2303TA](http://www.prolific.com.tw/US/ShowProduct.aspx?pcid=41) (a USB-to-serial/parallel converter chip) to talk to the Pi over GPIO pins 8 and 10 via USB. You can use this kind of USB to serial communication on plenty of devices but with the Pi, it's handy to use the `screen` application to effectively open a terminal to your Pi.

<!-- more -->

Most of the guides on the internet point you to older versions of the drivers, but to get things working on the Mac with El Capitan, I've found [v1.6 of the Prolific driver](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=229&pcid=41) is the only working option.


It's not hard to build you're own cable from the basic components or you could try [eBay for parts for under £2/$2](http://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.XPL2303TA.TRS0&_nkw=PL2303TA&_sacat=0) but I can't say if they use genuine Prolific chips or counterfeit.


## Create a Screen

    $ ls -la /dev/tty.usb*
    crw-rw-rw-  1 root  wheel   17,   4 28 Dec 19:49 /dev/tty.usbserial

Startup screen and point it to your Pi (`115200` is the baud rate to communicate with).

    screen /dev/tty.usbserial 115200

You might need to hit the `enter` key to wake things up, but you should see a regular Linux login prompt.

By default, the console width is 30 characters and wraps on a single line. It's pretty annoying when you paste a long command, so you can increase it for you session with the following

    stty cols 130


When you fire up the `screen` window manager, you can use Ctrl + A (![Option](/images/ks_control.gif) + `A`) to enter "command mode", hitting a subsequent key will execute a command. For example, Ctrl + A follwed by a `?` will show you some helpful commands.

Useful Screen commands.

| Command(s)        | Description
| Kill a session    | `Ctrl + A, Ctrl + \`


[Headless setup mounting an SD card](http://davidmaitland.me/2015/12/raspberry-pi-zero-headless-setup/)
