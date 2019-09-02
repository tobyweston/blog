---
layout: post
title: "Deploy Java on Debian"
date: 2019-09-02 09:06
comments: true
categories: 
sidebar: false
published: false
keywords: "java, scala, debian, debian repositories, aptly, ubuntu"
description: "Level up the way you distribute your Java/Scala/Kotlin applications by packaging them as .deb files and deploying via apt."
---

Level up the way you distribute your Java/Scala/Kotlin applications by packaging them as `.deb` files and deploying via `apt`. In this post, we'll look at how setup your own [debian repository](https://wiki.debian.org/DebianRepository) so users can install and upgrade your software via `apt-get` to popular Linux distros like Debian and Ubuntu.

<!-- more -->

## Approach

The basic approach:

1. Create a `.deb` package using `sbt` and the excellent `sbt-native-packager`
1. Use `aptly` to create a manage your own debian repository which you serve over HTTP
1. Tell your customers where your repository is hosted
1. Profit

## Packaging 

The [`sbt-native-packager`](https://www.scala-sbt.org/sbt-native-packager/index.html) plugin can create platform specific distributions for any `sbt` project. It can create a simple zip bundle with your application in (the `universal` package), tarballs, rpms, Mac dmgs, Windows MSIs, Docker images and, the one we're interested in, `.deb` files. Debian and derivatives like Ubuntu use this package format with `dpkg` and `apt` as the standard way to install and manage software. If you want to make it easy for Linux user's to get hold of your software, this is the way to do it.

## Deploying Debian Repository

## Setup `apt` 

## Extras

To slightly elaborate the procedure, you can use `sbt-assembly` to create a "fat" jar and `proguard` to shrink the resulting file (Scala will seriously bloat your jar) and generate `man` pages for that pro feel (hint: use `ronn` and `rdiscount`).

Thanks and appreciation to [@muuki88](https://github.com/muuki88) and others for `sbt-native-manager`, it's a seriously useful piece of software.