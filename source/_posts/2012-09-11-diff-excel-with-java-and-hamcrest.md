---
layout: post
title: "Diff Excel with Java and Hamcrest"
date: 2012-09-11 20:10
comments: true
categories: java recipes
sidebar: false
published: false
keywords: "excel, diff, compare excel"
description: "Diff Excel using Java and Hamcrest. Build and compare Excel files using Java and Hamcrest."
---

Comparing Excel spreadsheets programmatically can be tricky. Projects like [Apache POI](http://poi.apache.org/) and [JExcel](http://jexcelapi.sourceforge.net/) let you build and integrate sheets but don't offer an built in compare function. Fortunately, [simple-excel](http://github.com/tobyweston/simple-excel) offers a simplified API for building sheets in Java and a bunch of [Hamcrest](http://hamcrest.org/) matchers to find differences.

<!-- more -->


Check out the [GitHub](http://github.com/tobyweston/simple-excel) project.
