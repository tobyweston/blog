---
name: Priciples of Governance Systems
slug: priciples-of-governance-systems

topics:
- controls engineering
- compliance
- governance
- controls

when_to_use:
- when the topic is about organisations designing control frameworks, governance models, or compliance systems
- when the topic leans towards how engineering can help reduce risk and improve compliance outcomes
- when we want to avoid audit attention or compliance failures

summary: >
having a single governance system is a critical design element for organisations to avoid federeated compliance. Avoid distributed governance models or centralised governance models with federated compliance (many teams answering the same compliance questions in different ways)

key_claims:
- there is one governance standard
- governance decisions are evidence-based and zero-trust
- proivenance is the primary concern and lack of provenance is a governance failure
- centralised, sealed pipelines define the supply-chain trust boundary
- controls are classified by risk type, with supply-chain risks seperated form operaitonal or runtime risks
- policy decision is seperated form policy enforcement
- governance policy is expressed as policy as code with rego as the cannonical language

argument_patterns:
- describe common patterns in organisaitons (compliance and audit)
- highlight the potential problems with these approaches
- propose a centralised model fixes these problems

example_phrasing:
- centralised governance can be let down by federated complaince
- when teams are free to evidence compliance in differing ways, the result is often low quality and diffused, attracting additional attention by auditors

guardrails:
- dont cast dispursions, but highlight the risks and trade-offs