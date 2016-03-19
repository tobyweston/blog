---
layout: post
title: "Home Brew Temperature Logger"
date: 2015-11-29 16:39
comments: true
categories: 
sidebar: false
published: false
keywords: "raspberry pi, pi, pi zero, ds20b18, ds18b20, hobo, data logger, temperature, arduino"
description: "A home brew temperature logger using the Raspberry Pi zero for $10"
---

Using a Raspberry Pi Zero, some cheap components and some custom software, you can build a data logger to track ambient temperature in your home for around £10. Track days, weeks and months worth of temperature data and display some pretty graphs via the web.

[{% img ../../../../../images/temperature-machine.png 'The "temperature machine" in action' %}](../../../../../images/temperature-machine.png)

<!-- more -->

## Order list

| Item | Price |
|------|-------|
| [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero) | £ 4
| [SanDisk 8GB microSDHC memory card](http://www.amazon.co.uk/gp/product/B013UDL5V6/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B013UDL5V6&linkCode=as2&tag=baddotrobotco-21) | £ 4
| [2.54mm Header strip](http://www.amazon.co.uk/gp/product/B00OVPHETK/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00OVPHETK&linkCode=as2&tag=baddotrobotco-21)  | £ 0.89
| [DS18B20 1-Wire temperature sensor](http://www.amazon.co.uk/gp/product/B00HCB8GLU/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00HCB8GLU&linkCode=as2&tag=baddotrobotco-21)    | £ 2.49
| 1 x 4.7k Ω resistor | £ 0.10
| [Some jumper wires](http://www.amazon.co.uk/gp/product/B00ATMHU52/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00ATMHU52&linkCode=as2&tag=baddotrobotco-21) or otherwise recycled wires with connectors |    £ 0.97
| Data logging software | <span style="color:green;">FREE</span>
| | &nbsp;
| **Total** | **£ 12.45**


### Optional Extras

* USB Wifi adapter (about £ 6)
* Some heat shrink
* A case, I like the one from [Switched On Components](https://socomponents.co.uk/shop/black-laser-cut-acrylic-raspberry-pi-zero-case-with-gpio-access/) at £ 3.80
* A USB to TTL serial connection for headless setup. Something with a PL2302TA chip in it like [this module](http://www.amazon.co.uk/gp/product/B00KM6X7FC/ref=as_li_tl?ie=UTF8&camp=1634&creative=19450&creativeASIN=B00KM6X7FC&linkCode=as2&tag=baddotrobotco-21) or the [Adafruit console cable](https://www.adafruit.com/product/954).


## Setup the Hardware

Connecting the temperature sensor to the Pi is straight forward. There a loads of [tutorials on the web](https://www.google.co.uk/search?btnG=1&pws=0&q=pi+ds18b20+tutorial) but you're looking to connect the following physical pins on the Pi to the following sensor connectors.

Physical Pi Pin | Description | DS18b20 Connector
----------------|-------------|--------
1 | 3.3v Power  | Power (<span style="color:red;">red</span>)
7 | GPIO 4      | Data (<span style="color:orange;">yellow</span>)
9 | Ground      | Ground (<span style="color:black;">black</span>)

The other thing you'll need to do is connect the 4.7k Ω between the power and data lines. This acts as a [pull-up resistor](https://learn.sparkfun.com/tutorials/pull-up-resistors) to ensure that the Pi knows that the data line starts in a "high" state. Without it, it can't tell if it should start as high or low; it would be left _floating_.


## Setup the Pi

Make sure you have the following line in your `/boot/config.txt`. It will load the GPIO 1-wire driver and any attached temperature sensor should be automatically detected.

    dtoverlay=w1-gpio

On the sensor itself, temperature measurements are stored in an area of memory called the "scratchpad". If everything is connected ok, the contents of the scratchpad will be written to a file under `/sys/bus/w1/devices/28-xxx/w1_slave` (where `xxx` will be a HEX number unique to your sensor). Here's an example from my `w1_slave` file.

    4b 01 4b 46 7f ff 05 10 d8 : crc=d8 YES
    4b 01 4b 46 7f ff 05 10 d8 t=20687

The temperature is shown as the `t` value; 20.687 °C in this case. The scratchpad allows you to program the sensor as well as read temperature data from it. See the [data sheet](https://www.adafruit.com/datasheets/DS18B20.pdf) or [my associated README]() for more details.

Once you can see the `w1_slave` file, you're ready to install the data logging software.


## Setup the Data Logging Software

There are lots of options to record the temperature data but for something a bit different, the [temperature-machine](https://bitbucket.org/toby_weston/temperature-machine) software connects multiple Pi's together, showing the data from each of them. It can read temperatures from multiple sensors on multiple Pis, sending the data to a nominated "server" Pi. The server stores it all in a round robin database, generates the charts and serves it all up via a web server.

It's written in Scala and you'll need the `sbt` tool to build it. To setup `sbt` follow these steps.

    $ cd /usr/local/bin
    $ wget https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-launch/0.13.9/sbt-launch.jar

Create a file `/usr/local/bin/sbt` and paste the following in (take note that the max memory is set to 512 MB for the Pi Zero).

    #!/bin/bash
    SBT_OPTS="-Xms512M -Xmx512M -Xss1M -XX:+CMSClassUnloadingEnabled"
    java $SBT_OPTS -jar `dirname $0`/sbt-launch.jar "$@"

Then make it executable.

    chmod u+x ~/bin/sbt


Once you've setup SBT, clone the data logger's Git repository and build the binary.


    $ mkdir ~/code
    $ git clone https://toby_weston@bitbucket.org/toby_weston/temperature-machine.git ~/code/temperature-machine
    $ cd ~/code/temperature-machine
    $ sbt assembly

Then run from the project folder with

    $ ./start.sh


The data will be stored in `~/.temperature` and you can access the web page via your internal network with something like `http://10.0.1.55:11900`. Get you're IP address on the Pi with `hostname -I`.


### One Node or Two?

By default, running `start.sh` will start up the app in "server" mode. It will expect ...


### Multiple Sensors

The 1-wire protocol allows you to chain multiple sensors, so each Pi can have any number of sensors attached. The temperature-machine software automatically support up to five sensors. I found soldering a bunch of sensors together a bit tricky so I put together a simple PCB to allow me to chain them without soldering.

[{% img ../../../../../images/temperature-machine-add-on-1.png 266 200 'Multiple sensor add-on board' %}](../../../../../images/temperature-machine-add-on-1.png) [{% img ../../../../../images/temperature-machine-add-on-2.png 200 266 'With headers and resistor soldered' %}](../../../../../images/temperature-machine-add-on-2.png)



### Start Logger Automatically

There are different ways to start software automatically after a reboot, but for the `temperature-machine`, add the following to `/etc/rc.local`

    su pi -c 'cd /home/pi/code/temperature-machine && ./start.sh &'


It will run the start script that comes with the looger (`start.sh`) as the user `pi`. It assumes you've cloned the code in the previous step to `/home/pi/code/temperature-machine`. After rebooting, you should see a log file and `pid` file in the same location.


## Extras

Switching the Pi Zero LED off. https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=127336 and [Stack Overflow](http://raspberrypi.stackexchange.com/questions/40559/disable-leds-pi-zero?noredirect=1#comment57599_40559)

Switching the Edimax EW-7811 LED off. [Stack Overflow](http://raspberrypi.stackexchange.com/questions/40560/disable-led-for-edimax-ew-7811?noredirect=1#comment57486_40560)