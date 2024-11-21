---
layout: post
title: "HTTP Should be Simple"
date: 2012-06-10 10:06
comments: true
categories: java REST
sidebar: false
description: "Examples from simple-http, a Java HTTP client library making HTTP calls much more straight forward"
keywords: "simple-http, simple http, java, apache hc, apache http, configuring apache http, java"
---

Apache's HTTP client libraries (version 4.x has a very different API than 3.x) are fairly involved to configure and require a lot of boilerplate code. Making a simple HTTP GET request usually ends up with way too many lines of code. Working with HTTP should be simple, so I've been working on a library offering a straight forward API with sensible defaults. Typically, you'll make HTTP requests with just one line of code.

``` java
HttpResponse response = anApacheClient().get(new URL("http://baddotrobot.com"));
```
<!-- more -->

## The API

The library, [simple-http](https://github.com/tobyweston/simple-http), provides an implementation agnostic API. It ships with support for Apache's HTTP client 4.x but can be extended to use any underlying HTTP client library without changes to the API. It's essentially a builder ontop of the Apache library. You configure your client in a builder style then hit the HTTP verbs. For example.

``` java
HttpResponse response = anApacheClient()
    .with(httpTimeout(seconds(30)))
    .with(proxy(new URL("http://proxy.com:8999")))
    .get(new URL("http://baddotrobot.com"),
        headers(
            header("Accept", "text/html")
        )
    );
```

It's supposed to be so simple, it's self explanatory. If it's not, [let me know](https://twitter.com/#!/jamanifin). The starting point is just `HttpClients.anApacheClient()`.

## Separation of Concerns

First and foremost, [simple-http](https://github.com/tobyweston/simple-http) helps with separation of concern. It provides a basic `HttpClient` interface which you can easily mock in your code to assert your components send messages but not concern yourself with raw HTTP. It provides the anti-corruption layer between your application and HTTP. You depend on the [simple-http](https://github.com/tobyweston/simple-http) interfaces and not Apache's implementations. In that way, your application's interactions with HTTP are in terms of the _HTTP verbs_ and not Apache's technical details.

## Configuration

Secondarily, the library provides a fluent, straight-forward interface to instantiate and use a HTTP client. If you need special configuration, that's fine but as it comes sensible defaults, for the most part all you'll need to do is new it up. For example, to create a HTTP client which trusts self signed certificates, do the following.

``` java
HttpClient http = anApacheClient().withTrustingSsl();
```
Regular SSL authentication is straight forward too, just add a username and password to your client.

``` java
HttpClient http = anApacheClient().with("bobby brown", "secret");
```

## Helping you Test

As [simple-http](https://github.com/tobyweston/simple-http) ships with a bunch of `Matcher`s, it's easy to make assertions or set expectations. For a simple case, compare the following.

Using Apache directly, you might write something like this.

``` java
assertThat(apacheResponse.getStatusLine().getStatusCode(), is(200));
```
which, when it fails presents you with the following.

    java.lang.AssertionError:
    Expected: is <200>
         got: <404>


With [simple-http](https://github.com/tobyweston/simple-http), you write.

``` java
assertThat(response, has(status(200)));
```

which is much more helpful when it fails, showing the response's status code, message, content and headers.

    java.lang.AssertionError:
    Expected: a HttpMessage with status code <200>
         got: <DefaultHttpResponse{statusCode=404, statusMessage='Not Found', content='{ "message", "not found" }', headers='SimpleHeaders{headers=[SimpleHeader{name='Content-Type', value='application/json'}]}'}>

Of course, you can enrich the assertions, for example.

``` java
assertThat(response, allOf(has(status(200)), has(headerWithValue("Content-Type", containsString("json")))));
```
or assert against the message body, for example.

``` java
assertThat(response, has(content(not(containsString("\"error\"")))));
```

Or use them in an expectation, for example using [JMock](http://jmock.org/) below, we expect a HTTP `GET` to the URL [http://acme.com/stock](http://acme.com/stock) when we call the method `inventoryCount()`.

{% assign braces = '{{' %}
``` java
@Test
public void anExample() throws MalformedURLException {
    final HttpClient http = context.mock(HttpClient.class);
    context.checking(new Expectations() {{ braces }}
        oneOf(http).get(with(new URL("http://acme.com/stock")), with(headers(header("Accept", "application/json")))); will(returnValue(...));
        ...
    }});
    new StockRoom(http).inventoryCount();
    context.assertIsSatisfied();
}
```
Or here where we expect a HTTP `POST` to submit a URL form encoded body to add some stock. In the example, the form parameter we're expecting should look like `stock=%7Bsome%3A+json+message%7D`. Notice how [bad.robot.repo](http://robotooling.com/maven/) avoids this complexity.

``` java
public void anotherExample() throws Exception {
	checking(new Expectations() {{ braces }}
		oneOf(http).post(with(new URL("http://acme.com/stock")), with(post(content(params("stock", "{some: json message}").asString()))));
	}});
	new StockRoom(http).addStock(...);
}
```
## Download

You can download from the [bad.robot.repo](http://robotooling.com/maven/) Maven repository or get the source from [Github](https://github.com/tobyweston/simple-http).

``` xml
<repositories>
    <repository>
        <id>bad.robot</id>
        <name>bad.robot repository for robotooling</name>
        <url>http://www.robotooling.com/maven/</url>
    </repository>
</repositories>

<dependency>
    <groupId>bad.robot</groupId>
    <artifactId>simple-http</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependency>
```

Enjoy and [let me know](https://twitter.com/#!/jamanifin) how you get on.