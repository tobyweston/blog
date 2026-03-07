---
name: Evidence vs Assertion
slug: evidence-vs-assertion
topics:
- assurance
- compliance
- controls
- code-review
when_to_use:
- when discussing assurance, policy, auditability, or control design
- when teams are relying on stated process rather than demonstrated evidence
summary: >
Engineering organisations often confuse asserted process with demonstrated reality.
Reliable governance depends on evidence, not just policy statements or intent.
key_claims:
- Saying something happens is not the same as proving it happened.
- Good controls generate usable evidence as a side effect of normal work.
- Manual attestations are weak compared to automated, traceable evidence.
argument_patterns:
- start from a policy or control requirement
- show how assertion-based compliance fails
- contrast manual attestation with observable engineering evidence
- recommend designing systems that emit trustworthy evidence
example_phrasing:
- Policy without evidence is just aspiration.
- The important question is not what teams say they do, but what the system can show.
- Good governance should leave a trail.
guardrails:
- avoid implying that policy is useless
- position evidence as the thing that makes policy operational