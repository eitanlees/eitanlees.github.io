---
layout: post
title:  "Understanding The Altair Stack"
date:  2020-01-18 
categories: altair visualization python
permalink: /altair-stack/
---

<img
    src="/assets/images/vega-stack/00-all-logos.svg"
    width="800" />

## Motivation
Recently I came across a blog post by Éric Marty titled [The D3 / Vega
“stack”][stack-blog-post], in which he outlines the many packages and tools
surrounding the Vega ecosystem. His post and visuals have directly inspired my
post below.

## Standing on the Shoulders of Giants

After leading multiple workshops and showing off [Altair][altair-website] to
friends and family, I have come across a few similar questions:

- "Can I do [insert domain specific task] with Altair?"
- "Does Altair only work in [Jupyter Notebooks][jupyter-website]?"
- "How do I increase the font size?"

While tweaking font size is mostly a matter of knowing (or looking up) the
correct keyword to modify, I think having a solid understanding of the
software stack which Altair interacts with is important. The tools involved could be
visualize as follows:

<img
    src="/assets/images/vega-stack/01-d3-vega-stack.svg"
    width="800" />

This is intimidating to new users, as well as myself. If something goes wrong
in creating a visualization it could be a problem from anywhere in the stack.  On
top of that I am coming from a Python background, without much knowledge of
JavaScript and web related paradigms.

I have tried both a top down (Altair &rarr; VL &rarr; Vega &rarr; D3 &rarr; JS)
and bottom up approach when explaining how the tools interact. I am unsure which
explanation is more effective, but in my experience I am usually talking to
Python developers, and take to top down approach. 

<h3><img src="/assets/images/vega-stack/altair-logo.svg" height="40" /> <b>Altair</b>: Declarative Visualization in Python</h3>
Altair is a little different than other visualization packages in the Python
community.

From the [Altair docs][altair-quote-link]:
> Altair itself cannot render visualizations ... 
> Altair provides a Python API for generating validated Vega-Lite specifications

In other words, what Altair actually does is produce [JSON][json-website], \*cough\* \*cough\*
I mean "validated Vega-Lite specifications".  What you do as a user is specify what you want to be visualised and
pass the specification (or "spec" for short) to the browser to be rendered. 
The spec is essentially a description of the visualization. 

Altair and Vega-Lite share a (mostly) complete one to one mapping. Often I use Vega-Lite documentation when I am working with Altair.

<h3><img src="/assets/images/vega-stack/VL_Color.svg" height="25" /> <b>Vega-Lite</b>: A Grammar of Interactive Graphics</h3>

So what is this JSON file then? JSON isn't even a programming language?!

From the [Vega-Lite docs][vega-lite-website]:
>Vega-Lite is a high-level grammar of interactive graphics. It provides a
>concise JSON syntax for rapidly generating visualizations to support analysis. 

This is usually where the audience gets uneasy. I think some historical context
helps to clear things up.  In 1999 Leland Wilkinson published a book titled
[The Grammar of Graphics][gg-link] in which he outlines, in great detail, the
grammatical structure of a wide range of statistical visualizations.
Wilkinson's work was very influential in the visualization community and many
GG inspired tools were built (one popular example is the
[ggplot2][ggplot-website] library for R). I find visualization grammars to
be a fascinating subject which I am often blabbing about to my students and
colleagues. 

So back to the story, the JSON which Altair produces is a Vega-Lite spec. The
spec is a JSON file which describes the visualization using a high-level
visualization grammar. It is considered high level because some useful default
are assumed. For instance, Vega-Lite will automatically produce appropriate
scales and legends rather than you having to specify every component of your
visualization. 

Understanding the visualization grammar is <b>critical</b> in knowing what Vega-Lite
is capable of visualizing as well as Altair. 

The Vega-Lite project is more than just a specification. Vega-Lite specs are
compiled to a more detailed  Vega spec before it is rendered. The Vega-Lite
compiler is what allows for the high level JSON spec to be so expressive.

<h3><img src="/assets/images/vega-stack/VG_Color.svg" height="25" /> <b>Vega</b>: A Visualization Grammar</h3>

This is where I start to get uncomfortable. Vega specs are much more detailed.
They are still JSON files which means they are easily read but some of the high
level Vega-Lite constructs aren't provided. You have to specify every component
of the visualization. The Vega specs are actually much closer to Wilkinson's
detailed visualization grammar. The benifet of a detailed description is that
you have more flexibility. 

From the [Vega docs][vega-quote-link]:
>  Each Vega specification defines a reusable and shareable chart component.
>  Input data can also be included within a specification, resulting in
>  stand-alone definitions. In essence, Vega provides a file-format for saving
>  and sharing visualization designs.

The Vega specification is the grammatical foundations of Vega-Lite and Altair. Again 
the Vega project is more than just a specification. The Vega runtime parses the JSON and 
generates the associated visual elements in the browser using libraries such as D3.

<h3><img src="/assets/images/vega-stack/d3-logo.svg" height="30" /> <b>D3</b>: Data-Driven Documents</h3>

D3 is one of the most powerful visualization tools for the web. If you find
some awesome interactive visualization on a website there is a high probability
they are using D3 behind the scenes. In this context D3 is the library which is
actually controlling the visual elements on the screen. 

Again from the [Vega docs][vega-quote-link] explaining how Vega and D3 are related:
> During the early design of D3, we even referred to it as a “visualization
> kernel” rather than a “toolkit” or “framework”. In addition to custom design,
> D3 is intended as a supporting layer for higher-level visualization tools.

D3 is a JavaScript library. To work directly with D3 requires some
understanding of JS as well as other web concepts.  I have used D3 in the past,
but I don't have much confidence using the library. Initially D3 can be
overwhelming, but the opportunities it unlocks are substantial.  If you are
curious about learning D3 I highly recommend reading [The Trouble with
D3][d3-trouble] by Ian Johnson.


## Bringing it all together

Time for a recap! Altair is a Python library which outputs Vega-Lite
specifications (JSON). Vega-Lite is a high level visualization grammar. The
Vega-Lite spec is compiled into a more verbose Vega specification (JSON) which
completely describes the visualization in terms of it's visual elements. The
Vega spec is then rendered in the browser using JavaScript libraries such as D3
as it's visualization kernel. 

<img
    src="/assets/images/vega-stack/04-stack-labels.svg"
    width="800" />

If you understand this much I think using Altair and Vega-Lite will be much more fruitful. 

One interesting aspect of this software stack is the modularity. Altair is a
Python API but there are many other APIs for your preferred language. At the
other end of the stack is the JavaScript library D3, but there are other very
powerful visualization libraries which are optimized for different contexts. 
<img
    src="/assets/images/vega-stack/07-stack-split-dotted.svg"
    width="800" />
Having an expressive declarative visualization grammar opens up many opportunities. Currently
Vega/Vega-Lite targets the web via D3 and JavaScript allowing for a rich set of interactive visualizations 
to be made.  Once you have a Vega spec, other powerful tools 
could be used to convert and translate the visualization to different domains. 
For instance, I think it would be interesting to develop a program which reads Vega specs and 
creates TikZ code to be rendered in LaTeX documents. There are many possibilities and it is still early days.

Returning to the questions mentioned in the beginning, maybe now I can provide some more constructive answers:
- "Can I do [insert domain specific task] with Altair?"
    - Maybe. If you have [tidy data][tidy-link] and want to make a 2D
      statistical visualization, then probably!
- "Does Altair only work in Jupyter Notebooks?"
    - No. At it's core Altair is a Python library that outputs Vega-Lite specs.
      Jupyter Notebooks can render Vega-Lite specs, but so can many other
      tools.
- "How do I increase the font size?"
    - `chart.configure_axis(labelFontSize=20, titleFontSize=20)`

## Closing Remarks

I hope this post helps to orient new users as well as explain the many tools on which Altair depends.
Over the past few years working with Altair it has been really exciting to watch the 
community grow.  [Deep in a github issue][wilkinson-quote-link] on the Vega-Lite repository I found 
a wonderful quote

> “... having gone through a lot of these GG-inspired systems, 
> I believe [Vega/Vega-Lite] is the most authentic implementation. 
> I'm using it every day.” -- Leland Wilkinson

Whoa! Remember Wilkinson from earlier?!  It is really amazing to listen in on (and contribute to) the developments
of the Vega/Vega-Lite projects in real time. The comments and concerns voiced, have provided me with a 
much deeper understanding the process of visualization. 

Time next time, 

-Eitan


[wilkinson-quote-link]: https://github.com/vega/vega-lite/issues/408#issuecomment-500218456
[stack-blog-post]: https://blog.ericmarty.com/the-d3-/-vega-stack
[altair-website]: https://altair-viz.github.io/
[jupyter-website]: https://jupyter.org/
[gg-link]: https://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448
[altair-quote-link]: https://altair-viz.github.io/user_guide/internals.html
[vega-lite-website]: https://vega.github.io/vega-lite/
[vega-quote-link]: https://vega.github.io/vega/about/vega-and-d3/
[json-website]: https://www.json.org/json-en.html
[ggplot-website]: https://ggplot2.tidyverse.org/index.html
[d3-trouble]: https://medium.com/dailyjs/the-trouble-with-d3-4a84f7de011f
[tidy-link]: https://vita.had.co.nz/papers/tidy-data.pdf
[altair-viewer-link]: https://github.com/altair-viz/altair_viewer
