---
layout: post
title: "Pair Testing Doesn't Work"
date: 2015-09-25 16:57
comments: true
categories: 
sidebar: false
published: false
keywords: "agile, pair test, interview, best interview answers, how to beat the interview, technical interviews"
description: "Pair tests are outdated. Don't cling to biased and loaded interview techniques when looking to hire developers, embrace fairer and more balanced techniques."
---

Either when looking for work or looking to recruit, I've been doing pair tests in one form or another since 2008. I've only recently come to the conclusion that they just don't work. At least not reliably. 

I'm left wondering why we still use "pair tests" for recruitment. Is it to see how candidates problem solve? How they'd be to work with? The only way to assess these things is actually to do them. Pair tests are a poor simulation. If you want to see how someone works, work with them. Don't _pretend_ to work with them.

<!-- more -->


## From the Interviewer Perspective

If the goal is to see how candidates pair, a pair test in an interview context is just the wrong way to do it. You're already setting things up as a **test** and however hard you try, it won't be a realistic simulation. You already know the answers, so despite saying "let's try and pair on a problem and work out the solution together", you're already coming to the table with huge preconceptions and are poised for judgement. 


## From the Candidates Perspective

The candidate has a right to understand what it might be like to work at your company and a pair test gives them very little information. As a candidate I'm terribly nervous, I'm full of doubt and questions about what the interviewers really want to see. 

Candidates are often hyper-sensitive to the interviewer's comments so when an interviewer asks what she considers an innocuous question about the exercise, it's all to easy for the candidate to freak out. For example;

    Interviewer:            "So why have you used a `val` there and not a `def`."
    Candidates inner voice: "Because that's how I like to do it... hang on, I can't say that. 
                             They know something I don't know. What is it? WHAT IS IT? Oh, my word, 
                             they think I'm an idiot. I *am* an idiot."  

It just comes with the territory. You're at interview. There is a very clear and very deep seated notion of employer / employee deference at play. Candidates are often expected to want to take a job, even when they know very little about it. Remember, any interview should be a two way process. Am I right for the role and is the role right for me. It should be a partnership. 

> During my last round of recruitment using pair testing, I made a huge effort to put candidates at ease. We asked candidates to bring code with them to extend and made it clear there is no right or wrong answer. Yet, without exception, all of them showed signs of stress, panicked and basically got them selves into a muddle. 



## Not Everyone Solves Problems the Same Way

When you ask a candidate to solve a problem, however trivial you might think it is, you're basically asking them to come up with a solution in thirty seconds. That's not how I work in my day job. I'll chew over a problem, try one or two things, roll back, have another go. I think about what I'm trying to do and that might take a minute. I don't hack the first thing that comes into my head. 

As an example, I did a pair test with a TV broadcasting company recently. They asked me to solve the [Shopping Basket Problem](https://github.com/tobyweston/shopping_basket). I floundered when I was put was on the spot but had another go later. At home, I spent an hour or so and came up with something I was really pleased with, including an elegant way to [mixin](https://github.com/tobyweston/shopping_basket/blob/master/src/main/scala/shopping/Fruit.scala) offers to shopping items.

    case object Banana extends Fruit(51) with ThreeForTwo
    case object Apple extends Fruit(12) with TwoForOne
    case object Pineapple extends Fruit(95)


## Not Objective

There is often no clear yes or no result to a pair test. Because of the stressful nature, you can't be sure you're getting the best out of candidates. People often don't take this into account and assume the simulation was realistic. Best case scenario: someone flies through the exercise and gets everything "right". Are they an easy hire? Is there more to them? 

> In my recent round of recruitment, we offered four roles and each of them basically messed up the pair test. Each of them panicked or went off in a weird direction in a moment of stress. There's no coming back for the candidate when that happens. I'm hugely proud that we understood things well enough to factor in other aspects and still offer after what might have been seen as a "fail".



## A Better Way

Rather than simulate a working environment, nurture a real working environment. It's not always practical to ask a candidate to work with you for a week on your projects but you can invite candidates to an assessment day or hackathon.

###  Assessment Days 

Batch your candidates into cohorts and ask them to pair with _each other_ whilst you observe. Solve a sensible but fun problem over the course of an entire day and get them to explain their choices and experiences.

Rotate the pairs and get everyone on your dev team involved. Get them to walk around the room to observe candidates. As you have the time, you can mix in more traditional one-to-one interviews towards the end of the day. Oh, and don't forget to provide lunch.


## Summary

Pair testing suffers hugely from cognitive bias(?)

It is really hard to be objective in assessing candidates using pair testing. Partly because this kind of assessment is inherently subjective. Pair testing doesn't lend itself to critical thinking as there is no clear critique. Trying to identify objective criteria for code is a waste of your time; "quality" is not quantitative.

Pair testing comes with huge cognitive bias for both parties (framing effect, anchoring)

Pair testing is a flawed approach to critical thinking as there is no clear critique or way of objectively assessing them.
