---
name: Typical Audit Structures
slug: typical-audit-structures

topics:
- risk
- governance
- compliance
- controls
- audit
- banking

when_to_use:
- when the topic requires additional context around how organisations structure risk management
- when discussing governance, risk management or regulatory environments
- when explaining how responsibilities for controls and oversight are distributed
- when there is mention of first line of defence (1LoD), second line of defence (2LoD) or third line of defence (3LoD)
- when explaining accountability structures in regulated organisations

summary: >
  Many regulated organisations, particularly banks, structure their risk
  management responsibilities around the "Three Lines of Defence" model.
  The model separates responsibility for taking risk, overseeing risk, and
  independently assuring that controls and governance are effective.
  This separation prevents conflicts of interest and ensures that those
  who operate systems and processes are not the same people responsible
  for independently assessing their effectiveness.

key_claims:
- Risk management responsibilities are typically structured around the Three Lines of Defence model
- The model separates risk ownership, risk oversight, and independent assurance
- The purpose of the model is separation of responsibilities to avoid conflicts of interest
- Each line has distinct responsibilities and should not perform the roles of the others
- Effective governance depends on clear accountability across the three lines

argument_patterns:
- Introduce the Three Lines of Defence model as a common governance structure
- Explain the responsibilities of the first, second, and third lines
- Clarify the separation of duties between operating controls, overseeing risk, and auditing effectiveness
- Use the model to explain where specific governance or control responsibilities sit within an organisation

example_phrasing:
- "Most regulated organisations structure their risk management around the Three Lines of Defence model."
- "The first line of defence consists of the business units that own and operate the systems and processes where risk arises."
- "The second line provides oversight, setting risk frameworks and challenging the effectiveness of the controls operated by the business."
- "The third line, internal audit, provides independent assurance to senior management and the board."
- "The purpose of the model is to separate risk ownership, oversight and assurance."

guardrails:
- Do not imply that the lines perform each other's responsibilities
- Avoid suggesting that second line functions operate day-to-day controls
- Avoid suggesting that internal audit designs controls or creates governance standards
- Ensure the independence of the third line is maintained in explanations
- Keep the focus on separation of responsibilities rather than organisational hierarchy
---

```mermaid
flowchart TD

A["External Obligations<br/>(Laws, Rules, Regulation)"]

B["Regulatory Interpretation<br/>(2LoD)"]

C["Risk Taxonomy<br/>(2LoD)"]

D["Frameworks & Policy<br/>(2LoD)"]

E["Minimum Control Standards<br/>(2LoD)"]

F["Controls<br/>(1LoD)"]

G["Evidence & Monitoring<br/>(1LoD + 2LoD)"]

H["Independent Assurance<br/>(3LoD)"]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
```