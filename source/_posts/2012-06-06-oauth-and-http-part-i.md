---
layout: post
title: "OAuth &amp; HTTP (Part I)"
date: 2012-06-06 19:20
comments: true
categories: java
sidebar: false
published: false
---

## A typical OAuth / FreeAgent flow using Google's oauthplayground

<!-- more -->

## GET /approve_app

### Request

    GET /v2/approve_app?redirect_uri=https%3A%2F%2Fcode.google.com%2Foauthplayground&response_type=code&client_id=4ta9v9JrXqSGdcdNuzTUtA&scope=https%3A%2F%2Fapi.sandbox.freeagent.com%2Fv2%2Fapprove_app+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.file&access_type=offline HTTP/1.1
    Host: api.sandbox.freeagent.com
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Referer: https://code.google.com/oauthplayground/?code=1ZhV9346i6dDT3vZ7g7AH3GS3WYRvVhDrQsdYjKxA&state

### Response

    HTTP/1.1 302 Found
    Content-Type: text/html; charset=utf-8
    Location: https://api.sandbox.freeagent.com/v2/login

    <html><body>You are being <a href="https://api.sandbox.freeagent.com/v2/login">redirected</a>.</body></html>

## GET /login

### Request

    GET /v2/login HTTP/1.1
    Host: api.sandbox.freeagent.com
    Referer: https://code.google.com/oauthplayground/?code=1ZhV9346i6dDT3vZ7g7AH3GS3WYRvVhDrQsdYjKxA&state
    If-None-Match: "edf508dcf787ca438f1a28bbac4a6ff1"
    Cookie: _freeagent_session=BAh7CUkiD3Nlc3N...988a3e907ab901054d
    Connection: keep-alive
    Proxy-Connection: keep-alive

### Response

    HTTP/1.1 304 Not Modified

## POST /handle_login

### Request

    POST /v2/handle_login HTTP/1.1
    Host: api.sandbox.freeagent.com
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2
    Content-Length: 52
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Origin: https://api.sandbox.freeagent.com
    Content-Type: application/x-www-form-urlencoded
    Referer: https://api.sandbox.freeagent.com/v2/login

    email=my.email%40gmail.com&password=secretstuff

### Response

Which gives back a `302`

    HTTP/1.1 302 Found
    Content-Type: text/html; charset=utf-8
    Location: https://api.sandbox.freeagent.com/v2/request_approval

    <html><body>You are being <a href="https://api.sandbox.freeagent.com/v2/request_approval">redirected</a>.</body></html>

## GET /request_approval

### Request

Follow this to get `/request_approval`

    GET /v2/request_approval HTTP/1.1
    Host: api.sandbox.freeagent.com
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Origin: https://api.sandbox.freeagent.com
    Referer: https://api.sandbox.freeagent.com/v2/login

Which gives you the web page to login

### Response

    HTTP/1.1 200 OK
    Content-Type: text/html; charset=utf-8

    <html>
        ... HTML requesting Authorisation
    </html>


## POST /grant_approval

### Request

Which on successful submission redirects back to the orginal redirection url.

    POST /v2/grant_approval HTTP/1.1
    Host: api.sandbox.freeagent.com
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2
    Content-Length: 113
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Origin: https://api.sandbox.freeagent.com
    Content-Type: application/x-www-form-urlencoded
    Referer: https://api.sandbox.freeagent.com/v2/request_approval
    Accept-Language: en-us
    Accept-Encoding: gzip, deflate
    Cookie: _freeagent_session=BAh7CUkiD3Nlc3Npb25faWQGOgZFRiIlN2RhMDcyYmNmMzljZTY4NmM4Mjg5OTMwODY0MDkzYmZJIgphcGl2MgY7AEZ7CjoYb2F1dGhfcmVzcG9uc2VfdHlwZUkiCWNvZGUGOwBUOhRvYXV0aF9jbGllbnRfaWRJIhs0dGE5djlKclhxU0dkY2ROdXpUVXRBBjsAVDoXb2F1dGhfY2xpZW50X3N0YXRlMDoXb2F1dGhfcmVkaXJlY3RfdXJpSSIsaHR0cHM6Ly9jb2RlLmdvb2dsZS5jb20vb2F1dGhwbGF5Z3JvdW5kBjsAVDoTb2F1dGhfYWNjb3VudHNbBlsHSSInQmFkIFJvYm90IChEZXZlbG9wbWVudCkgKGJhZHJvYm90KQY7AFRpAfpJIg9leHBpcmVzX2F0BjsARkl1OglUaW1lDdIUHIChjS7FCjoLQF96b25lSSIIVVRDBjsAVDoNbmFub19udW1pAiYBOg1uYW5vX2RlbmkGOg1zdWJtaWNybyIHKUA6C29mZnNldGkASSIQX2NzcmZfdG9rZW4GOwBGSSIxZzg4UWFNd1NTcC9yVmJPdUQ1a1lrLzM5NHRhM2JhS3laQ1Rxc25UUGJUND0GOwBG--954c4bc953caf4c9e9e3481e6b7c56b3672fa33e
    Connection: keep-alive
    Proxy-Connection: keep-alive

    utf8=%E2%9C%93&authenticity_token=g88QaMwSSp%2FrVbOuD5kYk%2F394ta3baKyZCTqsnTPbT4%3D&user_id=250&commit=Authorise

### Response

    HTTP/1.1 302 Found
    Location: https://code.google.com/oauthplayground?code=1ZhV9346i6dDT3vZ7g7AH3GS3WYRvVhDrQsdYjKxA&state

    <html><body>You are being <a href="https://code.google.com/oauthplayground?code=1ZhV9346i6dDT3vZ7g7AH3GS3WYRvVhDrQsdYjKxA&amp;state">redirected</a>.</body></html>