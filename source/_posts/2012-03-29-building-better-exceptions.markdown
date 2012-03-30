---
name: building-better-exceptions
layout: post
title: Building Better Exceptions
time: 2012-03-28 06:00:00 +00:00
categories: java testing
comments: true
---

## Exceptions are Objects

Tell don't ask
Encapsulate

## Only using Runtime Exceptions


## Summary

- identify the boundaries (and so _when_ to handle)
- define a general handling approach (the _how_ to handle)
- use subclasses of `RuntimeException` to keep the code clean, catch these _only_ at the boundaries
- application specific exception subclasses should contain the specificifty (for example,
the message hardcoded in the constructor).
- exceptions are objects too; think OO.
- Never rethrow an exception verbatim. 
- However, if required, do _translate_ an exception into another at boundaries.
