---
layout: post
title:  Modular Latex
date:   2019-05-17
permalink: /modular-latex/
categories: latex
---

![typewriter](/assets/images/typewriter.gif)

## Modular Latex

Recently I was tasked with typing up the notes for a course in my department.
Each week I would attend class, typeset notes, and distribute them to students.
At the end of the semester I compiled the notes into a single document.  I
wanted this document to be built in a modular way rather than a large
monolithic tex file.  I mostly referred to a wiki [LaTeX/Modular
Documents](https://en.wikibooks.org/wiki/LaTeX/Modular_Documents) for advice on
how to set up a project.  I wanted to document my process as well as build a
template for future projects. 

Here is what I would like in a modular latex document:
- A main file to handle macro document structure
- Separate directory for tex content
- Separate style file for package imports and configuration
- A flexible bibliography
- Source code for tikz figures


**Note**: The method outlined here is subject to change in the future and
should be thought of as a record of what I did rather than the correct way of
doing things. 

### Version Control

I figure I should be version controlling everything these days.

```
git init new-project
```

Latex projects tend to generate a bunch of intermediate files during compilation.
I need a solid `.gitignore` file in order not to make version control a mess.
I used [github/gitignore/TeX.gitignore](https://github.com/github/gitignore/blob/master/TeX.gitignore)
as a starting place to cover most of the default output.

I added a few extras as well to suite my needs such as `*.swp` for vim's swap
files, and a folder `tmp` for my own temporary file needs.


### Project Structure

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

#### Main 

`main.tex` is the where the main structure of the document is established. All
that is done here is read in our style file, begin the document, input the tex
content, print the bibliography, and end the document. The macro level arrangement
of chapters can be adjusted here by moving the input statements around. This file 
can be thought of as a table of contents for your modular document. 

#### Style

`main.sty` is where all the package imports are done and the details of the
formatting options are set. It is continent to break the preamble into a separate
file because they tend to grow large for big projects.

#### Bibliography

`main.bib` contains all of the bibliographic information. In the past I have
used [JabRef](http://www.jabref.org/) for managing references but going forward I am 
not sure what the best option for me is. 

#### Content

The `tex` folder contains the main content of the project. Separate files could
include major sections of your document, or chapters. Breaking up content into
separate tex files improves version control and also helps to group concepts. 

#### Figures

`fig` is where I store all the information related to figures. I like to keep
the tikz source code as well as any images used in figures in this directory.
Typically I will try to name the files after which sections they are expected
to be in for better sorting. For example `LinAlg-SVD.tex` might contain the
tikz source for a figure about the SVD used in a chapter on linear algebra.

#### Make

`Makefile` is a rough  make file to compile the document. It is included to
alleviate some confusion when sharing the document with others.  I recommend to use
the function `latexmk` instead of this make file though. 

```
latexmk main.tex
```

Latexmk is a much more
robust program for compiling latex documents and is usually included in your LaTeX distribution. 

#### Other

The `LICENSE` and `README.md` are up to you to include. I think it's nice to include compilation instructions
in a readme for reference.

## Lessons Learned

Bibliographies can be a pain to fiddle with. In the past I had used `bibtex`
with relative success.  Every time I go to look up LaTeX bibliography
information it seem there are different suggestions.  This time on the overleaf
article [Bibliography management with
bibtex](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex)
I found a note:

    Note: If you are starting from scratch it's recommended to use biblatex since
    that package provides localization in several languages, it's actively
    developed and makes bibliography management easier and more flexible.

I found other tutorials which suggested using
[natbib](https://www.overleaf.com/learn/latex/Bibliography_management_with_natbib)
I figured since I _am_ starting from scratch I better give `biblatex` a try. At
first everything was fine, but then the next day nothing would compile.  I just
spent an hour and a half pulling my hair out over why my bibliography wasn't
working.  Turns out some `biber` cache file got corrupted. I deleted the cache
and everything worked again!  (In the future see [Troubleshooting for
biber](https://tex.stackexchange.com/questions/286706/troubleshooting-for-biber/287811)
for help. Specifically the section titled "The Infamous Cache Bug".)

Another lesson learned was as the document grows, so does compilation time.
What I would do is comment out input statements in `main.tex` to focus on
specific chapters. Then run a full compilation at the end to see how everything
fit together.  If this becomes a problem, one way to improve compilation time
would be to pre-compile the figures only use their outputs in the main
document. 

## Project Template

I created a project template on github at
[eitanlees/latex-project-template](https://github.com/eitanlees/latex-project-template)
to be used as a starting place for future projects.

I hope this has been helpful to you dear reader!

(Most likely only I will be using this for future reference.)
