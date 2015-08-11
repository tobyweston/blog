---
layout: post
title: "Pair Testing Doesn't Work"
date: 2015-08-28 16:57
comments: true
categories: 
sidebar: false
published: false
keywords: ""
description: ""
---

Either when looking for work or looking to recruit, I've been doing pair tests in one form or another since 2008. I've only recently come to conclusion that they just don't work. At least not reliably. 

Why do we even use "pair tests" for recruitment? Is it to see how candidates _pair_? How they _problem solve_? How they'd be to work with? The only way to assess these things is actually to do them. Pair tests are a poor simulation. If you want to see how someone works, work with them. Don't _pretend_ to work with them.

<!-- more -->

## Full of Contradictions

Objective vs. Subjective


## From the Interviewer Perspective

If the goal is to see how candidates pair, a pair _test_ in an _interview_ context is just the wrong way to do it. You set things up as a test and however hard you try, it won't be a realistic simulation. You already know the asnwers, so dispite saying "let's try and pair on it and work out the solution together", you're already coming to the table with huge preconceptions and are poised for judegement.


## From the Candidates Perspective

The candidate has a right to understand how it might be working at your company and a pair test gives them very little information. As a candidate I'm terribly nervous, I'm full of doubt and questions about what the interviwers really want to see. 

Candidates are often hyper-sesitive to the interviewrs comments so when an interviewer asks what she considers an inocous question about the exercise, it's all to easy for the candidate to basically freak out. For example;

    Interviewer:            "So why have you used a `val` there and not a `def`."
    Candidates inner voice: "Becuase that's how I like to do it... hang on, I can't say that. They know something I don't know. What is it? WHAT IS IT? Oh, my word, they think I'm an idiot. I *am* an idoit."  

It just comes with the territory. You're at interview. There is a very clear and very deep seated notion of employer / employee deference at play. Candiates are often expected to want to take a job, even when they know very little about it. Remember, any interview should be a two way process. Am *I* right for the role and is the *role* right for me. It should be a partnership. 

> During my last round of recruitment using pair testing, I made a huge effort to put candidates at ease. We asked candidates to bring code with them to extend and made it clear there is no right or wrong answer. Yet, without exception, all of them showed signs of stress, paniced and basically got them selves into a pickle. 



## Not Everyone Solves Problems the Same Way

When you ask a candidate to solve a problem, however trivial you might think it is, you're basically asking for them to come up with a solution in thrirty seconds. That's not how I work in my day job.

I'll chew over a problem, try one or two things, roll back, have another go. I think about what I'm trying to do and that might take me a mintue. I don't hack the first thing that comes into my head. As an example, I did a pair test at ITV recently. They asked me to solve the [Shopping Basket Problem](). I floundered when I put was on the spot but had another go later. At home, I spent an hour or so and came up with something I was really pleased with, including an elegant way to mixin offers to shoppinh items;

    case object Banana extends Fruit(51) with ThreeForTwo
    case object Apple extends Fruit(12) with TwoForOne
    case object Pineapple extends Fruit(95)


## Not Objective

There is often no clear yes or no result to a pair test. Because of the stressful nature, you can't be sure you're getting the best out of candidates. People often don't take this into account and assume the simulation was realistic. Best case scenario: someone flys through the exercise and gets everything "right". Are they an easy hire? Is there more to them? 

> In my recent round of recruitment, we offered four roles and each of them bsaically messed up the pair test. Each of them paniced or went off in a weird direction in a moment of stress. There's no coming back for the candidate when that happens. I'm hugely proud that we understood things enough to factor in other aspects and still offer on what otherwise would have been seen as a "fail".



## A Better Way




## Summary

Pair testing suffers hugely from cognitive bias(?)

It is really hard to be objective in assessing candidates. Partly by definition as assessment is inheriently subjective. Pair testing comes with huge cognative bias for both parties (framing effect, anchoring)

Pair testing is a flawed approach to critical thinking as there is no clear critque or way of objectively assessing them.
