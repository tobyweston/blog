---
name: jersey-and-ie8
layout: post
title: "Force IE8 to Display JSON with Jersey"
date: 2012-02-21 06:27
comments: true
categories: java REST recipe
sidebar : false
description: "Force IE8 to open JSON content within the browser with Jersey rather than prompt you to download and save as a file."
keywords: "ie8, json, in-browser, jersey, application/x-ms-application"
---

If Internet Explorer 8 performs a HTTP `GET` against some resource and receives a mime-type that it wasn't expecting, it will ask the user to download the resource and save it. Annoyingly for JSON content this means you wont see the JSON 'in-browser' like in Firefox and Chrome. If you're using [Jersey](http://jersey.java.net/), Oracle's JAX-RS reference implementation, here's how to make IE8 play nice.

<!-- more -->

The problem is in IE8's default set of `Accept` header values. For some reason, it'll ask for a very specific set of Microsoft types in the request;

{% codeblock %}
Accept: application/x-ms-application, application/xaml+xml, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*
{% endcodeblock %}

When the server responds with a `Content-Type` of anything other than what's in the accept list,
IE will prompt the user to save the resource instead of attempting to display it. That's fair enough as I imagine its
saying "I didn't say I could accept this so therefore, I don't know how to display it".

Responding to a request with the above `Accept` header from IE with a response including the following header

{% codeblock %}
Content-Type: application/json
{% endcodeblock %}

will prompt IE8 to save the file rather than display 'in-browser'.

When we return a response with a JSON content type, IE won't know how to handle it. We could send back our JSON as `text/plain` for all cases, but that kind of defeats the object of using `Content-Type` all together.

However, we can use Jersey to handle the IE case (where the request is for say `application/x-ms-application`)
by sending back plain text but still return JSON for all other cases.

{% codeblock lang:java %}
@Path("/customers")
public class Customers {

    @GET
    @Produces("application/json")
    public String getAllCustomers() {
        return allCustomersAsJson();
    }
 
    @GET
    @Produces("application/x-ms-application")
    public TextPlainOkResponse getAllCustomersForInternetExplorer() {
        return new TextPlainOkResponse(getAllCustomersAsJson());
    }
}
{% endcodeblock %}

The class above will return a list of all Customers as JSON. The `getAllCustomers` method will be dispatched to via
Jersey and send back the `String` with a `Content-Type` of `application/json` for all cases _unless_
the client asks for `application/x-ms-application`. This is the case for IE. Now, although the same JSON string is
constructed, we'll overwrite the `Content-Type` masquerading as `text/plain` in the `TextPlainOkResponse` class.

{% assign braces = '{{' %}
{% codeblock lang:java %}
public class TextPlainOkResponse extends Response {
 
    private final String json;
 
    public TextPlainOkResponse(String json) {
        this.json = json;
    }
 
    @Override
    public Object getEntity() {
        return json;
    }
 
    @Override
    public int getStatus() {
        return 200;
    }
 
    @Override
    public MultivaluedMap<String, Object> getMetadata() {
        return new MetadataMap<String, Object>() {{ braces }}
            put("Content-Type", Arrays.<Object>asList("text/plain"));
        }};
    }
}
{% endcodeblock %}

So for all clients asking for `application/x-ms-application`, they'll actually get `text/plain`. In the case of
Internet Explorer 8, it will display the JSON 'in-browser'. It won't apply any formatting though, so you may want to
pretty print the response before sending it back.

If it doesn't work for you, see what headers IE is actually sending and adapt the strategy accordingly. You can using
something like [ieHttpHeaders](http://www.blunck.info/iehttpheaders.html) or the awesome [Membrane](http://www.membrane-soa.org/soap-monitor/) to see what headers are going over the wire.
