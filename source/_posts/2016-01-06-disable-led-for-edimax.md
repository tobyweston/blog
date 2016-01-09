---
layout: post
title: "Disable LED for Edimax"
date: 2016-01-06 19:39
comments: true
categories: 
sidebar: false
published: false
keywords: "8192cu, edimax, rasperry pi, pi zero, EW-7811"
description: ""
---

Find out how to disable the LED on the Edimax EW-7811UN USB wireless adapter.

<!-- more -->

## How

The only way I found to disable the LED is to patch the actual [kernel module](https://en.wikibooks.org/wiki/The_Linux_Kernel/Modules). That means changing the source and recompiling everything.


## Instructions

### Background

You'll need to know the specific kernel version. Run the following.

    $ uname -a

It'll show something like this

    Linux raspberrypi 4.1.13+ #826 PREEMPT Fri Nov 13 20:13:22 GMT 2015 armv6l GNU/Linux


The Edimax uses the `8192cu` module. You can check it's loaded with `lsmod`. You'll see something like this.

    $ lsmod
    Module                  Size  Used by
    cfg80211              499834  0
    rfkill                 22491  2 cfg80211
    8192cu                569532  0
    ...

and you can get more information with `modinfo 8192cu`. Make a note of some the details:

    filename:       /lib/modules/4.1.13+/kernel/drivers/net/wireless/rtl8192cu/8192cu.ko
    version:        v4.0.2_9000.20130911
    author:         Realtek Semiconductor Corp.
    description:    Realtek Wireless Lan Driver
    license:        GPL
    srcversion:     133EACDEB0C6BEBC3ECA8D0
    vermagic:       4.1.13+ preempt mod_unload modversions ARMv6
    ...


### Get the Source

You need the module source to be able to modify and compile. It might take some googling but for `v4.0.2_9000` it can be found on the [Realtek site](http://218.210.127.131/downloads/downloadsView.aspx?Langid=1&PNid=21&PFid=48&Level=5&Conn=4&DownTypeID=3&GetDown=false&Downloads=true#2772). Check carefully the module name (8192CU) and kernel version matches the output of `uname -a`.

On the Pi, download the bundle:

    wget -O 0001-RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911.zip http://12244.wpc.azureedge.net/8012244/drivers/rtdrivers/cn/wlan/0001-RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911.zip


Once downloaded, extract with `unzip *.zip` then `cd` into the resulting folder then;

    cd driver

You should see a tarball such as `rtl8188C_8192C_usb_linux_v4.0.2_9000.20130911.tar.gz`. Extract that.

    tar -xvf *.tar.gz


## Modify the Makefile

Locate the `autoconf.h` file and comment out the following `CONFIG_LED` macro definition. It should look like this.

    // #define CONFIG_LED
    #ifdef CONFIG_LED
        #define CONFIG_SW_LED
        #ifdef CONFIG_SW_LED
            //#define CONFIG_LED_HANDLED_BY_CMD_THREAD
        #endif
    #endif // CONFIG_LED


## Compile

Before you can compile the driver using `make`, you need to make sure you have all it's dependencies and you Pi has the various tools needed to build stuff.

Get the basic build tools with the following command.

    $ sudo apt-get install build-essential

Ordinarily, you'd also `apt-get install linux-headers-$(uname -r)` to get the headers but the maintainers for the Raspberry Pi linux distribution don't make them like this. Instead, we need to get the full kernel source from the [Pi Foundation's Github repository](https://github.com/raspberrypi/linux).

The latest source may not match your kernel version. You can check in the `Makefile`;

    VERSION = 4
    PATCHLEVEL = 1
    SUBLEVEL = 15
    ...

This is version `4.1.15` whereas my version (`uname -r`) is `4.1.13`. Major versions are stored as branches in the repository so you can `git checkout branch` but if like me, you version is a minor level, you have to scan the commits from the appropriate branch. For example, [4.1.13](https://github.com/raspberrypi/linux/commit/1f2ce4a2e7aea3a2123b17aff62a80553df31e21) and [4.1.12](https://github.com/raspberrypi/linux/commit/10f9e3bce7f3ab7ab4d09a9b78c7208c9a1455f7) were documented by [Greg Kroah-Hartman](https://github.com/gregkh) in the commit messages.


## Manually Install the Headers

Getting the full kernel source from Git gives you the required headers. You just need to sym-link to the expected location before you try and compile the driver.

You'll also need the kernel config settings which should be in `/proc/config.gz` on the Pi, if the file doesn't exist, try running `sudo modprobe configs`.

So, perform the following.

    git clone --branch=rpi-4.1.y https://github.com/raspberrypi/linux.git
    ln -s linux linux-$(uname -r)

    cd linux
    git checkout 1f2ce4a2   # the SHA of your specific version, this is 4.1.13
    zcat /proc/config.gz > .config
    ln -s /usr/src/linux /lib/modules/$(uname -r)/build


The `git clone` command will checkout (download) the full source. Create a sym-link for yourself then change into the downloaded location. The `checkout SHA` line will roll back the current source to match the specific version you're interested in. Find your SHA in the commit messages as mentioned above.

The `zcat` command will create you a `.config` file containing the current kernel configuration which we'll need when building stuff later. The last line is to create the folder that compilation requires. It's what fixes the infamous error;

    make[1]: *** /lib/modules/4.1.13+/build: No such file or directory


## Compile the Kernel

This isn't as scary as it sounds. We need to compile the actual kernel source. Not to install but just to create various generated dependencies that we'll need when compiling the driver. For example, compiling the driver would fail with missing files like   `include/generated/autoconf.h` or `include/config/auto.conf`.


Before compiling the kernel, get some extra dependencies

    $ sudo apt-get install libncurses5-dev      # required for menuconfig
    $ sudo apt-get install bc                   # required for timeconst.h


You can have a go at running just `make` at this point but various options need to be set and it's probably easier to use `menuconfig`. Make sure you created the `.config` from earlier then run the following.

    $ make menuconfig

Scan the options but as they're based on your current settings, you should just be able to quit (`ESC`, `ESC`) and something like the following will be output.

      HOSTCC  scripts/kconfig/mconf.o
      HOSTCC  scripts/kconfig/zconf.tab.o
      HOSTCC  scripts/kconfig/lxdialog/checklist.o
      HOSTCC  scripts/kconfig/lxdialog/util.o
      HOSTCC  scripts/kconfig/lxdialog/inputbox.o
      HOSTCC  scripts/kconfig/lxdialog/textbox.o
      HOSTCC  scripts/kconfig/lxdialog/yesno.o
      HOSTCC  scripts/kconfig/lxdialog/menubox.o
      HOSTLD  scripts/kconfig/mconf
    scripts/kconfig/mconf  Kconfig
    configuration written to .config

    *** End of the configuration.
    *** Execute 'make' to start the build or try 'make help'.


The last remaining config files will have now been created, so you can do the actual build with;

    make ARCH=arm


For exatra background, I found an interesting guide on Stack Exchange about [Configuring, Compiling and Installing Kernels](http://unix.stackexchange.com/questions/115620/configuring-compiling-and-installing-a-custom-linux-kernel/115621#115621.) although we're not going as far as installing the built kernel.


## Compile the Driver

The dependencies should all be available now, so you're ready to compile the driver. Compile from the location of the extracted driver tarball. For me, it was `RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911/driver/rtl8188C_8192C_usb_linux_v4.0.2_9000.20130911`

    $ cd driver
    $ make ARCH=arm

You can expect a bunch of problems though;

 * No headers
 * No armv6l folder
 *



## No Header


## No `armv6l` folder

    cd /usr/src/linux-rpi-3.6.y/arch/
    sudo ln -s arm armv6l

or

    make ARCH=arm


## No auto.cofig

    make ARCH=armv6l CROSS_COMPILE= -C /lib/modules/4.1.13+/build M=/home/pi/code/edimax_driver/RTL8188C_8192C_USB_linux_v4.0.2_9000.20130911/driver/rtl8188C_8192C_usb_linux_v4.0.2_9000.20130911  modules
    make[1]: Entering directory '/home/pi/code/rpi-linux-1f2ce4a'

      ERROR: Kernel configuration is invalid.
             include/generated/autoconf.h or include/config/auto.conf are missing.
             Run 'make oldconfig && make prepare' on kernel src to fix it.


      WARNING: Symbol version dump ./Module.symvers
               is missing; modules will have no dependencies and modversions.

      Building modules, stage 2.
    scripts/Makefile.modpost:42: include/config/auto.conf: No such file or directory
    make[2]: *** No rule to make target 'include/config/auto.conf'.  Stop.
    Makefile:1387: recipe for target 'modules' failed
    make[1]: *** [modules] Error 2
    make[1]: Leaving directory '/home/pi/code/rpi-linux-1f2ce4a'
    Makefile:584: recipe for target 'modules' failed
    make: *** [modules] Error 2


## References

* Based on this [forum post](https://www.raspberrypi.org/forums/viewtopic.php?t=11162).
* [Good post](http://lostindetails.com/blog/post/Compiling-a-kernel-module-for-the-raspberry-pi-2)
* [Compiling-a-kernel-module-for-the-raspberry-pi](http://lostindetails.com/blog/post/Compiling-a-kernel-module-for-the-raspberry-pi-2)


