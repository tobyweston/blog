---
layout: post
title: "HTTP Encoding Schemes"
date: 2012-06-11 18:06
comments: true
categories: java REST
sidebar: false
published: false
description: "Find out the difference between URL Encoding and Form URL Encoding and how to encode to both schemes in Java"
keywords: "URL vs form encoding, URL encoding in Java, URL form encoding, percent encoding, x-www-form-urlencoded"
---

What's the difference between URL Encoding and Form URL Encoding?

## URL Encoding

Sometimes refered to as [Percent Encoding](http://en.wikipedia.org/wiki/Percent-encoding), this scheme is intended for use with URLs. This is recognisable by the replacement of characters with a percentage value. For example, the space character gets replaced by `%20`.

You can create an encoded URL using new `java.netURI("http", "baddotrobot.com", "/cheese sandwich").toURL();` which in this case produces `http:baddotrobot.com#/cheese%20sandwich`.

## Form URL Encoding

Refered to by the `application/x-www-form-urlencoded` mime-type. This scheme was based on an early version of URL Encoding but at some point diverged. For example, the space character gets replaced by the `+` rather than `%20`. This is the scheme HTML forms with use with a submit type of `POST`.

Use `java.net.URLEncoder.encode(value, "UTF-8");` to encode `value` using this scheme`.

For example, a HTML form with `name` and `address` would be encoded such.

    Example (are parameter key's encoded?)

## Base64 Encoding

Another one to be aware of, this is a basic encoding ...

For example, adding a basic auth header, you'd use something like the following.

	new header("AUTHORIZATION", "Basic " + new Base64Encoder().encode((userName + ":" + password).getBytes()));