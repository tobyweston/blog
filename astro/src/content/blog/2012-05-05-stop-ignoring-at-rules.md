---
title: "Stop Ignoring @Rules"
pubDate: "2012-05-05"
categories: 'java testing'
keywords: "JUnit @Rule, ExternalResource, TemporaryFolder, JUnit rules, test fixtures, setup teardown"
description: "Stop overlooking JUnit's @Rule annotation. Discover how ExternalResource, TemporaryFolder and custom rules make test setup and teardown cleaner."
---

If you're using a version of JMock prior to 2.6.0 and use `@RunWith(JMock.class)` you may have spotted that your `@Rules` are actually being ignored when running JUnit tests. This could mean false positives. It's because older versions of the `JMock.class` extend `JUnit4ClassRunner` and `JUnit4ClassRunner` ignores rules.

The good news is that [JMock 2.6.0](http://repo1.maven.org/maven2/org/jmock/) and above use the newer `BlockJUnit4ClassRunner` and this does support rules. Bear this in mind when working with any class and the `@RunWith` as they may also extend the rule ignoring runner.