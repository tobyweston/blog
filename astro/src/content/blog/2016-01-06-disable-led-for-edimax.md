---
title: "Disable Edimax Wifi Dongles LED"
pubDate: "2016-01-06"
categories: 'pi'
keywords: "8192cu, edimax, rasperry pi, pi zero, EW-7811, EW-7811UN, pi"
description: "Instructions how to recompile the Raspberry Pi kernel and disable the Edimax EW-7811UN LED"
---

Pi specific instructions to disable the LED on the Edimax EW-7811UN USB wireless adapter.


The only way I found to disable the LED is by modifying the [kernel module](https://en.wikibooks.org/wiki/The_Linux_Kernel/Modules). Compiling that meant recompiling the associated kernel to get all the dependencies lined up. 

If you don"t want to have a go at compiling the kernel, you can always download the output of my efforts [here](http://robotooling.com/maven/bad/robot/temperature-machine/) (built against 4.9.17-v7+).


## Gather Information

You'll need to know the specific kernel version. Run the following.

```bash
$ uname -a
```

It'll show something like this

```bash
Linux raspberrypi 4.1.13+ #826 PREEMPT Fri Nov 13 20:13:22 GMT 2015 armv6l GNU/Linux
```

The Edimax uses the `8192cu` module. You can check it's loaded with `lsmod`. You'll see something like this.

```bash
$ lsmod
Module                  Size  Used by
cfg80211              499834  0
rfkill                 22491  2 cfg80211
8192cu                569532  0
...
```

For interest, you can get more information running `modinfo 8192cu`.

```bash
filename:       /lib/modules/4.1.13+/kernel/drivers/net/wireless/rtl8192cu/8192cu.ko
version:        v4.0.2_9000.20130911
author:         Realtek Semiconductor Corp.
description:    Realtek Wireless Lan Driver
license:        GPL
srcversion:     133EACDEB0C6BEBC3ECA8D0
vermagic:       4.1.13+ preempt mod_unload modversions ARMv6
...
```

## Get the Source

You need both the **module** and **kernel** source.

The latest driver version (`v4.0.2_9000`) on the [Realtek site](http://218.210.127.131/downloads/downloadsView.aspx?Langid=1&PNid=21&PFid=48&Level=5&Conn=4&DownTypeID=3&GetDown=false&Downloads=true#2772) isn't actually the latest version. At least, it's been modified for the Pi. The good news is that the modified version is bundled with the Pi kernel source at [https://github.com/raspberrypi/linux.git](https://github.com/raspberrypi/linux.git). On the Pi, run the following (matching your running kernel version with the `--branch` option).

```bash
$ git clone --branch=rpi-4.1.y --depth=50 https://github.com/raspberrypi/linux.git
$ ln -s linux linux-$(uname -r)
```

The `git clone` command will download the full source (including headers and all built-in drivers) into a new folder called `linux`. The symbolic link is just a handy reminder of what you've cloned.

The latest source may not match your running kernel version (`uname -r`). You can check in the `Makefile`;

```bash
VERSION = 4
PATCHLEVEL = 1
SUBLEVEL = 15
...
```

This is version `4.1.15` whereas my version was `4.1.13`. Major versions are stored as branches in the repository (hence the `--branch=rpi-4.1.y` option above) but if like me, your version is a minor level, you have to scan the commits from the appropriate branch. For example, [4.1.13](https://github.com/raspberrypi/linux/commit/1f2ce4a2e7aea3a2123b17aff62a80553df31e21) and [4.1.12](https://github.com/raspberrypi/linux/commit/10f9e3bce7f3ab7ab4d09a9b78c7208c9a1455f7) were documented by [Greg Kroah-Hartman](https://github.com/gregkh) in the commit messages. You could also try something `git log --oneline | grep "Linux 4.1.18"` to save manually scanning the logs.

The upshot is that you may need to roll back to the revision that is specifically for your kernel version. That's why I used `--depth=50` in the hope of catching the revision I'm interested in.

```bash
$ cd linux
$ git checkout 1f2ce4a2     # the SHA of your specific version, this is 4.1.13
```

## Manually Install the Headers

Compiling anything in Linux usually requires you have the kernel header files available. The usual way to get these is to run `apt-get install linux-headers-$(uname -r)` but the maintainers for the Raspberry Pi linux distribution don’t make them available like this. Instead, we have to rely on the full kernel source you've just downloaded.

Create a symbolic link to fill in for the missing `build` folder in `/lib/modules` before you try and compile the driver:

```bash
$ cd ..
$ ln -s linux /lib/modules/$(uname -r)/build
```

This creates the missing folder but points at the newly downloaded source. It's what fixes the infamous error;

```bash
make[1]: *** /lib/modules/4.1.13+/build: No such file or directory
```

## Setup your Config

Before we build the kernel, we need to create a `.config` file containing the current kernel configuration. The current config should be in the `/proc/config.gz` file on the Pi. If the file doesn't exist, run `sudo modprobe configs` and check again.

```bash
$ cd linux
$ zcat /proc/config.gz > .config
```


## Compile the Kernel

This isn't as scary as it sounds. We need to compile the kernel source. We're not going to install it, but we do want to create various dependencies that are needed to compile the driver. For example, compiling the driver would fail with missing files like   `include/generated/autoconf.h` or `include/config/auto.conf`. Compiling the entire kernel is probably a bit overkill but I've found it easier than chasing down individual errors.

Before compiling the kernel, get some extra dependencies

```bash
$ sudo apt-get install build-essential
$ sudo apt-get install libncurses5-dev      # required for menuconfig
$ sudo apt-get install bc                   # required for timeconst.h
```

You can have a go at running just `make` from the `linux` folder at this point but various options need to be set and it's probably easier to use `menuconfig`. Make sure you created the `.config` from earlier then run the following.

```bash
$ cd linux
$ make menuconfig
```

Scan the options but as they're based on your current settings (via `.config`), you should just be able to quit (`ESC`, `ESC`) and something like the following will be output.

```bash
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
```

The last remaining config files will have now been created, so you can do the actual build with;

```bash
make ARCH=arm
```

or as Avi P points out below if you're running on a multi-core Pi like the Pi 2 or Pi 3;

```bash
make -j4 ARCH=arm
```

This takes a while; on my Pi Zero, over 12 hours. There's always the option to [cross compile](https://www.raspberrypi.org/documentation/linux/kernel/building.md) if you're in a hurry.

For extra background, I found an interesting guide on Stack Exchange about [Configuring, Compiling and Installing Kernels](http://unix.stackexchange.com/questions/115620/configuring-compiling-and-installing-a-custom-linux-kernel/115621#115621.) (although we're not going as far as installing the built kernel here).


## Modify the Driver

This is the step that actually disables the LED on the dongle.

Locate the `autoconf.h` file in the drivers folder (`linux/drivers/net/wireless/rtl8192cu/include` or `linux/drivers/net/wireless/realtek/rtl8192cu/include` in newer linux versions) and comment out the `CONFIG_LED` macro definition. It should look like this when you're done.

```bash
// #define CONFIG_LED           // <-- comment this line out to disable LED
#ifdef CONFIG_LED
    #define CONFIG_SW_LED
    #ifdef CONFIG_SW_LED
        //#define CONFIG_LED_HANDLED_BY_CMD_THREAD
    #endif
#endif // CONFIG_LED
```

## Compile the Driver

The dependencies should all be available now, so you're ready to compile the driver. Compile from the location of driver source (probably `linux/drivers/net/wireless/rtl8192cu` or `linux/drivers/net/wireless/realtek/rtl8192cu`).

```bash
$ cd linux/drivers/net/wireless/realtek/rtl8192cu
$ make ARCH=arm
```

Again, use the `-j4` flag if you're on a big boy Pi.


## Test & Install the Driver

Once it's compiled, remove the old driver with `sudo rmmod 8192cu` and from the driver folder, manually startup the newly compiled one; `sudo insmod 8192cu.ko`. Note that you'll loose network connectivity after removing the old module. Make sure you've got a way to connect back to your Pi (like a [console cable](/blog/2015/12/28/pi-console-lead/)).

Running `modinfo 8192cu` doesn't help verify the new driver as none of the meta-data has changed but you can check the datestamp of the `.ko` and you should see that there's no LED flashing.


To keep the change, I renamed the patched module to `8192cu-no-led.ko` and copied it into the Pi's main kernel drivers folder. I renamed the original driver to `8192cu-original.ko` and created a symbolic link for the true module name `8192cu.ko`. This is because I want to be able to swtich back easily and not have to modify any additional configuration (for example, any `/etc/modprobe.d/8219cu.conf` settings) or black lists.

```bash
$ mv 8192cu.ko 8192cu-no-led.ko
$ sudo cp 8192cu-no-led.ko /lib/modules/4.1.13+/kernel/drivers/net/wireless/rtl8192cu/
$ cd /lib/modules/4.1.13+/kernel/drivers/net/wireless/rtl8192cu/
$ sudo mv 8192cu.ko 8192cu-original.ko
$ sudo ln -s 8192cu-no-led.ko 8192cu.ko
```

You should see something like this.

```bash
$ ll
total 1332
lrwxrwxrwx 1 root root     13 Jan 12 17:58 8192cu.ko -> 8192cu-no-led.ko
-rw-r--r-- 1 root root 672500 Jan 12 17:58 8192cu-no-led.ko
-rw-r--r-- 1 root root 686160 Nov 18 16:01 8192cu-original.ko
```

You can enable the original driver by reassigning the symbolic link.


## Common Problems

### No `armv6l` folder

```bash
$ cd linux/arch
$ sudo ln -s arm armv6l
```

or always run the following when compiling

```bash
make ARCH=arm
```

## No `build` folder

```bash
$ make[1]: *** /lib/modules/4.9.58+/build: No such file or directory.  Stop.
```

Create a sym

```bash
$ sudo ln -s /home/pi/code/linux build
```

The folder should look something like this.

```bash
$ ll
total 1.9M
drwxr-xr-x 11 root root 4.0K Oct 27 18:52 kernel
lrwxrwxrwx  1 root root   19 Oct 29 11:33 build -> /home/pi/code/linux
-rw-r--r--  1 root root 471K Oct 27 18:53 modules.alias
-rw-r--r--  1 root root 486K Oct 27 18:53 modules.alias.bin
-rw-r--r--  1 root root 4.7K Oct 27 18:52 modules.builtin
...
-rw-r--r--  1 root root 249K Oct 27 18:53 modules.symbols.bin
```

### Edimax Sleeps and Drops the Network

Setup some config in the `modprobe.d` folder.

```bash
$ cd /etc/modprobe.d/
$ ll
total 16
-rw-r--r-- 1 root root  73 Jan  1 19:45 8192cu.conf
$ cat 8192cu.conf
options 8192cu rtw_power_mgnt=0 rtw_enusbss=0
```
