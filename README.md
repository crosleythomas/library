---
layout: default
title: Artificial Intelligence Library
---

# Artificial Intelligence Library
There are a lot of great resources these days for finding academic research, such as <a href="semanticscholar.org">Semantic Scholar</a>, <a href="https://arxiv.org/">arXiv</a>, and <a href="http://www.arxiv-sanity.com/">Arxiv Sanity Preserver</a>.<br><br>
These sites are all great but can get a bit unwieldy.  Sometimes, what you really need is a librarian to point you right where you should be.  This repository is meant to be a more curated and selective collection of the most interesting AI papers being published.

## Format
library/<br>
library/topic<br>
library/topic/readme.md -- list of papers related to this topic [year, title (w/ hyperlink), authors, affiliation, code, other relevant links]<br>
library/topic/papers -- stored papers<br>

library/topic/subtopic -- more specific subtopic of topic (i.e. library/rl/model_based_rl )<br>
library/topic/subtopic/readme.md -- list of papers related to this subtopic of topic [year, title (w/ hyperlink), authors]<br>
library/topic/subtopic/papers -- stored papers<br>

Every new topic should have:
1. README.md
2. papers/

The easiest way to create a new topic is:
```
cp -r template <topic_name>
```
Then replace as necessary.

## Guidelines
* **Duplicates are okay!**  One paper can fall under multiple topics.  Err on the side of over-duplication rather than under-duplication.  If a paper discusses both more than one topic, list it under all of them.</li>
* **Keep tables chronologically sorted.** Trends are important, let the arc of thinking let us know what we're missing.
* **Contributions welcome!** 

