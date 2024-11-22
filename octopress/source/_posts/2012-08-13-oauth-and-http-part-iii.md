---
layout: post
title: "FreeAgent, OAuth &amp; HTTP (Part III)"
series: FreeAgent OAuth
pubDate: 2012-08-13 19:13
comments: true
categories: java
sidebar: false
published: true
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

In a successful exchange of _authorisation code_ for _access token_, you should see a response like this.

``` js
{
    "access_token":"2YotasFasFzCXcCsMWp1",
    "token_type":"bearer",
    "expires_in":604800,
    "refresh_token":"1Gzv0XG5Qx2T3JOkFlKWyj"
}
```
In OAuth, The `expires_in` value should be the time in seconds that the _access token_ is valid.

{% blockquote OAuth 2.0 Specification https://tools.ietf.org/html/draft-ietf-oauth-v2-26#section-4.2.2 %}
RECOMMENDED. The lifetime in seconds of the access token. For example, the value "3600" denotes that the access token will expire in one hour from the time the response was generated. If omitted, the authorization server SHOULD provide the expiration time via other means or document the default value.
{% endblockquote %}

FreeAgent return `604800` which is consistent with their documentation as it works out as 7 days. As this countdown starts when you exchange the tokens, I convert the number into a concrete date when I get the response. That way, I can see later if I actually need to refresh the token. However, it seems that you can refresh your token at any point.

The process is similar to the [requesting the original _access token_]({{ root_url }}/blog/2012/08/12/oauth-and-http-part-ii). Make a Basic auth HTTP POST but with a slightly smaller body.

    POST /v2/token_endpoint HTTP/1.1
    Authorization: Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=
    Accept: application/json
    Content-Type: application/x-www-form-urlencoded
    User-Agent: Java/1.6.0_33
    Host: api.freeagent.com
    Connection: close
    Content-Length: 127

    grant_type=refresh_token&refresh_token=12wXjd7SL7SLOE1sdsaX8oCgix


which will return something like

``` js
{
    "access_token":"2YotasFasFzCXcCsMWp1",
    "token_type":"bearer",
    "expires_in":604800
}
```