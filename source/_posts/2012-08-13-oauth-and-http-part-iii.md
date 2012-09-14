---
layout: post
title: "FreeAgent, OAuth &amp; HTTP (Part III)"
series: FreeAgent OAuth
date: 2012-08-13 19:13
comments: true
categories: java
sidebar: false
published: false
description: "Caveats access the FreeAgent API using OAuth"
keywords: "FreeAgent, OAuth, OAuth and FreeAgent, tutorial, scribe, java, google oauth"
---

In previous posts, we looked at setting up authentication with OAuth to access FreeAgent's API. We've got something working but a couple of caveats remain when working with it from a rich client.

<!-- more -->

## The Workflow

To summarise the workflow;

 1. Ask your user to authorise your application (on the target application's servers).
 1. You'll be given an _authorisation token_ from the above. Stash it.
 1. Exchange your _authorisation token_ for an _access token_. Stash this too (along with the _refresh token_).
 1. Make requests passing along the _access token_ to prove you're you.


## The Authorisation Request

It's not always clear, but step 1. above is a one time operation. You don't make this request every time your programmatically want to access the target application. It also implies that the `GET` request is made from the browser. There are "out of band" options but in-browser is the simplest.


## The Access Token Request

Again, it's not always clear but the _access token_ request only needs to be made once. In fact, if you've successfully retrieved an _access token_ and then request a new one, FreeAgent will error with a basic authentication failure.

    HTTP/1.1 401 Unauthorized
    Server: nginx/1.0.14
    Date: Mon, 13 Aug 2012 18:13:44 GMT
    Content-Type: text/html; charset=utf-8
    Status: 401 Unauthorized
    WWW-Authenticate: Basic realm="Application"
    X-UA-Compatible: IE=Edge,chrome=1
    X-Runtime: 0.099212
    X-Rev: 9301db5
    X-Host: web3

    HTTP Basic: Access denied.

I think it's trying to say that your application isn't allowed to request a new access token whilst one is already valid.

## Refreshing the Access Token

