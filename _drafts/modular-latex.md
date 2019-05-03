---
layout: post
title:  Modular Latex
date:   2019-05-02
permalink: /modular-latex/
categories: latex
---

![typewriter](/assets/images/typewriter.gif)

## Modular Latex
I want to write about my experience taking notes for ISC 4933.

What I want to include in this post:
- Directions on how to set up a modular latex project
- explaination of the directory structre
- `biblatex` and setting up a bibliography. 


Links:

I mostly referred to [LaTeX/Modular Documents](https://en.wikibooks.org/wiki/LaTeX/Modular_Documents)

What I would like in a latex document. 

- A main file to handle macro document structure
- Separate style file
- A bibliography which is flexible
- Source code for figures

## File Structure

![filecabinet](/assets/images/filecabinet.gif)

```
├── LICENSE
├── Makefile
├── README.md
├── fig
│   ├── figure-A.tex
│   ├── figure-B.tex
│   └── figure-C.tex
├── main.bib
├── main.sty
├── main.tex
└── tex
    ├── section-A.tex
    ├── section-B.tex
    └── section-C.tex
```
