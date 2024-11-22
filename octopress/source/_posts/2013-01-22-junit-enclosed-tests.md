---
layout: post
title: "Embed Multiple Tests in JUnit "
date: 2013-01-22 19:14
comments: true
categories: java object-oriented
sidebar: false
published: false
keywords: ""
description: ""
---

Occasionally we might want our tests to span multiple files. One file for an acceptance style test and one for a unit style test. Sometimes, different file names make sense and we can easily locate them. If however, you want to create a test with a strange file name, it can get lost in your source. [JUnit](http://junit.org)'s `Enclosed` runner lets you embed multiple test classes within a single JUnit test.

<!-- more -->

@RunWith(Enclosed.class)
public class ExampleTest {

    @Test
    public void topLevelTestsDontRun() {
        fail("this test is never run");
    }

    public static class Example {

        @Test
        public void addition() {
            assertThat(1 + 1, is(2));
        }
    }

    public static class AnotherExample {

        @Test
        public void multiplication() {
            assertThat(2 * 2, is(4));
        }
    }

}