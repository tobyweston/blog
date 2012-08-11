---
layout: post
title: "OAuth &amp; HTTP (Part II)"
series: OAuth &amp; Desktop Applications
date: 2012-08-12 11:13
comments: true
categories: java
sidebar: false
published: false
description: ""
keywords: "FreeAgent, OAuth, OAuth and FreeAgent"
---

In the [previous post]({{ root_url }}/blog/2012/08/11/oauth-and-http-part-i), we walked through requesting authorisation using OAuth and FreeAgent as our example. In this next post, we'll look at the next steps, requesting an access token and actually making client API calls to our target application.

<!-- more -->

## Access Token Request

Once you've got the _authorisation code_ but before actually being able to access target resources, you need to exchange the code for an _access token_. This is done in the form of a HTTPS `POST` to the (access) _token endpoint_. The request should give you back a _temporary_ token which is required in _every subsequent_ request to the target resources. The token should be supplied in the `Authorization` header.

    Authorization: Bearer TOKEN


## Google's OAuth Playground

Useless.