---
layout: post
title: "HTTP Encoding Schemes"
date: 2012-06-11 18:06
comments: true
categories: java REST
sidebar: false
published: false
---

## URL Encoding

Sometimes refered to as [Percent Encoding](http://en.wikipedia.org/wiki/Percent-encoding), this scheme is intended for use with URLs. This is recognisable by the replacement of characters with a percentage value. For example, the space character gets replaced by `%20`.

## Form URL Encoding

Refered to by the `application/x-www-form-urlencoded` mime-type. This scheme was based on an early version of URL Encoding but at some point diverged. For example, the space character gets replaced by the `+` rather than `%20`. This is the scheme HTML forms with use with a submit type of `POST`.

## Java Encoding