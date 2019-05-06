---
layout: post
title:  Modular Latex
date:   2019-05-02
permalink: /modular-latex/
categories: latex
---

![typewriter](/assets/images/typewriter.gif)

## Modular Latex

Recently I was tasked with typing up the notes for a course in my department. 
Each week I would attend class, typeset notes, and distribute them to students. 
At the end of the semester I compiled the notes into a single document. 
I wanted this document to be built in a modular way rather than a large monolithic
tex file.  I mostly referred to a wiki titled [LaTeX/Modular
Documents](https://en.wikibooks.org/wiki/LaTeX/Modular_Documents). 


I want to document my process as well as build a template for future projects. 

**Note**: The method outlined here is subject to change in the future and should be thought of 
as a record of what I did rather than the correct way of doing things. 


## What I want 
**Notes**
What I want to include in this post:
- Directions on how to set up a modular latex project
- explanation of the directory structure
- `biblatex` and setting up a bibliography. 

I just spent an hour and a half pulling my hair out over latex bibliographies.
Turns out some `biber` cache got corrupted. Delete the cache and everything works again
see [Troubleshooting for
biber](https://tex.stackexchange.com/questions/286706/troubleshooting-for-biber/287811)
for help. Specifically the section titled "The Infamous Cache Bug"

Links:


What I would like in a latex document. 

- A main file to handle macro document structure
- Separate style file
- A bibliography which is flexible
- Source code for figures

## Version Control

I figure I should be version controlling everything these days.

```
git init new-project
```

Latex projects tend to generate a bunch of intermediate files during compilation.
I would need a solid `.gitignore` file in order not to make version control a mess.
I used [github/gitignore/TeX.gitignore](https://github.com/github/gitignore/blob/master/TeX.gitignore)
as a starting place to cover most of the default output.

I added a few extras as well to suite my needs.


## Project Structure

![file cabinet](/assets/images/filecabinet.gif)

A template for a modular latex document is set up as follows
```
.
├── LICENSE
├── Makefile
├── README.md
├── fig
│   ├── figure-A.tex
│   └── figure-B.tex
├── main.bib
├── main.sty
├── main.tex
└── tex
    ├── section-A.tex
    └── section-B.tex

2 directories, 10 files
```

### Main 

`main.tex` is the where the main structure of the document is shown. 

### Style

`main.sty` is where all the package imports hare and the details of the formatting options. 

### Bibliography

`main.bib` contains all of the bibliographic information

### Content

The `tex` folder contains the main content of the project. 

### Figures

`fig` is where I store all the information related to figures. I like to keep the tex source in this folder. 

### Make

`Makefile` is a rough rough make file. I recommend to use `latexmk` instead of this make file. 

### Other

The `LICENSE` and `README.md` are up to you to include. I think it's nice to include compilation instructions
in a readme. 

## Lessons Learned

Bibliographies can be a pain. 
