---
name: Software Supply Chain Risk vs Operational Risk
slug: supply-chain-vs-operational-risk

topics:
- risk
- software-delivery
- operations
- governance
- software-supply-chain

when_to_use:
- when distinguishing risks in the software supply chain from risks in live operation
- when CI/CD pipelines are being used to enforce operational governance
- when discussing deployment trust, release safety or SDLC governance
- when explaining why control placement matters
- when discussing day-zero events or risks introduced outside the SDLC

summary: >
  Software supply chain risk and operational risk are related but distinct.
  The software supply chain concerns whether we can trust the artefacts we
  are about to deploy. Operational risk concerns whether systems should be
  allowed to operate or change at all. Many organisations blur these
  categories and attempt to enforce operational concerns within CI/CD
  pipelines. This often results in poorly designed controls that fail to
  address real operational risk.

key_claims:
- Controls should match the type of risk they are intended to manage.
- Software supply chain risk concerns the trustworthiness of artefacts produced by the SDLC.
- Operational risk concerns the safety and stability of systems running in production.
- CI/CD pipelines are well suited to enforcing supply chain trust but poorly suited to enforcing operational governance.
- Separating these risk categories leads to clearer and more effective control design.

argument_patterns:
- introduce a governance or control problem in the SDLC
- show how operational and supply chain risks are being conflated
- separate the two risk categories conceptually
- explain how different control mechanisms apply to each risk type
- demonstrate how clearer categorisation improves governance and risk management

example_phrasing:
- "The key question for the software supply chain is simple: can we trust what we are about to deploy?"
- "Operational risk asks a different question: should this system be allowed to operate or change at all?"
- "CI/CD pipelines are good at establishing trust in artefacts, but they are a poor framework for managing operational risk."
- "Many organisations attempt to enforce operational policy inside pipelines, which leaves material risks unaddressed."
- "A release gate can stop a deployment, but it cannot protect you from a vulnerability discovered the next day."
- "CI/CD is a good place to enforce supply chain trust, but a poor place to enforce operational safety."
- Supply chain risk mental model is “Can we trust what we're about to deploy?”
- Operational risk mental model is “Should this system be allowed to operate or change at all?”

guardrails:
- avoid treating risk as a single undifferentiated concept
- avoid implying that CI/CD pipelines can manage all operational risk
- include concrete examples such as day-zero vulnerabilities or disaster recovery failures
- emphasise that operational risks can arise outside the SDLC

risk_model:
  Software Supply Chain Risk:
    description: >
      Risks associated with producing trustworthy software artefacts through
      the SDLC, including source control, dependency management, build
      systems, artifact creation and deployment assurance.
    mental_model: "Can we trust what we are about to deploy?"
    typical_controls:
    - signed commits and trusted developers
    - dependency management and provenance
    - reproducible builds
    - artifact integrity and signing
    - verified deployment pipelines

  Operational Risk:
    description: >
      Risks associated with running systems safely in production, including
      events or failures that occur outside the software delivery process.
    mental_model: "Should this system be allowed to operate or change at all?"
    typical_examples:
    - day-zero vulnerabilities
    - operational misconfiguration
    - disaster recovery failures
    - environment onboarding procedures
    - runtime policy enforcement
---