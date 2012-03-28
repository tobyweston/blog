---
name: never-assert-against-exception-messages
layout: post
title: never-assert-against-exception-messages
time: 2012-03-28 06:00:00 +00:00
categories: java 
comments: true
---

This post offers a general approach to exception handling that if followed, means that when testing for exceptions, you need _never_ assert on the contents of the exception message...

<!-- more -->

## General Approach

So earlier I said that _we should never assert against the exception message_. That's rather an extreme position so I should probably explain what I mean by that.

As a general approach, exceptions should be dealt with at the boundaries of your system. Examples include architectural "layers' such as the UI or the API. I use API in the general sense; it could be a concrete RESTful API or something less formal like the API between two internal components of your system.

(the implication being a user would benefit from seeing that some problem occurred), 

