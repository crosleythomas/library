---
layout: default
title: Artificial Intelligence Library
---

# library
Sorted accumulation of interesting reading.

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