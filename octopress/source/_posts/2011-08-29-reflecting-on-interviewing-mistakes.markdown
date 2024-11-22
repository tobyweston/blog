---
name: reflecting-on-interviewing-mistakes
layout: post
title: Reflecting on Interviewing Mistakes
time: 2011-08-29 13:30:00 +01:00
categories: agile coaching
comments: true
sidebar : false
description: "Reflecting on the last few years of heavily interviewing for agile developers. We've got the process down but often fool ourselves and let good guys slip through. Right or wrong answers don’t really have a place because there’s never a right or wrong answer in what we do."
keywords: "interviewing, agile interview, pair test, reflections on interviewing, open questions, honesty when interviewing"
---

Recruiting for the next guy on your team is hard. At first glance it doesn't seem to be, we've developed techniques like pair tests but as I start to look at it more closely, I've started to notice that even the more progressive techniques don't preclude us from making the same mistakes as the traditional interview.
  
Let's take an example from two teams.

<!-- more -->
  
Team A's process starts off by favoring buzz word heavy CVs and CVs that meet a minimum number of years of experience. A unattended pen and paper test, characterised by very closed questioning against specialist areas of the programming language. This might include questions around language syntax semantics (keywords and modifiers, object equality etc etc). Things like bubble sorts algorithms are requested. Scores out of 100 are tallied. Things are fairly black and white.

{% pullquote %}
Team B's process favors mention of agile experience in the CV. Follow up questions prompt genuine conversation {" but often an implied hurdle that the candidate must jump is "has he reached the same conclusion as me on topic X?" "}. The unattended coding exercise is not a test, at least it should be more of an exercise to explore the way a candidate approaches things. The team might require the presence of unit tests and evidence of TDD but should actively not persecute style or syntax. Something that's harder in practice to do than in theory.
 {% endpullquote %}

Hopefully, its clear that Team A's selection process is heavily biased towards developers with good memories. It's probably unfairly prejudice against candidates that haven't had specific exposure to specific scenarios / solutions. I experienced this when I was asked to write a algorithm to calculate prime numbers with pen and paper. I fumbled through and handed over my scrawl. I explained that I'd prefer write tests, experiment with the code and improve the design; basically to learn as I went along. The response from the interviewer, looking down at my scribbling, was "that's not really what we're looking for... have you heard of the Sieve of Eratosthenes?". Obviously, I hadn't.
  
Rather than assess my approach, the interviewer was looking for a specific piece of knowledge but what for? If I got the job I'm pretty sure my first task wouldn't be to write something to work out prime numbers. Would that fix some production problem? Would it introduce a new feature that had no other solution? No.

A huge part of what we do is learn, or at least it should be. Failure is what makes us better and in environments where failure is embraced and we write code that we can (fairly) easily rework, we get better systems (as we refine our understanding). We never now what the real problems are going to be when we start a story. The interviewer above simply brushed over this, it seemed he wanted me to reach the same conclusion he had without explaining the steps I took to get there. Without any advocacy on my part, how would he know I could do it again with a different problem?

> "Right or wrong answers don't really have a place because there's never a right or wrong answer in what we do."

Having said all that, I'm sure we'd all favour a process like Team Bs but I'm starting to see that Team B are making at least some of the same mistakes just in a more subtle way...

  
For the CV selection, Team A look for "spring", "hibernate" and other technology buzzwords. Team B look for "refactoring", "TDD", "XP" and other development buzz words, the reason usually cited as being because the technologies aren't as import. Team B are favouring the _why_ over the _how_, they're assuming given the right approach and smart people, specifics around technologies can be learnt. Both teams are trying to expose characteristics of the candidates that mirror their own.
  
Team B asks candidates to complete a short programming exercise off-line. Implement a library, a DVD store, a robot explorer, whatever. It should only take an hour or so and demonstrates the candidates style. I've certainly seen it as an effective tool to eliminate people that really can't code for toffee but I've also seen people fall into the same old trap and eliminate people who missed something specific hidden there. A trivial example might be "oh! they didn't use dependency injection. Fail!".

  
Team B's pair test should be a great way to understand how a candidate operates in front of an IDE and if you'll actually be able to work with him. A bit like the unattended test, it's a good way to eliminate extreme cases. If the candidate behaves completely anti-socially, wont listen and codes like mad man, you can probably reject him with confidence. It's easy to let bad interview habits creep in though; to focus more on some obscure gotcha in the code than how the candidate is actually pairing.

> "I think the problem with both these techniques (unattended exercise and the pair test) is when too much specificity comes in at the start. When you are looking for something specific, you'll often be disappointed."

I've certainly heard myself say "oh, he didn't spot that there was a precision issue with double there...". In all honesty, I'd miss that kind of bug as often as I'd spot it but I'd hire me! The upshot there, especially when we doing a couple of pair tests a week, is to stay focused on why you're doing the pair test and not on the test itself. Are we doing this to see if the candidate can spot all the traps and pitfalls that we spent so long putting in or do we want to see how they pair? In my view, if they get the "right" answer is almost irrelevant, it's how they explore the problem.
  
I guess what I'm reflecting on here is how as a peer group, we pretty much realise that closed questioning limits our choices and that open ended questions lead to real conversations that are more relevant to the types of conversations we have day to day. Right or wrong answers don't really have a place because there's never a right or wrong answer in what we do. If I implement a prime number finder without the Colander of Eratosthenes, am I wrong? The tests still pass so I must be right? Is Eratosthenes more right? Despite this realisation though, we can easily fall into a more subtle way of behaving where we mentally start ticking off specifics for a candidate.
  
I guess we have to keep reminding ourselves what's important and what we're looking for in a candidate. I guess I'm mellowing in the way I assess candidates and probably rejected a fair few unfairly in the past. Sorry.

  






