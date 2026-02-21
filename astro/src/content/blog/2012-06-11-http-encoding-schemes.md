---
title: "HTTP Encoding Schemes"
pubDate: '2012-06-11'
categories: 'web'
keywords: "URL encoding, percent encoding, form encoding, x-www-form-urlencoded, Java URL encode, HTTP encoding"
description: "Understand the difference between URL encoding and form encoding (x-www-form-urlencoded) and how to correctly encode HTTP request parameters in Java."
---

What's the difference between URL Encoding and Form URL Encoding?


## URL Encoding

Sometimes referred to as [Percent Encoding](http://en.wikipedia.org/wiki/Percent-encoding), this scheme is intended to encode non-ASCII characters consistently in URLs. For example, characters like `#` have special meaning in a URL and would need to be converted to avoid problems. The scheme is recognisable by the replacement of characters with a percentage value. For example, the space character gets replaced by `%20`.

In Java, you can create an encoded URL using

``` java
new java.net.URI("http", "baddotrobot.com", "/cheese sandwich").toURL();
```

which in this case produces

    http:baddotrobot.com#/cheese%20sandwich

## Form URL Encoding

Refered to by the `application/x-www-form-urlencoded` mime-type. This scheme was based on an early version of URL Encoding but at some point diverged. For example, the space character gets replaced by the `+` rather than `%20`. It's typically used for encoding `POST` message content by HTML forms.

For example, a HTML form with `name` and `address` would send over the following.

    POST http://baddotrobot.com/ HTTP/1.1
    Content-Type: application/x-www-form-urlencoded

    name=bad.robot&address=the+land+of+make+believe

Use the unhelpfully named class `URLEncoder` in Java

``` java
java.net.URLEncoder.encode(value, "UTF-8");
```




## Base64 Encoding

Another one to be aware of, this is a basic encoding used by various protocols related to HTTP. For example, basic authentication is supported by adding a [Authorization](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.8) header with base 64 encoded username and password; you'd do something like the following.

``` java
new header("Authorization", "Basic " + new sun.misc.Base64Encoder().encode("username:password".getBytes()));
```
Which, for example, could be used to send the following HTTP message

	GET /login HTTP/1.1
	Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
	