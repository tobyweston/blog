---
layout: post
title: "Vintage AirPlay Speakers"
date: 2016-01-20 19:01
comments: true
categories: 
sidebar: false
published: false
keywords: ""
description: ""
---


<!-- more -->

## Shopping List

| Item | Supplier | Price |
|--------------------------------------------------------------------------------|----------------------------------------|
| Roberts R66 Radio     | eBay   | £ 20
| IQaudIO [Pi-DigiAMP+](http://www.iqaudio.co.uk/home/9-pi-digiamp-0712411999650.html)      | £ 59.50 (inc. delivery) |
| 19W Power Supply | [RS Online](http://uk.rs-online.com/web/p/desktop-power-supply/7316074/) [Data sheet](http://docs-europe.electrocomponents.com/webdocs/0f8a/0900766b80f8a1bb.pdf) or [Farnell](http://uk.farnell.com/xp-power/vef65us19/power-supply-65w-19v-3-42a/dp/2365126) [Data sheet](http://www.farnell.com/datasheets/1766195.pdf)|
| Techtonic [Balanced Mode Radiator 20W Speaker Drivers](http://www.tectonicelements.com/bmr-speakers/) x2 | [RS Online](http://uk.rs-online.com/web/p/speaker-drivers/8765241/) | £ 35.72
| Rasperry Pi Zero | PiHut | £ 4
| 2.5 x 5.5mm [female DC socket](http://www.maplin.co.uk/p/25-x-55mm-single-hole-fixing-dc-socket-jk10l) and [male plug](http://www.maplin.co.uk/p/maplin-25-x-55mm-dc-power-plug-hh62s) | Maplin | £ 4.28
| 2 Core wire for DC power | |
| | |
| | |
| | &nbsp;
| **Total** | **£ 123.50**


## Software

Building [Shareport Sync](https://github.com/mikebrady/shairport-sync)

    $ apt-get install build-essential git
    $ apt-get install autoconf automake libtool libdaemon-dev libasound2-dev libpopt-dev libconfig-dev
    $ apt-get install avahi-daemon libavahi-client-dev
    $ apt-get install libssl-dev
    $ apt-get install libsoxr-dev

    $ git clone https://github.com/mikebrady/shairport-sync.git

    $ autoreconf -i -f


Disable the standard sound card. Supposed to be able to comment it out in `/etc/modules` but mine was empty.`

    pi@radio:/etc $ sudo nano /etc/modprobe.d/raspi-blacklist.conf
    pi@radio:/etc $ lsmod
    Module                  Size  Used by
    cfg80211              477515  0
    rfkill                 21439  2 cfg80211
    8192cu                567860  0
    snd_bcm2835            22317  0
    bcm2835_gpiomem         3703  0
    bcm2835_rng             2215  0
    snd_pcm                92397  1 snd_bcm2835
    snd_timer              21932  1 snd_pcm
    snd                    66988  3 snd_bcm2835,snd_timer,snd_pcm
    uio_pdrv_genirq         3550  0
    uio                    10002  1 uio_pdrv_genirq
    i2c_dev                 6406  0
    fuse                   85816  1
    ipv6                  354610  26

    pi@radio:/etc $ aplay -l
    **** List of PLAYBACK Hardware Devices ****
    card 0: ALSA [bcm2835 ALSA], device 0: bcm2835 ALSA [bcm2835 ALSA]
      Subdevices: 8/8
      Subdevice #0: subdevice #0
      Subdevice #1: subdevice #1
      Subdevice #2: subdevice #2
      Subdevice #3: subdevice #3
      Subdevice #4: subdevice #4
      Subdevice #5: subdevice #5
      Subdevice #6: subdevice #6
      Subdevice #7: subdevice #7
    card 0: ALSA [bcm2835 ALSA], device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

after adding to `/etc/modprob.d/raspi-blacklist.conf`;

    blacklist snd_bcm2835

    pi@radio:~ $ lsmod
    Module                  Size  Used by
    cfg80211              477515  0
    rfkill                 21439  2 cfg80211
    snd_soc_pcm512x_i2c     2570  0
    snd_soc_pcm512x        18073  1 snd_soc_pcm512x_i2c
    regmap_i2c              3346  1 snd_soc_pcm512x_i2c
    8192cu                567860  0
    snd_soc_bcm2708_i2s     7566  0
    regmap_mmio             3556  1 snd_soc_bcm2708_i2s
    snd_soc_iqaudio_dac     3003  0
    snd_soc_core          167798  3 snd_soc_pcm512x,snd_soc_iqaudio_dac,snd_soc_bcm2708_i2s
    snd_compress            8813  1 snd_soc_core
    snd_pcm_dmaengine       5778  1 snd_soc_core
    snd_pcm                92397  4 snd_soc_pcm512x,snd_soc_core,snd_soc_iqaudio_dac,snd_pcm_dmaengine
    snd_timer              21932  1 snd_pcm
    snd                    66988  4 snd_soc_core,snd_timer,snd_pcm,snd_compress
    i2c_bcm2708             6068  0
    bcm2835_gpiomem         3703  0
    bcm2835_rng             2215  0
    uio_pdrv_genirq         3550  0
    uio                    10002  1 uio_pdrv_genirq
    i2c_dev                 6406  0
    fuse                   85816  1
    ipv6                  354610  26

    pi@radio:~ $ aplay -l
    aplay: device_list:268: no soundcards found...

then

(dont do this)

    blacklist snd_soc_bcm2708_i2s


    Module                  Size  Used by
    cfg80211              477515  0
    rfkill                 21439  2 cfg80211
    snd_soc_pcm512x_i2c     2570  0
    snd_soc_pcm512x        18073  1 snd_soc_pcm512x_i2c
    regmap_i2c              3346  1 snd_soc_pcm512x_i2c
    8192cu                567860  0
    snd_soc_iqaudio_dac     3003  0
    snd_soc_core          167798  2 snd_soc_pcm512x,snd_soc_iqaudio_dac
    snd_compress            8813  1 snd_soc_core
    snd_pcm_dmaengine       5778  1 snd_soc_core
    snd_pcm                92397  4 snd_soc_pcm512x,snd_soc_core,snd_soc_iqaudio_dac,snd_pcm_dmaengine
    snd_timer              21932  1 snd_pcm
    snd                    66988  4 snd_soc_core,snd_timer,snd_pcm,snd_compress
    i2c_bcm2708             6068  0
    bcm2835_gpiomem         3703  0
    bcm2835_rng             2215  0
    uio_pdrv_genirq         3550  0
    uio                    10002  1 uio_pdrv_genirq
    i2c_dev                 6406  0
    fuse                   85816  1
    ipv6                  354610  26


    pi@radio:~ $ aplay -l
    **** List of PLAYBACK Hardware Devices ****
    card 0: IQaudIODAC [IQaudIODAC], device 0: IQaudIO DAC HiFi pcm512x-hifi-0 []
      Subdevices: 1/1
      Subdevice #0: subdevice #0