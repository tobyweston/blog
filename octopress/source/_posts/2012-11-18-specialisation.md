---
layout: post
title: "Specialisation and Generalisation in OOD"
date: 2012-11-18 08:22
comments: true
categories: java object-oriented
sidebar: false
published: false
keywords: "generalisation, specialisation, inheritance, composition, aggregation"
description: "Specialisation and generalisation in OOD and how inheritance, aggregation and compoisition fit in."
---



Objects aren't data plus behaviour, they're really just behaviour that may use data.

When subclassing, I try to adhere to the "is a" rule but more than that I also try to stick to the "exchibites same behaviour" rule.

For example, I'm usually suspicious about subclassing an object that contains just data (ie, a bean). It certainly makes more sense to subclass when something has behaviour and you're inheriting that behaviour. If that behaviour is facilitated by the use of the object's data, great but that data doesn't *define* the behaviour.

Specialisation and Generatlisation

People tend to talk in terms of inheritance when talking about the "is a" relationship. However, the more general term _specialisation_ is really what we're interested in object oriented design. 

Inheritance is just one mechanism to implement specialisation and generalisation. Composition, aggregation and role based design are all alternatives.


Generalization/specialization is an abstraction principle that allows to define classes as a refinement of other
classes. [1]

Calling "super" from a sub-class to its parent, couples the child to the parent [James]. UI frameworks are a good example where the domain isn't really a good application of OO. The noun has moved away from ...?... would aggregation be prefable here? Kind of means that inheritance is well suited for varying behaviour and not algorthmic variation. That is to say, varying the algorithm defined in the super type couples to that super type, whereas varying true behaviour doesn't. In the later case, you request an object responds to sending a message and don't care how, in the former, there's some implicit knowledge that to respond to the message, the reciever will ask its parent the same question.

Aggregation vs Compoisition

Inheritance vs Aggregation

Inheritance for code reuse is a bad thing.


See previous post.


[1] GENERALIZATION/SPECIALIZATION AND ROLE IN OBJECT
ORIENTED CONCEPTUAL MODELING, Monique Snoeck, Guido Dedene