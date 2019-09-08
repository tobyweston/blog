---
layout: post
title: "Creating Debian Repositories"
series: Deploying to Debian
date: 2019-09-03 09:06
comments: true
categories: 
sidebar: false
published: false
keywords: "java, scala, debian, debian repositories, aptly, ubuntu"
description: "Create your own Debian repository for deploying your Java / Scala apps"
---

In this post, we'll look at to how to setup your own [debian repository](https://wiki.debian.org/DebianRepository) so users can install and upgrade your software via `apt-get` on popular Linux distros like Debian and Ubuntu.

<!-- more -->

## Approach

The basic approach:

1. Create a `.deb` package (see the [previous post]({{ root_url }}/blog/2019/09/02/deploy-java-to-debian) for doing so with Java/Scala and `sbt`)
1. Use `aptly` to create a manage your own debian repository, serving your packages over HTTP
1. Tell your customers where your repository is hosted
1. Profit


### Debian Repository Format

## `aptly`

## Users Setup `apt` 

