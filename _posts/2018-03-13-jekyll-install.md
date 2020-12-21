---
layout: post
title: My Jekyll Installation Experience
date: 2018-03-13 11:46:59 
categories: jekyll update installation
---

All in all to get a simple blog up and running with [Jekyll](https://jekyllrb.com/) has been pretty
straight forward. Customization and using themes has been a little confusing. 

#### Pros :+1:

- Setting up [GitHub Pages](https://pages.github.com/) was really easy. Just create a repository
  with _username_.github.io and it works. 
- The default [Minima](https://github.com/jekyll/minima) theme is pretty good for a simple look.
- [Writing posts](https://jekyllrb.com/docs/posts/) is very easy and can be done with markdown. 

#### Cons :-1:

- Many tutorials involve a _[fork first workflow](https://github.com/barryclark/jekyll-now)_ which I don't like. I am comfortable with the
  command line and prefer developing locally before publishing. Maybe a _clone first workflow_?

- Changing themes has been kind of a mess because of the different layout requirements. I tried a
  few themes but ran into errors when compiling. Incremental changes were hard to implement because
  themes required specific directory structure.

- Initially I found the [gem-based themes](https://jekyllrb.com/docs/themes/) confusing as many
  online tutorials had a different directory structure. To make local customizations I would need to
  run `bundle show minima` to see where the Minima configuration files are. Then make a copy in my
  local site repository and make the changes. The lesson I learned was read the docs!

For now I plan to stay with Minima and focus on content. I want to add some more incremental changes
such as comments on posts, also maybe a contact, resume and archive page. 

#### Useful Links :link:

I found the most of my questions were addressed in the official documentation. Often re-reading
helped. 

- [Official Jekyll Documentation](https://jekyllrb.com/docs/home/) 

I  enjoyed this write up about setting up a Jekyll blog. At the time of writing this post Brian's
website is also using the Minima theme which was a great reference point.

- [Simple Jekyll tutorial with Github Pages](https://web.archive.org/web/20200811074905/https://briancaffey.github.io/2016/03/17/jekyll-tutorial.html) by Brian Caffey


I enjoyed this set of videos going into the specifics about using Jekyll.

- [Jekyll: Static Site Generator Tutorial](https://www.youtube.com/playlist?list=PLLAZ4kZ9dFpOPV5C5Ay0pHaa0RJFhcmcB) by Giraffe Academy


