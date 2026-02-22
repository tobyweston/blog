---
title: "Interfaces vs Class impostorisers"
pubDate: '2008-12-24'
categories: 'java-testing'
keywords: "JMock, class impostorisers, mocking, interface mocking, cglib, SWT testing, legacy code"
description: "When is using a class imposturiser in JMock acceptable? Explores the trade-offs of mocking classes vs interfaces, particularly when working with third-party or legacy code like SWT."
---

I've been mocking with JMock2 for a while now and fully buy into using mocks and driving out behaviour using interfaces. However, I'm not sure I get the resistance when people want to use class imposterisers.

I've been doing a lot with SWT lately and generally want to unit test the UI elements. One way I've managed to do this is to mock parts of the GUI framework using impostorisers. Unless I want the full UI brought up, there just isn't another way. The UI API doesn't offer me any convenient interfaces and I can't even create sub-classed mocks myself as SWT prevents you from sub-classing with run time checks.

I understand that by slowly teasing out behaviour during the mocking / TDD process you can clearly express the collaborations a class may have but I feel that you can still be clear about class behaviour when using an impostor. It's just code right? I'm not sure I care that collaborations are documented as interfaces or not, my tests express the relationships and I've gone through the same thought process to understand clearly how the classes under test interact. So why is an impostor the bad guy?


In the case of legacy code or third part code, you're kind of stuck with impostorisers right? I mean you could build an application layer between your code and the third party stuff but I'd want better motivation for doing this than to avoid using impostorisers.

In the traditional description of an interface, we're taught to use interfaces when we want to share behaviour across multiple implementations. When driven to creating interfaces for mocking purposes we often only ever have one implementation in production which would seem at odds with this traditional definition. We do usually end up with a well designed applications which are nicely componentised and plugable, but we rarely plug anything different in. This in itself often leads us to testing the production configuration in larger end-to-end style tests.

So I feel that if you're clear about what's driving you to expose a public method on a class, your test exercises the collaboration clearly with mocks and your class under test is small and discrete then impostorising isn't really the devils work. You've considered what you're doing and why and at the end of the day, you've created a test that does what its supposed to.

If you're naturally defining interfaces, then like me, mock away but at least consider not creating an interface if the only reason you're doing this is for mocking. If you do end up creating an interface just for mocking, don't do it just for mocking but take it further and be explicit in why you're formalising the collaboration. Think about the behaviour and let it drive your design.

  




  

  



