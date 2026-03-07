---
name: Delivery vs Runtime Risk
slug: delivery-vs-runtime-risk
topics:
- risk
- software-delivery
- operations
- governance
when_to_use:
- when distinguishing risks in the SDLC from risks in live operation
- when control design gets muddled across delivery and runtime
summary: >
Delivery risk and runtime risk are related but distinct. Teams often design controls badly
because they fail to separate the risk of changing software from the risk of running it.
key_claims:
- Controls should match the type of risk they are intended to manage.
- Delivery controls are about the trustworthiness of change.
- Runtime controls are about the trustworthiness of operation.
argument_patterns:
- introduce a risk or control problem
- show how two different risks are being conflated
- separate delivery risk from runtime risk
- explain how control design improves once the distinction is clear
example_phrasing:
- We often talk about risk as though it were one thing. It isn't.
- The risk of shipping change is not the same as the risk of operating software.
- Better distinctions lead to better controls.
guardrails:
- avoid becoming too abstract
- give concrete examples of each risk type