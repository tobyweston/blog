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

Sometimes refered to as [Percent Encoding](http://en.wikipedia.org/wiki/Percent-encoding), this scheme is intended to encode non-ASCII characters consistently in URLs. For example, characters like `#` have special meaning in a URL. The scheme is recognisable by the replacement of characters with a percentage value. For example, the space character gets replaced by `%20`.

You can create an encoded URL using new `java.netURI("http", "baddotrobot.com", "/cheese sandwich").toURL();` which in this case produces `http:baddotrobot.com#/cheese%20sandwich`.

## Form URL Encoding

Refered to by the `application/x-www-form-urlencoded` mime-type. This scheme was based on an early version of URL Encoding but at some point diverged. For example, the space character gets replaced by the `+` rather than `%20`. It's typically used for encoding `POST` message content by HTML forms.

Use `java.net.URLEncoder.encode(value, "UTF-8");` to encode `value` using this scheme`.

For example, a HTML form with `name` and `address` would be encoded such.

    Example (are parameter key's encoded?)

## Base64 Encoding

Another one to be aware of, this is a basic encoding used by various protocols related to HTTP. For example, basic authentication is supporting by adding a [Authorization](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.8) header with base 64 encoded username and password; you'd do something like the following.

	new header("Authorization", "Basic " + new sun.misc.Base64Encoder().encode(("username:password").getBytes()));

For example, sending the following HTTP message

	GET /login HTTP/1.1
	Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
	