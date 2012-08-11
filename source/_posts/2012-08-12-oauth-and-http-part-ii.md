---
layout: post
title: "FreeAgent, OAuth &amp; HTTP (Part II)"
series: FreeAgent OAuth
date: 2012-08-12 11:13
comments: true
categories: java
sidebar: false
published: false
description: ""
keywords: "FreeAgent, OAuth, OAuth and FreeAgent"
---

In the [previous post]({{ root_url }}/blog/2012/08/11/oauth-and-http-part-i), we walked through requesting authorisation using OAuth and FreeAgent as our example. In this next post, we'll look at the next steps, requesting an access token and actually making client API calls to our target application.

We're using [FreeAgent API](https://dev.freeagent.com/docs/oauth) as our example.

<!-- more -->

## After Authorisation

Once you've got the _authorisation code_ but before actually being able to access target resources, you need to exchange the code for an _access token_. If you don't know what I'm talking about, refer back to the [previous post]({{ root_url }}/blog/2012/08/11/oauth-and-http-part-i). This is done in the form of a HTTPS `POST` to the (access) _token endpoint_. The request should give you back a _temporary_ token which is required in _every subsequent_ request to the target resources. At which point, the token should be supplied in the `Authorization` header.

    Authorization: Bearer 1GwfYDOaz_rG35SSgf8y8aBUasP5QrG9FSasfiD13

## Access Token Request

The HTTPS `POST` for FreeAgent requires [basic auth](http://en.wikipedia.org/wiki/Basic_access_authentication) using _client id_ and _client secret_ as username and password. That means supplying a `Authorization` header with base 64 encoded username and password, separated by a colon. So,

    client_id:client_secret

Should be encoded and sent over in the header, it'll look something like this.

    Authorization: Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=

The `POST` body should include the following [x-www-form-urlencoded](/blog/2012/06/11/http-encoding-schemes) parameters.

 * `grant_type=authorization_code`
 * `code=`<the authorisation code (see [previous post]({{ root_url }}/blog/2012/08/11/oauth-and-http-part-i))>
 * `redirect_uri=<your redirect URI>`

The request should also include an Accept header of application/xml or application/json.

FreeAgent differs from a lot of other OAuth implementations where the information is pass along as query parameters to a `GET`.

### The Request

So, an example request would look like this.

    POST /v2/token_endpoint HTTP/1.1
    Authorization: Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=
    Accept: application/json
    Content-Type: application/x-www-form-urlencoded
    User-Agent: Java/1.6.0_33
    Host: api.freeagent.com
    Connection: close
    Content-Length: 127

    grant_type=authorization_code&code=19P34sFZRwAsXjd7SLOE1ddsaX84jfjoCgix&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Foauth


### The Response

Which should give back the response below

    HTTP/1.1 200 OK
    Server: nginx/1.0.14
    Date: Sat, 11 Aug 2012 17:35:19 GMT
    Content-Type: application/json;charset=UTF-8
    Transfer-Encoding: chunked
    Connection: close
    Status: 200 OK
    Cache-Control: no-store
    Pragma: no-cache
    ETag: "6eabf5cd4b391a5d7e6e0ded90e73d7b"
    X-UA-Compatible: IE=Edge,chrome=1
    X-Runtime: 0.283021
    X-Rev: 9301db5
    X-Host: web4

    {
       "access_token":"1GwfYDOaz_rG352X-gf88aBUasP5QrG9FSasfiD13",
       "token_type":"bearer",
       "expires_in":604800,
       "refresh_token":"2sdf35SFdisaa1g-x1-MaBsdHsdO7ssgZfsSRhUVsjU"
    }


## Extract the Access Token

What's left to do? Extract the token returned in the response above and pass it through on every subsequent request.

## Google's OAuth Playground

Useless.