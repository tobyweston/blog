---
name: changing-test-gears
title: Changing Test Gears
pubDate: 2010-07-09 18:55:00 +01:00
categories: agile coaching java mocking testing
description: "Understanding different types of testing (unit, integration, acceptance) and when each is appropriate is a subtle skill. Optimising your approach and avoiding duplicate testing requires you know the context you're working in and what's coming up."
keywords: "unit testing, acceptance testing, integration testing, unit vs acceptance testing, agile testing, user testing, uat, java, spring, application context, builder pattern"
---

Good poker players know when to change gears. They know when to alter their playing style from cautious to aggressive as the game changes and players drop out. They look at how the _odds change_ as the game progresses and react appropriately. It's the same with testing, you gotta know when to change gears.
  
To put it development terms, good developers know when to change gears. They know when to change their testing style from cautious to aggressive as the code evolves.

Lets pretend there is just three types of testing; _unit_, _integration_ and _acceptance_. In the interest of stereotyping, we'll define them simplistically as

  * _Unit_ - single object tests, no collaborations (strict I know, but bear with me)
  * _Integration_ - testing object collaborations, for the purposes of this article, lets assume end-to-end testing slot into this bracket
  * _Acceptance_ - leaning towards end-to-end but key here is that they are customer authored. As such, to convince the customer these will likely be relatively coarse grained and start outside the system boundary

<!-- more -->

## Starting in a Low Gear with Unit Tests

  
People are probably most comfortable with this type of testing. The term unit testing and the technology JUnit have become so intertwined in the Java world, that people often confuse tests written with JUnit as unit tests. They may be, but they may not be. So where's the value in defining the term unit testing and how does knowing what type of test you've just written in JUnit help with changing gears?

  
Knowing what gear you're in and knowing the terrain that’s coming up is essential for you to select the right gear. Writing a non-unit test in JUnit has value, of course it does, so why should I care if it’s a unit test or an integration test? Knowing where you are and where you want to be is useful because you can defer some things and avoid duplication. So for me, unit testing is good for testing the edge cases ([Right BICEP](http://lmgtfy.com/?q=right+bicep+junit+testing)) and exploring the class you're writing.

It can be especially useful when you _test drive_ towards something or explore relationships and your understanding of the classes roles and responsibilities. In this sense, testing becomes a design or analysis activity; a chance to phrase your thinking and understanding in code.

The regression element can quickly lose value here. For example, writing a test with mocks to explore the interaction between two collaborators, A and B. Then writing a separate test to explore the same for classes B and C. Then a test for A, B and C. There was value in each test individually, but is there still value in all three when there is obvious cross-over? When might I consciously choose _not_ to write unit tests?
  

## Changing up to Integration Tests

  
If I know the context that a set of objects are going to work together in, I'm going to want to be confident that they work together as expected. I can't test these in isolation, so I'm going to need to test them in cooperation. At this level, my confidence is fairly high around the composites so I'm already up and running. I'm more concerned here with a broader brush approach. I'm certainly not interested in re-testing all the lower level object tests, just how they operate together.

So I change up a gear and as a developer, convince myself that these object work together _in context_. I'm most likely still using JUnit but I do so with a clear understanding of what gear I'm in.

  

## Cruising with Acceptance Tests

  
So how about the value to the business? The unit tests in particular don't advertise value to the business, they're a developer tool and its all too easy to write individual classes well with good test coverage and yet combine them into something that doesn't work for the business.

Demonstrating to business that their specifications have been meet is the ultimate gear, and to change up to that gear and have supreme confidence in the system means going through the previous gears. Knowing that you'll be changing up whilst in lower gears can help you decide what to do (and what to leave out) in those lower gears.

  
For example, lets assume the business want to _see_ the affect of a configuration file in the system. When developing the code to load and decode the contents of the file, you started by proving the component works at the unit level so why would you test that the component is wired up correctly as a unit test? You'd be forced to mock that component in some higher level component and test it calls it. But what does this give you? You can still wire the higher level component up incorrectly in production. The acceptance test is going to have to test this to demonstrate the affect, so there's an argument to say you can leave it to the acceptance test to verify.


## The Missing Gear?

  
When we build software in a componentised way, we're often left with objects that work in isolation with their dependencies passed in. We push up and up the assembly of the objects and are left with parts of the system that are responsible for this assembly. This might be done in code or by some dependency injection framework. I'm really talking about the _configuration_ of your application here, be it done declaratively via Spring's application context or imperatively in code.

Either way, it feels like these 'assemblers' have a clear role and responsibility and so shouldn't they be tested? What gear do we test them in? Personally, I'm comfortable in limiting the assembly options and so reduce the combinations of testing required. With a single "builder" or "spring context", I'm comfortable with testing these through acceptance tests.

  
In this article, I suppose I'm using "gears" as an analogy for pragmatism and certainly not pace. I'm not saying that good developers know when to rush, compromising quality but they do know how to optimise their testing strategies. I think its important not to get bogged down in exhaustive unit-style testing if its not of value. Understanding what gear you're in and what gear you'll soon be in can help focus your attentions and avoid retesting the same thing again and again.

"What to test and when to test it" is a question I find myself asking again and again.

  



