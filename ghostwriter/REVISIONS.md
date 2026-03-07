# Ghostwriter CLI Revisions

Each mode tells the model **what kind of editor it should behave like**.

You should almost never do a full rewrite. Instead run **small targeted revisions**.


# Revision Philosophy

The workflow is:

```
Plan → Draft → Targeted edits
```

Instead of:

```
Plan → Draft → Rewrite → Rewrite → Rewrite
```

The modes encourage **surgical improvements**.



# 1. `tighten`

**Purpose**

Remove fluff and improve clarity.

**What it does**

* removes filler sentences
* shortens explanations
* reduces repetition
* improves paragraph flow
* keeps your meaning intact

**Typical effect**

```
20–30% shorter
clearer sentences
faster reading
```

**Example**

Before:

> Many organisations today are attempting to introduce governance mechanisms that attempt to reduce risk in the software development lifecycle.

After:

> Many organisations introduce governance mechanisms to reduce risk in the software lifecycle.

Same meaning. Less friction.

**When to use**

Almost always as a first pass.



# 2. `stronger-hook`

**Purpose**

Improve the opening of the article.

**What it does**

* rewrites the introduction
* clarifies the central problem
* creates tension or curiosity
* makes the reader want to continue

**Example**

Before:

> In this article we will explore the challenges of compliance in software delivery.

After:

> Compliance is supposed to reduce risk.
> Yet in many organisations it does the opposite: it slows developers down while giving leadership a false sense of safety.

**When to use**

When the intro feels **generic or flat**.



# 3. `more-like-me`

**Purpose**

Push the article closer to **your authentic voice**.

**What it does**

* emphasises reasoning
* adds subtle contrarian tone
* removes generic AI phrasing
* improves argument structure

**Typical changes**

* more opinion
* stronger statements
* clearer reasoning chains

**Example**

Before:

> Code reviews are important because they help improve quality.

After:

> Code reviews are often described as a quality mechanism.
> In practice they are something more important: an **evidence system**.

**When to use**

When the draft feels **AI-ish or neutral**.



# 4. `less-tutorial`

**Purpose**

Reduce "how-to article" tone.

Your blog is **not a tutorial site**.

It is **engineering thinking and analysis**.

**What it does**

Removes things like:

```
Step 1
Step 2
Step 3
```

and replaces them with:

```
argument
analysis
framework
implications
```

**Example**

Before:

> Step 1: configure your pipeline
> Step 2: add code review
> Step 3: measure lead time

After:

> Organisations often attempt to improve delivery by adding more controls to the pipeline.
> The problem is that these controls usually generate assertions rather than evidence.

**When to use**

When the draft reads like **Dev.to or Medium tutorial content**.



# 5. `more-opinionated`

**Purpose**

Strengthen the thesis.

Adds stronger positions and clearer judgement.

**What it does**

* removes hedging
* clarifies what you actually believe
* sharpens the argument

**Example**

Before:

> It may be beneficial for organisations to consider trunk-based development.

After:

> Organisations that care about delivery performance should adopt trunk-based development.

**When to use**

When the draft feels **too safe**.



# 6. `add-framework`

**Purpose**

Strengthen the structure using one of your frameworks.

Examples:

```
trust lifecycle
delivery vs runtime risk
evidence vs assertion
```

**What it does**

* introduces a framework section
* reorganises argument around it
* clarifies mental models

**Example**

Before:

General discussion about governance.

After:

```
Establish Trust
Verify Trust
Maintain Trust
```

**When to use**

When the article needs **structure**.



# Recommended Revision Strategy

Usually:

```
1 tighten
2 stronger-hook
3 more-like-me
```

Occasionally:

```
tighten
less-tutorial
more-opinionated
```



# Example Real Workflow

```
gw new "Why compliance fails developers"
```

Then:

```
tighten
```

Then:

```
stronger-hook
```

Then maybe:

```
more-like-me
```

Then evaluate.



# One Important Rule

Never stack too many revisions.

Max recommended:

```
2–3 passes
```

Otherwise the model starts **overfitting its own edits**.



# My Personal Default

If I were using this system daily, I would almost always run:

```
tighten
```

Then decide between:

```
stronger-hook
```

or

```
more-like-me
```



If you want, I can also show you **one extremely powerful additional revision mode** that fits your blog style perfectly:

```
sharpen-argument
```

It dramatically improves the **central idea of the article** and works very well for thought-leadership style writing.
