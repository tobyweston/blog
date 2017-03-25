---
layout: post
title: "Home Brew Temperature Logger"
date: 2016-03-23 21:39
comments: true
categories: pi
sidebar: false
published: true
keywords: "raspberry pi, pi, pi zero, ds20b18, ds18b20, hobo, data logger, temperature, arduino, scala"
description: "A home brew temperature logger using the Raspberry Pi zero for around $10"
---

Using a Raspberry Pi Zero, some cheap components and some custom software, you can build a data logger to track ambient temperature in your home for around £10. Track days, [weeks](../../../../../images/temperature-30-days.png) and months worth of temperature data and display some pretty graphs via the web.

[{% img ../../../../../images/temperature-machine.png 'The "temperature machine" in action' %}](../../../../../images/temperature-machine.png)

<!-- more -->

## Order list

| Item | Price |
|------|-------|
| [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero) | £ 4
| [SanDisk 8GB microSDHC memory card](http://amzn.to/1T6zIc9) | £ 4
| [2.54mm Header strip](http://amzn.to/1pIKZ7m)  | £ 0.89
| [DS18B20 1-Wire temperature sensor](http://amzn.to/1RhmOHc)    | £ 2.49
| 1 x 4.7k Ω resistor | £ 0.10
| [Some jumper wires](http://amzn.to/1Rlrbj9) or otherwise recycled wires with connectors |    £ 0.97
| Data logging software | <span style="color:green;">[FREE](https://github.com/tobyweston/temperature-machine)</span>
| | &nbsp;
| **Total** | **£ 12.45**


**Optional extras** You might also want to consider a [USB Wifi adapter](http://amzn.to/1RhmTKQ) (about £ 6), a case (I like the one from [Switched On Components](https://socomponents.co.uk/shop/black-laser-cut-acrylic-raspberry-pi-zero-case-v2/) at £ 3.80) and a USB to TTL serial connection for headless setup. Something with a PL2302TA chip in it like [this module](http://amzn.to/1ZtRWoA) or the [Adafruit console cable](https://www.adafruit.com/product/954).


## Setup the Hardware

Connecting the temperature sensor to the Pi is straight forward. There a loads of [tutorials on the web](https://www.google.co.uk/search?btnG=1&pws=0&q=pi+ds18b20+tutorial) but you're looking to connect the following physical pins on the Pi to the following sensor connectors.

Physical Pi Pin | Description | DS18b20 Connector
----------------|-------------|--------
1 | 3.3v Power  | Power (<span style="color:red;">red</span>)
7 | GPIO 4      | Data (<span style="color:orange;">yellow</span>)
9 | Ground      | Ground (<span style="color:black;">black</span>)

The other thing you'll need to do is connect the 4.7k Ω resistor between the power and data lines. This acts as a [pull-up resistor](https://learn.sparkfun.com/tutorials/pull-up-resistors) to ensure that the Pi knows that the data line starts in a "high" state. Without it, it can't tell if it should start as high or low; it would be left _floating_.


## Setup the Pi

Make sure you have the following line in your `/boot/config.txt`. It will load the GPIO 1-wire driver and any attached temperature sensor should be automatically detected.

    dtoverlay=w1-gpio

On the sensor itself, temperature measurements are stored in an area of memory called the "scratchpad". If everything is connected ok, the contents of the scratchpad will be written to a file under `/sys/bus/w1/devices/28-xxx/w1_slave` (where `xxx` will be a HEX number unique to your sensor). Here's an example from my `w1_slave` file.

    4b 01 4b 46 7f ff 05 10 d8 : crc=d8 YES
    4b 01 4b 46 7f ff 05 10 d8 t=20687

The temperature is shown as the `t` value; 20.687 °C in this case. The scratchpad allows you to program the sensor as well as read temperature data from it. See the [data sheet](https://www.adafruit.com/datasheets/DS18B20.pdf) or [my associated README]() for more details (including how to change the precision of the sensor).

Once you can see the `w1_slave` file, you're ready to install the data logging software.


## Setup the Data Logging Software

There are lots of options to record the temperature data but for something a bit different, the [temperature-machine](https://github.com/tobyweston/temperature-machine) software logs temperatures from multiple sensors on multiple Pi's. It sends the data to a nominated "server" Pi and the server stores it all in a round robin database and serves up the charts via a web page.

It's written in Scala and you'll need the `sbt` tool to build it. To setup `sbt` follow these steps.

    $ cd /usr/local/bin
    $ sudo wget https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-launch/0.13.13/sbt-launch.jar
    $ sudo chown pi sbt-launch.jar
    $ sudo chgrp pi sbt-launch.jar

Create a file `/usr/local/bin/sbt` (change the owner and group as above) and paste the following in (take note that the max memory is set to 512 MB for the Pi Zero). Change the owner and group as above.

    #!/bin/bash
    SBT_OPTS="-Xms512M -Xmx512M"
    java $SBT_OPTS -jar `dirname $0`/sbt-launch.jar "$@"

Then make it executable.

    chmod u+x /usr/local/bin/sbt


Once you've setup SBT, clone the data logger's Git repository and build the binary.


    $ mkdir ~/code
    $ git clone https://github.com/tobyweston/temperature-machine.git ~/code/temperature-machine
    $ cd ~/code/temperature-machine
    $ sbt assembly

Then run from the project folder with the following.

    $ ./start.sh


The data will be stored in `~/.temperature` and you can access the web page via your internal network with something like `http://10.0.1.55:11900`. Get you're IP address on the Pi with `hostname -I`.


## Add Multiple Machines

Running `start.sh` will start up the app in "server" single-machine mode. It will start logging data and serve the web page but not expect any more machines to be sending it data. To support multiple machines, you need to do a little more configuration.

Due to the way round robin databases work, you need to say upfront how many machines you want to connect. It will support up to five sensors per machine. So the first thing is to start up the server specifying the `hostname` of each machine. To do this, you can use the `start-server.sh` script instead of `server.sh`.

    ./start-server.sh bedroom garage


In this example, I changed the hostname of each machine to the room they're situated in. If you already have data in `~/.temperature`, you'll have to manually delete the contents first (`rm ~/.temperature/*`). It will start up in the server and log data sent from machines named `bedroom` and `garage`. Make sure the hostname of the machine you run this from is included in the list.

The next job is to run the client version on each machine, so if `garage` is my server, I'd run the following on the `bedroom` machine. Ensure this machine's hostname matches what you setup on the server (i.e. `bedroom`).

    ./start-client.sh


The server broadcasts it's IP address, so any clients should automatically detect where the server is and start sending data to it.


## Add Multiple Sensors

The 1-wire protocol allows you to chain multiple sensors, so each Pi can have any number of sensors attached. The software automatically supports up to five sensors. Connect them to your Pi and restart and they'll be automatically detected and included in the charts.


I found soldering a bunch of sensor wires together along with the resistor a bit tricky so I put together a simple PCB to allow me to chain them without soldering.

[{% img ../../../../../images/temperature-machine-add-on-1.png 266 200 'Save soldering with a multiple sensor add-on board' %}](../../../../../images/temperature-machine-add-on-1.png) [{% img ../../../../../images/temperature-machine-add-on-2.png 266 200 'With headers and resistor soldered' %}](../../../../../images/temperature-machine-add-on-2.png) [{% img ../../../../../images/temperature-machine-add-on-3.png 266 200 'Three sensors connected' %}](../../../../../images/temperature-machine-add-on-3.png) [{% img ../../../../../images/temperature-machine-add-on-7.png 266 200 'Slim version with GPIO headers at the side' %}](../../../../../images/temperature-machine-add-on-7.png)



## Start Logging Automatically

There are different ways to start software automatically after a reboot. I chose to add the following to `/etc/rc.local` on the server.

    su pi -c 'cd /home/pi/code/temperature-machine && ./start-server.sh garage bedroom &'

and the following to the client.

    su pi -c 'cd /home/pi/code/temperature-machine && ./start-client.sh &'


It will run the startup scripts as the user `pi` and assumes you've cloned the code as above (to `/home/pi/code/temperature-machine`). After rebooting, you should see a log file and `pid` file in the same location.

To stop, just run the `stop.sh` script.


## Do Not Disturb

If you're monitoring temperatures in a bedroom, you might not want to be disturbed by the LEDs. To switch the Pi Zero LED off, see the [Raspberry Pi Forum](https://www.raspberrypi.org/forums/viewtopic.php?f=29&t=127336) and [Stack Overflow](http://raspberrypi.stackexchange.com/questions/40559/disable-leds-pi-zero?noredirect=1#comment57599_40559) and to switch an Edimax EW-7811 LED off, see my [previous post]({{ root_url }}/blog/2016/01/06/disable-led-for-edimax/).