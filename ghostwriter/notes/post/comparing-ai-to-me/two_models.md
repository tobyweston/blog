# Model 1 — **Feature Value Index (FVI)**

*A commit-signal productivity model*

This model estimates delivery throughput using **observable Git signals** instead of lines-of-code.

It attempts to approximate how much **real product work** occurred in a window by weighting different commit categories.

## Inputs

For each repo window:

* `feature` = feature-like commits
* `new_code` = new code files added
* `new_tests` = new test files added
* `reliability` = CI/test/reliability commits

These signals are **normalized across repos** to the maximum observed value.

## Algorithm

```
feature_norm      = feature / max(feature)
new_code_norm     = new_code / max(new_code)
new_tests_norm    = new_tests / max(new_tests)
reliability_norm  = reliability / max(reliability)

FeatureValueIndex =
    100 * (
        0.45 * feature_norm +
        0.25 * new_code_norm +
        0.20 * new_tests_norm +
        0.10 * reliability_norm
    )
```

## Rationale

Weights were chosen to reflect delivery importance:

| Component       | Weight  | Reason                                  |
| --------------- | ------- | --------------------------------------- |
| Feature commits | **45%** | Most direct proxy for user-visible work |
| New code files  | **25%** | Captures structural expansion           |
| Test files      | **20%** | Indicates operational hardening         |
| Reliability/CI  | **10%** | Signals production readiness            |

This produces a normalized score between **0 and 100**.

## Interpretation

Higher FVI means:

* more features shipped
* more code created
* more tests and reliability scaffolding

But it still remains a **proxy metric**.

---

# Model 2 — **Feature Size Score → Feature Points (FSS/FP)**

*A capability/initiative productivity model*

This model measures productivity by **sizing initiatives**, similar to story points but designed for **engineering systems work**.

Instead of counting commits, it measures **how big the shipped capabilities were**.

## Initiative scoring dimensions

Each initiative is scored **1–5** on five dimensions.

| Dimension                 | Weight  | Meaning                                 |
| ------------------------- | ------- | --------------------------------------- |
| Novel Capability (N)      | **30%** | Is this something fundamentally new?    |
| Technical Depth (D)       | **25%** | Architectural or algorithmic complexity |
| Surface Breadth (B)       | **20%** | How much of the system it touches       |
| Operational Hardening (O) | **15%** | Tests, CI, packaging, release readiness |
| User/Product Impact (U)   | **10%** | Visible value to users                  |

---

## Algorithm

```
FeatureSizeScore (FSS) =
    20 * (
        0.30 * N +
        0.25 * D +
        0.20 * B +
        0.15 * O +
        0.10 * U
    )
```

This produces a score between **0–100**.

---

## Mapping to Feature Points

The FSS score is converted into **Feature Points (FP)**:

| FSS Range | Size | Feature Points |
| --------- | ---- | -------------- |
| ≥ 85      | XXL  | 13             |
| 70–84     | XL   | 8              |
| 55–69     | L    | 5              |
| 40–54     | M    | 3              |
| 25–39     | S    | 2              |
| <25       | XS   | 1              |

Total productivity for a time window is:

```
TotalFeaturePoints = sum(FP for all initiatives)
```

---

# The key difference between the models

| Model               | What it measures         |
| ------------------- | ------------------------ |
| Feature Value Index | **delivery signals**     |
| Feature Size Score  | **initiative magnitude** |

So they answer different questions.

**FVI asks:**

> How much delivery activity occurred?

**FSS/FP asks:**

> How large were the things that were shipped?

---

# Why both models are useful

Using both avoids the classic productivity traps.

### If you only use commits

You measure **activity**.

### If you only size initiatives

You measure **impact**.

Using both gives you:

```
productivity ≈ activity × initiative size
```

Which is why your results showed:

| Model          | Result             |
| -------------- | ------------------ |
| FVI            | ~2.0× productivity |
| Feature Points | ~2.8× productivity |

