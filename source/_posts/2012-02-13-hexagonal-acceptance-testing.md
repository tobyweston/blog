---
layout: post
title: Hexagonal Acceptance Testing
date: 2012-02-13 21:24
comments: true
categories: java testing agile
---

There's no reason a unit test can't also be an acceptance test. If you can prove that the _unit_ behaves a certain way _and_ that it production, it will behave in the same way as in your unit test, the intersection should give you enough confidence.

What seems to make things harder to discuss is that its difficult to agree on a common definition for the different types of testing. As a peer-group, we're usually horrified by the previous paragraph and ask the question _"shouldn't we start up the entire stack in an acceptance test?"_. This often leads us to long-running, duplicative and expensive tests in the name of acceptance testing. 

Taking inspiration from Cockburn's [Hexagonal Architecture](http://alistair.cockburn.us/Hexagonal+architecture) and being more flexible in our technical definitions of acceptance testing however, we _can_ create lightning fast acceptance testing.

<!-- more -->  

## Conway's Law

To paraphrase something [@Jazzatola](https://twitter.com/#!/Jazzatola) recently said

{% blockquote @Jazzatola https://twitter.com/#!/Jazzatola %}
"people are usually happy to test interactions with other systems 'by specification' but are less happy to do so when testing their internal systems"
{% endblockquote %}

As he points out; we're happy to say "given the external system responds with `X`, when we send a message `Y` then our system behaves `Z`". We know the API and test against it as a _specification_, typically via _mocking_ the behaviour of the external system and testing against the response. We're less happy to talk about our internal interactions as internal APIs in the same way.

I find this interesting for a couple of reasons. [@Jazzatola](https://twitter.com/#!/Jazzatola) was suggesting that this is an example of [Conway's law](http://en.wikipedia.org/wiki/Conway's_law); where the communication structures within an organisation are leading design. We're physically separated from our external system actors but intimately acquainted with the internal communication flows. After all, we wrote them.

It's also interesting because it can limit how we go about implementing our acceptance tests.

## Hexagonal Implementation

If we look at our system as a series of _ports_ and _adaptors_ (as in Cockburn's [Hexagonal Architecture](http://alistair.cockburn.us/Hexagonal+architecture)), we can start to test it as a series of internal, co-operating handoffs. Don't we already test our systems like this; with conventional mocking? The difference is that this kind of mocking is at a finer grained level; we mock _collaborators_ to create unit-style tests and drive out design. When we mock external systems and the _ports_ in our internal systems, we're mocking coarse grained _behaviours_. We're confirming an established design rather than driving one out. We can formalise this established design as _ports_.

If you look closely at the last few sentences you'll notice that I'm talking about _test confirm_ at the coarse grained level rather than the _test driving_ techniques we apply with unit-style tests. I think this is natural fit for acceptance testing where we should be thinking about testing the external affects produced by internal flows (more black than white box).

So, given we expect an internal interaction to behave in such-and-such way, why do we need to startup the entire application to exercise the effect of that behaviour? We don't. We can _simulate_ the specification internally by mocking and produce a series of overlapping tests. Each one supporting and giving more confidence to the last.

We've certainly had some great successes with this technique. We've produced faster running test suites that customers were happy to "accept" or sign-off against. We built trust working with the customers to understand the approach and put ourselves more easily in their 'voice' describing the system as a series of internal API interactions.

### Conventional Hexagonal Architecture Footnote

In the original article, Cockburn talks about ports and adaptors as a fairly abstract architectural approach. He describes it in terms of a pattern which have slightly different motivations than those described here. 

He talks about a relatively small number of _ports_ (say ~4-5) and decoupling _major_ components of a system (for example, the database and the GUI) so that it can be driven and tested by different _external_ actors. 

I'm talking more about changing the _external_ nature of these actors to be more _internal_. If we have a much larger number of ports (say >30), decoupling _minor_ components we can achieve this substutatabiliy on a bigger scale and be more flexible on how we test the system.

Conway described an approach where we can test the system at end-to-end via it's ports. Taking this further to confirm small business functionality or _acceptance criteria_ is a logical progression and fits nicely into iterative development.

Have a go and see if it works for you...


