---
layout: post
title: "Home Brew Temperature Logger"
date: 2015-11-29 16:39
comments: true
categories: 
sidebar: false
published: false
keywords: "rasperry pi, pi, hobo, data logger, temperature, arduino"
description: "A home brew temperature logger using the Raspberry Pi zero for $10"
---

Using a Raspberry Pi Zero, some cheap components and some custom software, you can build a data logger to track ambient temperature in your house for around $10/£10. Track days or weeks of temperature data and display some pretty graphs via the web.

{% img ../../../../../images/temperature-machine.png 'The "temperature machine" in action' %}

<!-- more -->

## Order list

| Item | Price |
|--------------------------------------------------------------------------------|----------------------------------------|
| [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero) | £ 4
| [SanDisk 8GB microSDHC memory card](http://www.amazon.co.uk/gp/product/B013UDL5V6/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B013UDL5V6&linkCode=as2&tag=baddotrobotco-21) | £ 4
| [2.54mm Header strip](http://www.amazon.co.uk/gp/product/B00OVPHETK/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00OVPHETK&linkCode=as2&tag=baddotrobotco-21)  | £ 0.89
| [DS18B20 1-Wire temperature sensor](http://www.amazon.co.uk/gp/product/B00HCB8GLU/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00HCB8GLU&linkCode=as2&tag=baddotrobotco-21)    | £ 2.49
| 1 x 4.7k Ω resistor | £ 0.10
| [Some jumper wires](http://www.amazon.co.uk/gp/product/B00ATMHU52/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00ATMHU52&linkCode=as2&tag=baddotrobotco-21) or otherwise recycled wires with connectors |    £ 0.97
| | &nbsp;
| **Total** | **£ 12.45**


### Optional Extras

* USB Wifi adapter (about £ 6)
* Some heat shrink
* A case, I like the one from [Switched On Components](https://socomponents.co.uk/shop/black-laser-cut-acrylic-raspberry-pi-zero-case-with-gpio-access/) at £ 3.80
* A USB to TTL serial connection for headless setup. Something with a PL2302TA chip in it like [module](http://www.amazon.co.uk/gp/product/B00KM6X7FC/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00KM6X7FC&linkCode=as2&tag=baddotrobotco-21) or the [Adafruit console cable](https://www.adafruit.com/product/954).


## The Hardware

## The Software

The [`temperature-machine`](https://bitbucket.org/toby_weston/temperature-machine) software records temperature measurements storing it in a round robin database. It generates charts from this and serves up the data via a HTTP server. It's written in Scala and once you've setup SBT, cloned the Git repository onto your Pi Zero, build the binary with

    $ sbt -J-Xmx512m -J-Xms512m assembly

Then run from the project folder with

    $ ./start.sh


The data will be stored in `~/.temperature` and you can access the web page via your internal network with something like `http://10.0.1.55:11900`.


## Extras

Switching the Pi Zero LED off. https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=127336 and [Stack Overflow](http://raspberrypi.stackexchange.com/questions/40559/disable-leds-pi-zero?noredirect=1#comment57599_40559)

Switching the Edimax EW-7811 LED off. [Stack Overflow](http://raspberrypi.stackexchange.com/questions/40560/disable-led-for-edimax-ew-7811?noredirect=1#comment57486_40560)