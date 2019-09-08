---
layout: post
title: "Easily Deploy Java to Debian"
series: Deploying to Debian
date: 2019-09-02 09:06
comments: true
categories: 
sidebar: false
published: true
keywords: "java, scala, debian, debian repositories, aptly, ubuntu"
description: "Level up the way you distribute your Java/Scala/Kotlin applications by packaging them as .deb files and deploying via apt."
---

Level up the way you distribute your Java/Scala/Kotlin applications by packaging them as `.deb` files and deploying via `apt`. 

<!-- more -->

## Approach

The basic approach:

1. Create a `.deb` package using `sbt` and the excellent `sbt-native-packager`
1. Create your own Debian repository, add your packages and then serve them over HTTP
1. Tell your customers where your repository is hosted
1. Profit

This post looks at the first step, creating the `.deb` package using the `sbt-native-packager` plugin. In the [next post]({{ root_url }}/blog/2019/09/03/create-debian-repositories), we'll look at how setup your own [debian repository](https://wiki.debian.org/DebianRepository) so users can install and upgrade your software via `apt-get` to popular Linux distros like Debian and Ubuntu.

Thanks and appreciation to [@muuki88](https://github.com/muuki88) and the project maintainers for `sbt-native-manager`, it's a seriously useful piece of software. 


## Packaging 

The [`sbt-native-packager`](https://www.scala-sbt.org/sbt-native-packager/index.html) plugin can create platform specific distributions for any `sbt` project. It can create a simple zip bundle for your application (the `universal` package), tarballs, rpms, Mac dmgs, Windows MSIs, Docker images and, the one we're interested in, `.deb` files. Debian and derivatives like Ubuntu use this package format with `dpkg` and `apt` as the standard way to install and manage software. If you want to make it easy for Linux user's to get hold of your software, this is the way to do it.


### Native Packager Core Concepts

The native packager takes care of packaging, the act of putting a list of *mappings* (source file to install target path) into the chosen package format (zip, rpm, etc.). Each [packing format](https://www.scala-sbt.org/sbt-native-packager/formats/index.html) your use will expect the package specific files in a specific folder location in your source. For example, the Universal plugin will look in `src\universal` for files to add to the zip. Debian packaging will look for `src\debian`.


It uses [Project Arcetypes](https://www.scala-sbt.org/sbt-native-packager/archetypes/index.html) like the [Java CLI Application Archetype](https://www.scala-sbt.org/sbt-native-packager/archetypes/java_app/index.html) or [Java Server Application Archetype](https://www.scala-sbt.org/sbt-native-packager/archetypes/java_server/index.html) to add additional files to the mappings enriching the created package. They don’t provide any new features per se.


You'll need to read up a little on how to use the plugin, see [Debian specific instructions](https://www.scala-sbt.org/sbt-native-packager/formats/debian.html) but the core concepts include:

1. [Packaging format plugins](https://www.scala-sbt.org/sbt-native-packager/introduction.html#format-plugins) - _how_ an application is packaged; universal, linux, debian, rpm, docker, windows etc 
1. [Archetype plugins](https://www.scala-sbt.org/sbt-native-packager/introduction.html#archetype-plugins) - _what's_ packaged (predefined configurations); java application, java server application, system loaders etc
1. [Mappings](https://www.scala-sbt.org/sbt-native-packager/introduction.html#mappings) map source files to target system locations


### Running as a Service

One of the many awesome features of the packager is that it can set your application up as a service on the target system. For example, if you want to start your application using `systemd`, just add a `enablePlugins(SystemdPlugin)` line to your build. The OS will take care of everything else, even restarting your application should it crash.

The native packagers doesn't provide application lifecyle management however. Custom start/stop scripts, PID management, etc. are not part of native packager.

### Extras

For some additional nice to haves, you might consider adding `man` pages (with `ronn`), creating a "fat" JAR (with [`sbt-assembly`](https://github.com/sbt/sbt-assembly) plugin) and stripping unused Scala library classes with ProGuard.

## Deploying Debian Repository

The native packager doesn't take care of deployment. You use it to create your `.deb` package but what you do with it is down to you. The obvious choice is to deploy it to a Debian repository for your users to download via `apt`. Read the [next post]({{ root_url }}/blog/2019/09/03/create-debian-repositories) to find out how.
