---
title: "Establishing an Engineering Culture"
subTitle: "Using trust, voice, and autonomy to build generative teams"
description: "How trust, voice, and autonomy shape engineering culture, with practical levers drawn from Westrum, DORA, and Deming."
heroImage: "/images/heroes/trust-voice-autonomy.svg"
pubDate: 2020-02-01
categories: "engineering culture"
keywords: "engineering culture, trust, voice, autonomy, DORA, Westrum, Deming"
---

Establishing an Engineering Culture at DB means two things to me, a) changing the existing culture to b) allow an engineering focused culture to emerge.

Changing culture is hard but there's a lot of industry and academic research on the subject. It may seem obvious but I was surprised to learn that the way to change culture is "not to first change how people think, but instead to start by changing how people behave - what they do" (John Shook reflecting on General Motors / Toyota cultural reinvention). Additional research correlates a lot of lean practices to positive cultural change as outcomes. The implication is that if we **eliminate waste, reduce inventory** and follow continuous improvement, a move towards a more generative culture will follow. This seems easier than I thought, just follow the agile manifesto no?

## Westrum's Organisational Cultural Topology
 

Ron Westrum defined a useful model to define organisation cultures. His research focused information flows within organisations as a predictive measure of software development performance. Good culture is predictive of good outcomes. Accelerate supports these ideas and bolsters them with concrete practices that are again, predictive of good outcomes.

 

Based on [his model](https://qualitysafety.bmj.com/content/13/suppl_2/ii22.short) below, what do you think our culture looks like now?

| Pathological Culture           | Bureaucratic Culture      | Generative Culture *           |
|--------------------------------|---------------------------|--------------------------------|
| **Power oriented**             | **Rule oriented**         | **Performance oriented**       |
| Low co-operation               | Modest co-operation       | High co-operation              |
| Messengers "shot"              | Messengers neglected      | Messengers trained             |
| Responsibilities shirked       | Narrow responsibilities   | Risks are shared               |
| Bridging discouraged           | Bridging tolerated        | Bridging encouraged            |
| Failures lead to scapegoating  | Failure leads to justice  | Failures lead to inquiry       |
| Novelty (innovation) crushed | Novelty leads to problems | Novelty implemented (valued) |

^ Westrum's topology of organisational cultures

* In generative cultures, leaders place emphasis on accomplishing organisational goals and outcomes, rather than on personal gain or rules (typical to performance-oriented cultures)

## Focus on Practices and Measurements

Shook and DevOps Research and Assessment (DORA) group's research agree that simple steps to encourage the (non-bold) characteristics in the generative column can lead to cultural change. For example, encouraging bridging is about breaking down silos through physical co-location, cross functional teams (negating Conway's Law) and networking. Bringing in XP practices can lead to high co-operation, lean principles lead to a performance oriented focus and so on.

 

I really liked Westrum's views on how to measure cultural change, he points out that it is a **perceptive measure** and so questionnaires are the best mechanism by which to measure. We can use this when experimenting to measure the success of any initiative we try (another lean principle). He suggests the following survey (scored 1-7 when aggregating to give a quantitative result).

 

| Statement                                                                        | Strongly Disagree | Disagree | Somewhat Disagree | Neither Agree nor Disagree | Somewhat Agree | Agree | Strongly Agree |
|----------------------------------------------------------------------------------|-------------------|----------|-------------------|----------------------------|----------------|-------|----------------|
| On my team, information is actively sought                                       |                   |          |                   |                            |                |       |                |
| Messengers are not punished when they deliver news of failures or other bad news |                   |          |                   |                            |                |       |                |
| On my team, responsibilities are shared                                          |                   |          |                   |                            |                |       |                |
| On my team, cross-functional collaboration is encouraged and rewarded            |                   |          |                   |                            |                |       |                |
| On my team, failure causes inquiry                                               |                   |          |                   |                            |                |       |                |
| On my team, new ideas are welcomed                                               |                   |          |                   |                            |                |       |                |


## The Big 3 Levers
 

I think particularly relevant to our firm, three cultural capabilities seem to affect culture more significantly than others. As levers, DORA assert that the following have been shown to drive organisational culture.

`TRUST -> VOICE -> AUTONOMY`

They feel intuitive. That trust can neutralize a fear culture, that voice empowers individuals and validates self-worth and autonomy promotes initiative (doing the right thing without being told) and innovation. All of them feed into the generative capabilities of Westrum's topology and should in my view, be our focus.

| Desired Outcome | Antithesis          | Discussion and examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Autonomy        | Command and control | Deming's work supports the need for autonomy and purpose - the two go hand in hand. Leaders are in a position to affect this straight away by how they behave. In autonomous teams, leaders demonstrate the fulcrums below                                                                                                                                                                                                                                                                |
| Trust           | Fear                | As an industry, investment banking does not have the public's trust - this manifests as a deeply ingrained fear culture in the majority of banks. I think it stems from the horror stories (like our involvement in CDO market) and the power over entire economies the big institutions hold. It's evidenced by the need to regulate.<br/><br/>Misconceptions around governance, driven by misunderstanding regulation or audit interpretation can also contribute to a feature culture. |
| Voice           | Not listening       | The measure of how strongly individuals and teams feel about their ability to speak up both with bad news, during conflict and with positive suggestions on improvement. For me, this is really about how much people feel they are heard. Nobody likes to feel marginalised and feeling like you are contributing ideas and suggestions has a huge affect on morale or worth.<br/><br/>This is driven by autonomy and trust.                                                             |

### Autonomy Fulcrums

- Communicate goals or outcomes, let teams decide how to achieve them
- Allow teams to prioritise good outcomes for customer, even if it means bending the "rules". This has direct bearing 
  - when deciding if dev teams should use centrally provided infra like Teamcity and BitBucket or host their own
  - when allowing teams to attest source code reviews are taking place without mandating central tooling (in this case, the central solution doesn't support pull requests and so inhibits trunk based development - this takes away choice and autonomy)
  - mandating languages, frameworks, libraries (just don't do this)
- Eliminate all targets (Deming's point 10) and by implication measures (like code commit statistics). This kind of measures are powerful tools in internal reflection and improvement (i.e. at the team level) but do not scale well to the enterprise.

### Trust Fulcrums

- Encouraging inquiry, trusting dev teams to self attest that they can demonstrate regulation having shown they actually understand it (stopping the dogma)
- Give problems to the experts. Put another way, delegate the problems to the teams in the trenches and trust them
- Deming's point 8 (drive out fear) and associated material (you'll have to do some of your own reading here to find specific examples / techniques)_
- Encourage "messengers" (never "shoot the messenger"), favor postmortems, retrospectives and continuous improvement over blame
- Share risks.


 ## What's next
 How else can we affect these levers and what impact can they have to the generative culture characteristics above? You tell me in the comments below.

 Further Reading
 

Summary of DORA research (http://services.google.com/fh/files/misc/dora_research_program.pdf)
Westrum's 2004 research (https://qualitysafety.bmj.com/content/13/suppl_2/ii22)
Google Cloud / DevOps compendium (cultural change section) https://cloud.google.com/solutions/devops/devops-culture-westrum-organizational-culture
How to transform (DevOps culture) inc PDCA https://cloud.google.com/solutions/devops/devops-culture-transform
Author of Brave New World talking at Google (via Marco Milone)