---
layout: post
title: "Evidencing Source Code Reviews"
date: 2019-10-30 08:16
comments: true
categories: 
sidebar: false
published: false
keywords: "mas, monetary authority of singapore, technology risk management guidelines, crypto-evidence"
description: ""
---

Many industries need to evidence that code reviews have taken place. This is typical in regulated environments like Banking but the Regulators aren't clear what constitutes a good source code review process and don't yet understand modern practices like Pair Programming. They can't help you streamline your process.

The result is a tension between old-fashioned bureaucracy and modern development practices; the need to prove you have a rigorous process in-place and the desire to push frequent releases to production without wasteful paperwork. 

Amazon have thousands of "applications" and deploy to production every 2 seconds*. How would they demonstrate that each has been the subject of a thorough code review without constantly producing reams of documentation?

<!-- more -->

## The Regulators

The Monetary Authority of Singapore (MAS) is Singapore's central bank and regulatory authority. If you want to do business in Singapore, you need to comply with their regulations. They've published what they call the Technology Risk Management (TRM) Guidelines to help with "the adoption of sound practices and processes for managing technology". Each financial institution with an interest in Singapore is expected to adopt these guidelines with the following caveat.

{% blockquote Monetary Authority of Singapore, TRM Guidelines - section 2.0.1 %}
"Financial institutions (FIs) may adapt these guidelines, taking into account the diverse activities they engage in and the markets in which they conduct transactions. FIs should read the Guidelines in conjunction with relevant regulatory requirements and industry standards."
{% endblockquote %}
 
One area of the TRM guidelines talks about the need to conduct code reviews (section 6.3). Each institution must interpret these guidelines and be comfortable articulating how the manage the source code review process. The TRM guidelines don't say *how* to conduct reviews and doing effective code reviews is hard.

Regulators struggle to keep up with modern software development practices and how they can help give confidence that guidelines are being followed. They struggle to assess the impact of things like containerised deployments and having data on the public cloud. For source code reviews, each institution must adapt the guidelines to fit their development practices but at a minimum, each should be able to provide evidence. 


## Evidence

So how do we evidence that code reviews have taken place? A traditional process would be to conduct an out-of-band code review (after the coding task has been completed) and document it via some tool like Codacy or Crucible. GitHub (and GitHub Enterprise) have nice integrated review tools and BitBucket have something similar. These are often combined with the act of merging a Pull Request, i.e. you do the code review when you accept a PR.

### Trunk Based Development vs Branch 

Tools that combine merging branches with code reviews __conflate two distinct ideas__ (managing your source code and peer reviewing source code). If you do both actions together, your branching model has been chosen for you and doing trunk based development (TBD) becomes harder. If you do try for TBD and use short lived branches purely to facilitate code reviews, __you're introducing waste__ (albeit the cost may be reclaimed somewhat by the tooling that motivated the decision).

Trunk based development has lots of advantages in it own right, not least of which is that it offers __continuous integration__ (CI). CI has been around since the early 90s and helps reduce the feedback loop for dev teams. Compared to long running feature branches where by definition, integration takes place intermittently and infrequently, it helps find potential problems early.

{% blockquote Martin Fowler, Chief Scientist @ ThoughtWorks %}
"Continuous Integration doesn’t get rid of bugs, but it does make them dramatically easier to find and remove."
{% endblockquote %}

### Pair Programming vs Code Reviews

Pair Programming as an alternative to traditional out-of-band code reviews offer significant advantages. Again, mostly this is around __shortening the feedback loop__ and fixing potential problems early. If code reviews are a good idea, why not do them all the time? When you're actually coding and not when you've finished?

So how do you practice trunk based developed, utilise Pair Programming and still provide evidence that you've had multiple developers work on a single piece of code? Perhaps crypto-evidence can help?


## Crypto-evidence

Crypto-evidence is a term I made up for this post but it implies that we should be able to supply evidence that can be proven via cryptographical means. With traditional techniques, a code reviewer can be proven to be who she says she is (and that she's a different person than the original author) by the login credentials they used with the review and VCS tools. These would be encrypted and so (in theory) can not be subverted or faked. Assuming the rest of the review is locked down, we have our evidence.


### Git Digital Signatures

Git is probably the most widely used VCS today (some figures suggesting it's used by 70% of projects). It offers a feature called **signed commits** whereby the person committing code digitally signs the commit with GPG. This can be retrieved (along with the author information) and, in theory, prove a different individual "signed" a commit than it's author. This signature could be used as a sign-off for a code review. Just use `-S` (not `-s`):

```bash
$ git -S -m "initial commit"
```

...and verify with `git log --show-signature`:

```bash
$ git log --show-signature
commit d001cb9e78a2dbf4ce8ddad3eb2fe8b14234e3c5 (HEAD -> master)
gpg: Signature made Wed 30 Oct 12:37:18 2019 GMT
gpg:                using RSA key 39E273602
gpg: Good signature from "Toby (baddotrobot.com) <toby@badrobot.com>" [ultimate]
Author: Toby <toby@badrobot.com>
Date:   Wed Oct 30 12:37:18 2019 +0000

    initial commit

```

The key line includes `Signature made ... using RSA key 39E273602`. Evidence, job done. Not quite...


### Proving Pair Programming

I brushed over a little bit there. Assuming we want to prove Pair Programming was being done, we need to show an alternative author from the signatory. We can do that either supplying the `--author` argument or (more practically) sharing the team's private keys securely and signing based on who's at the computer.

1. On Toby's computer (the default key is Toby's set with `git config --global user.signingkey 39E273602`) and Barry pairing:

   ```bash
   $ git commit -S --author="Barry <barry@badrobot.com>" -m "commit from Toby's machine with Barry as the author"
   ```

1. Or if each machine has each developer's private key installed in GPG and from Barry's machine (Toby pairing):

   ```bash
   $ git commit -Stoby -m "commit as Barry with Toby signing the commit"
   ```
   
Both would result in something like the following.

```bash
$ git log --show-signature
commit e128af7f51e272eae29cee8f1c124ec0be3b64ad (HEAD -> master)
gpg: Signature made Wed 30 Oct 12:54:49 2019 GMT
gpg:                using RSA key 39E273602
gpg: Good signature from "Toby (baddotrobot.com) <toby@badrobot.com>" [ultimate]
Author: Barry <barry@badrobot.com>
Date:   Wed Oct 30 12:54:49 2019 +0000

    commit as Barry with Toby signing the commit

```

When you force each commit to be signed, you should be able to build a report from the Git log showing every commit was paired on.

```bash
git config --global commit.gpgsign true
```

### Sharing and Importing Secrets

To share private keys, export your key (you may choose to share this via Git alongside your source code).

```bash
$ gpg --export-secret-key --armor toby@badrobot.com > secretkey_toby.asc
```

...and import it on each developer's machine. 

```bash
gpg --import secretkey_toby.asc
```

Just pass in the name you used when creating the key to the `-S` argument. In my case `-Stoby`.

## References

*As of 2009

* [Git adoption figures](https://softwareengineering.stackexchange.com/questions/136079/are-there-any-statistics-that-show-the-popularity-of-git-versus-svn)
* [TBD vs Branching](https://www.toptal.com/software/trunk-based-development-git-flow)


[Technology Risk Management Guidelines](https://www.mas.gov.sg/-/media/MAS/Regulations-and-Financial-Stability/Regulatory-and-Supervisory-Framework/Risk-Management/TRM-Guidelines--21-June-2013.pdf)


## Miscellaneous Setup

To test your GPG program, run the following.

```bash
$ echo "test" | gpg --clearsign
```

If the output includes the following.

```bash
gpg: signing failed: Inappropriate ioctl for device
gpg: [stdin]: clear-sign failed: Inappropriate ioctl for device
```
You may need to run the following (I did on MacOSX).

```bash
$ export GPG_TTY=$(tty)
```