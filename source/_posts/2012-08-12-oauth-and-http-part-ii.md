---
layout: post
title: "FreeAgent, OAuth &amp; HTTP (Part II)"
series: FreeAgent OAuth
date: 2012-08-12 11:13
comments: true
categories: java recipes
sidebar: false
description: "Retrieving the FreeAgent OAuth access token requires a basic auth POST request with a body with content previously retrieved. See the details here."
keywords: "FreeAgent, OAuth, OAuth and FreeAgent, tutorial, scribe, java, google oauth"
---

In the [previous post]({{ root_url }}/blog/2012/08/11/oauth-and-http-part-i), we walked through requesting "authorisation" from [FreeAgent](https://dev.freeagent.com/docs/oauth) using OAuth. In this next post, we'll look at the next steps, requesting an _access token_ and actually making client API calls to our target application.

## After Authorisation

Once you've got the _authorisation code_ but before actually being able to access target resources, you need to exchange the code for an _access token_. If you don't know what I'm talking about in terms of authorisation, refer back to the [previous post]({{ root_url }}/blog/2012/08/11/oauth-and-http-part-i). This is done in the form of a HTTPS `POST` to the (access) _token endpoint_. The request should give you back a _temporary_ token which is required in _every subsequent_ request to the target resources.

<!-- more -->


## Access Token Request

The HTTPS `POST` for FreeAgent requires [basic auth](http://en.wikipedia.org/wiki/Basic_access_authentication) using _client id_ and _client secret_ as username and password. That means supplying a `Authorization` header with base 64 encoded username and password, separated by a colon. So,

    client_id:client_secret

Should be encoded and sent over in the header. It'll look something like this.

    Authorization: Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=

The `POST` body should include the following [x-www-form-urlencoded](/blog/2012/06/11/http-encoding-schemes) parameters.

 * `grant_type=authorization_code`
 * `code=`the authorisation code (see [previous post]({{ root_url }}/blog/2012/08/11/oauth-and-http-part-i))
 * `redirect_uri=`your redirect URI

FreeAgent differs from a lot of other OAuth implementations where the information is pass along as query parameters to a `GET`.

The request should also include an `Accept` header of `application/xml` or `application/json`.

## The Request

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


## The Response

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


## Using the Access Token

To make fully authenticated calls to the target system, every request is made using the _access token_. Therefore, it must be extracted from the response above and stashed in your application. All that's left to do is pass this through on every request to a protected resource.

In FreeAgent's case, the token should be supplied in the `Authorization` header.

    Authorization: Bearer 1GwfYDOaz_rG35SSgf8y8aBUasP5QrG9FSasfiD13


## Refreshing the Access Token

The access token will eventually expire (FreeAgent have set it to expire in seven days but this may change). To refresh the FreeAgent token, you send a similar `POST` request to the access token request with a few minor differences. See the [FreeAgent documentation](https://dev.freeagent.com/docs/oauth#refreshing-the-access-token) for details.


## Next Up

That's about it for now. Hopefully its been useful. I may continue the series and post an extended example using raw HTTP to interact with FreeAgent (no OAuth library) if there's interest. Let me know.