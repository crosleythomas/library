---
layout: default
title: Artificial Intelligence Library
---

# Artificial Intelligence Library
There are a lot of great resources these days for finding academic research, such as <a href="semanticscholar.org">Semantic Scholar</a>, <a href="https://arxiv.org/">arXiv</a>, and <a href="http://www.arxiv-sanity.com/">Arxiv Sanity Preserver</a>.<br><br>
These sites are all great but can get a bit unwieldy.  Sometimes, what you really need is a librarian to point you right where you should be.  This repository is meant to be a more curated and selective collection of the most interesting AI papers being published.

## Repository Structure
library/<br>
library/topic<br>
library/topic/readme.md -- list of papers related to this topic [year, title (w/ hyperlink), authors, affiliation, code, other relevant links]<br>
library/topic/papers.txt -- list of paper titles with their arxiv link for offline download
library/topic/papers -- stored papers (after running the pull.py script locally)<br>

library/topic/subtopic -- more specific subtopic of topic (i.e. library/rl/model_based_rl )<br>
library/topic/subtopic/readme.md -- list of papers related to this subtopic of topic [year, title (w/ hyperlink), authors]<br>
library/topic/subtopic/papers.txt -- list of paper titles with their arxiv link for offline download
library/topic/subtopic/papers -- stored papers (after running the pull.py script locally)<br>

Every new topic should have:
1. README.md
2. papers.txt
3. papers/

## Structure
When adding a new paper:
1. Add it into the table (chronologically!) of the appropriate topic, or set of topics.
2. Save the paper's title and arxiv link (or other stable link) into the papers.txt file

## Creating a new topic:
```
cp -r template <topic_name>
```
Then replace as necessary.

## Pulling Papers
To keep the repository from getting unusably large, the repo only stores links to PDFs, not the PDFs themselves.<br>
To get all the papers locally run the pull script:
```
python pull.py
```

To clear out all old papers there is a clear script as well:
```
python clear.py
```

## Guidelines
* **Duplicates are okay!**  One paper can fall under multiple topics.  Err on the side of over-duplication rather than under-duplication.  If a paper discusses both more than one topic, list it under all of them.</li>
* **Keep tables chronologically sorted.** Trends are important!
* **All resources welcome.** Blog posts, Jupyter notebooks, lecture slides, etc. are all welcome in this repository. 
* **Contributions welcome!** 

