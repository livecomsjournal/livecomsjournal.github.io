---
layout: single
sidebar:
  nav: authors_policies.md
title: General Author Instructions
excerpt: This article describes how LiveCoMS article preparation and submission work, as well as giving details of the review process, revisions, authorship, and other aspects.
permalink: /authors/policies/
---

This article describes how [LiveCoMS](http://www.livecomsjournal.org) article preparation and submission work, as well as giving details of the review process, revisions, authorship, and other aspects.

## Introduction

Submitting an article to LiveCoMS is substantially different from submitting an article to most journals. 
In this article, we lay out the process by which authors create an article, submit it to LiveCoMS, and update it over time to create a living document.  

## General Article Guidelines

There are no explicit length limits on any manuscript. 
Articles do not need to contain original research, but may contain it.

## Types of Articles

Click each type of article for more information for submitting an article of that type.

- [Best Practices Guides](/best_practices/)

- [Perpetual Reviews](/perpetual_reviews/)

- [Comparisons of Molecular Simulation Packages](/compare_simulations/)

- [Tutorials](/tutorials/)

- ["Lessons Learned"](/lessons_learned/)

# Before Submission

## Presubmission Letter

Authors should first send a presubmission letter to the [lead editor in the relevant area](http://www.livecomsjournal.org/editorial-board).  The letter should be no more than one page, and should:
* Outline the scope of the proposed contribution.
* Explain how the proposed manuscript is different from existing published work. 
* Note whether the manuscript is adapted from a previous article (and identify the article if so).
* Explain the expertise that the proposed authors have on the subject.
* Describe the license that the authors will use that will enable the article to be released freely to the public.

Potential authors submitting a presubmission letter will typically receive an answer within two weeks with either encouragement for a full submission, suggestion to work with previous authors on existing articles, or discouragement.
Articles should be received within six months of a notification of encouragement.

## Preparation of Your Article For Submission

The authors should prepare the document using
[LaTeX](https://www.latex-project.org/) in a public repository owned
by one of the authors (or their organization/group) on [GitHub](http://wwww.github.com). 
LiveCoMS [provides template LaTeX files to start from](https://github.com/livecomsjournal/article_templates), and instructions for exactly how to structure the documents.
We require that articles submitted to LiveCoMS use the provided templates so that the journal has a consistent visual presentation.
Additionally, articles should include clear links to, and mention of, the relevant GitHub repository and encourage community participation/feedback via GitHub. 

For an example of an article hosted on GitHub in this style (though not a LiveCoMS article), see [the following perpetual review](https://github.com/MobleyLab/benchmarksets). 


### Writing style and editing

Articles for LiveCoMS should aim to be as clear as possible, as they are intended to aid the community, not just an expert in the field.
In general we recommend authors follow the [ACS Style Guide](http://pubs.acs.org/isbn/9780841239999) and especially the sections on:
- [Writing and word usage](http://pubs.acs.org/doi/pdf/10.1021/bk-2006-STYG.ch004), noting the advice to use direct, declarative sentences, often in active voice
- [Editorial style](http://pubs.acs.org/doi/pdf/10.1021/bk-2006-STYG.ch010)
- [Grammar, spelling, and punctuation](http://pubs.acs.org/doi/pdf/10.1021/bk-2006-STYG.ch009)

We also find Plaxco's [The Art of Writing Science](http://dx.doi.org/10.1002/pro.514) to be a particularly helpful concise summary of our desired style.

It is particularly important to note that **LiveCoMS does not edit articles in detail, so it is important to arrange for your own editing**.
You may receive some comments from your editor and/or the peer reviewers that point out typos or other issues, but you should not **rely** on this for your editing process. 
In order to keep costs to authors at a minimum, we do not employ copy editors, so be sure to arrange for your own editing.

Articles can have any length; however, you should be as concise as possible.

### Article layout

You are responsible for preparing your article PDF and materials in the way you want them to appear in LiveCoMS [using our templates](http://www.github.com/livecoms/author_templates), so it is important to take some care as to how your submitted materials look.
LiveCoMS will not be separately typesetting your article for you, so be careful that your materials are laid out well.
Be sure to pay particular attention to:
- Place your figures and tables appropriately in the document, rather than collecting them at the end
- Number figures and tables in the order in which they are referenced in the text
- Use consistent (and legible) font sizes in figures and tables; our LaTeX template uses OpenSans; we recommend its use if possible in figures as well.


### Preprints

One written, the authors post the resulting PDF document to a preprint server of their choice, which can be any one of:
* [ArXiv](https://arxiv.org)
* [BioRxiv](http://www.bioarxiv.org)
* [ChemRxiv](https://chemrxiv.org/)
* [Faculty of 1000 Research](https://f1000research.com)
* Any of the [Open Science Framework preprint servers](https://osf.io/preprints/) (engrXiv, etc.)

Posting to the preprint server can be done at any time prior to submission. 


# Submission and the Review Process


## Article submission 

After posting to the preprint server, the author uploads the final
article PDF (created using the [LiveCoMS
templates](https://github.com/livecomsjournal/article_templates), discussed above) and a link to the GitHub site for the article.

The authors must also submit a cover letter with suggestions for 4--5
reviewers, and note any deviations from the presubmission letter.


## The review process

The editors will choose reviewers, which may include the editors themselves.  
Reviews will generally be anonymous, though reviewers will be allowed to become known if they desire, and can participate directly in revisions through the GitHub website, whether or not they remain anonymous.
For example, a reviewer could choose to submit a very brief review addressing only suitability, but provide extensive feedback to the authors on the GitHub issue tracker, allowing discussion of how the article should be revised to be done openly.
This open revision approach may be particularly suitable for articles which will become community resources. 

## Review criteria 
A key purpose of the articles is that they should be useful to a range of researchers, but
especially beginning researchers. 
Thus, all submitted manuscripts will be reviewed by a member of the student review board, which consists of graduate students and postdocs invited by the editorial board.

Authors are also encouraged to have other researchers review their
content, with comments and responses handled via the article's GitHub issue
tracker. 
A history of revisions in response to community concerns will impact the review process favorably.

Reviewers will also be asked to assess whether articles are well edited and clearly written.
Authors whose article uses inconsistent style or poor grammar, or is poorly edited, may be asked to revise and address these issues. 

Reviews will also consider the additional factors according to manuscript category: [please see the individual category links](#types-of-articles) for more information on these review criteria.


## The Revision Process

If manuscript revision is requested, authors will be asked to re-submit within 30 days for minor revisions and 60 days for major revisions. 
After this time, a revised manuscript may be handled as a new submission.

# Updating LiveCoMS Articles

A unique aspect of LiveCoMS is article versions, where new, updated versions of articles can be re-reviewed and treated as new publications. 

Once peer reviewed, articles receive new DOI’s and are published on the LiveCoMS site as new versions. 
This allows authors to receive credit for ongoing work they do on their articles.

Authors are encouraged to make updates to articles in their GitHub repositories as frequently as warranted. However, release of new peer-reviewed versions via LiveCoMS is warranted only when changes become particularly extensive or important. Thus, versioning should typically be done no more frequently than every 12 months.  

The review process for an update to a LiveCoMS article is similar to the review process for the initial version.  Additional review criteria will include whether or not issues the community raised on the article's issue tracker were responded to, and whether the revision includes sufficient new material.

Certain categories of article may need revision at different frequencies. For information on the review frequencies, see [author information for each of the types of articles](#types-of-articles).

## Engaging the Community in Improving Articles

We require GitHub use for papers to provide an easy mechanism for community feedback on the paper, allowing questions, comments, or additions.
Community members can easily [file issues](https://help.github.com/articles/about-issues/) on these topics, and then these can be incorporated into new versions of the article.
This can help LiveCoMS articles truly become living documents.
Please note: The issue tracker for these documents is not just for *problems* with the articles, but also for general discussion, feedback, questions, and so on -- really, for any type of discussion about the article.

We are sympathetic to the fact that some commenters may wish to provide feedback to authors outside of GitHub.
This can be done via conventional means, such as contacting the relevant authors directly.


## Paper Writing as Code Development

This model of updatable papers, curated with community input, allows paper-writing to become much more like code development -- a process of iterative improvement. This approach can be called [paper writing as code development](paper_code.md), and allows authors to benefit from well-established practices and tools which help code developers.

# Authorship and Changes to Authorship

Authorship for "living" documents, LiveCoMS' focus, can become complicated as the document involves and more people contribute.
Our key principle is that participants should get credit for their contributions, which can come in a variety of forms such as actually writing the work, providing feedback and filing issues, etc.
However, different types of credit may be warranted. 
In general, changes which constitute writing a significant part of the article merit authorship, but not those which only modify small portions.

In order to acknowledge more minor contributors, people who offer comments/citations that are used in the paper should be listed listed on the relevant GitHub repository README Markdown file, and should be listed in the acknowledgment section of the paper. 
However, if the current authors feel that the contributions rise to the level of authorship, they can add new authors when the next major version is submitted.

Exactly what constitutes a "significant" contribution is by necessity subjective, and authors should endeavor to be generous. In the process of reviewing revisions, the editors may examine the history of the GitHub repository to ensure appropriate credit is being given. 
If contributors feel that they should be given authorship based on the number of accepted commits, the editors will help resolve any disputes. 
If contributors feel that their commits are not being accepted by the authors they should first strive to convince the authors and the community through well documented, convincing arguments. 
If authors do not engage with substantial issues that have been raised, they may be asked to address these issues in the review process. 
If authors do not substantively engage in the discussions on issues that are raised, this may prevent new updates of the review from being accepted.

# Other Policies for Submitted Articles

## Funding Compliance
Authors are required to report funding sources and grant/award numbers relevant to the manuscript for ALL authors.

Authors should note whether any funding could be perceived as a conflict of interest, e.g., an article describing software in which an author has a financial interest.

## Licensing 

LiveCoMS does not request or allow any copyright transfer.

However, in order to submit to LiveCoMS, authors must provide, at
minimum, a license for LiveCoMS to publish the article and distribute
it free of charge. We recommend that the authors release the article
under an open source license such as [Creative Commons
  Attribution](https://creativecommons.org/licenses/by/4.0/}{Creative Commons
  Attribution) (also known as CC-BY) releasing the document for anyone to copy and
redistribute the material in any medium or format, and remix,
transform, and build upon the material for any purpose, even
commercially.  Making it available to all of course makes it possible
for LiveCoMS to publish it, and for the community to edit and
contribute.  We highly recommend the CC-BY license in order to ensure
your work can reach and help the broadest audience possible, and
suggest that when considering the appropriate license you [read this analysis](http://openaccess.ox.ac.uk/2013/06/13/cc-by-what-does-it-mean-for-scholarly-articles-3/).

Other more restrictive licenses may be permissible as long as LiveCoMS
has the permission to publish and excerpt from the document; 
another license might be needed if someone other than the authors has some rights to
the material (for example, if it was previously published in some
other journal). Generally, we only allow a more restrictive license in
these cases, but are happy to discuss. Please ask the managing editors
if you require some other licensing regime.

For employees of the U.S. Government, their work products are under
public domain, and thus CC-BY is not appropriate. We recommend the
license language: "As a work of the United States Government, this
package is in the public domain within the United
States. Additionally, \[Agency Name\] waives copyright and related
rights in the work worldwide through the CC0 1.0 Universal Public
Domain Dedication (which can be found at
https://creativecommons.org/publicdomain/zero/1.0/)."
[See the analysis of this language here](https://theunitedstates.io/licensing/).

## Prior Publication

Documents should not have been submitted in the current form to another journal, or be simultaneously under consideration for publication another journal. 
Preprints do not count as prior publication. 
Documents that are major revisions of previously published articles are welcomed. 
However, authors should ensure that material they develop for the journal does not have rights reserved by other journals from such previous publication that impede release under open licenses. 
Some journals, for example, *Annual Reviews* lets the authors retain the right to create derivative works, which could perhaps be exercised in preparing a review to be published in LiveCoMS. 

If an article is an adaptation of a previously published article, it must be noted in the cover letter, and major changes noted. 
Evaluating whether such changes constitute a significant revision will be part of the review process.

## Author Order
Authors should, to the extent possible, determine the author order
among themselves.  However, we acknowledge that institutions
evaluating for merit, promotion, tenure or other cases may not read
this level of detail, so traditional notions of author order (first
author, corresponding author, etc.) may still be relevant and the
authors will need to coordinate who should occupy these positions.

Each work must have a section describing the actual contributions of
authors (and of those acknowledged) to provide clarity, and journal
templates include such a section.  Please note, since this is an
electronic-only journal, there is no length limit when you describe
the authors' contributions, so we recommend describing what they
actually did rather than simply categorizing them in a small number of
predefined roles as might be done in more conventional journals.
<!-- MRS: still need to add that section of the templates somewhat -->  

## Abandoned Documents

By the submission of their paper, document, or materials, all the
authors consent that if they no longer are willing or able to maintain
their work, LiveCoMS may assign another individual or individuals to
do so, with appropriate modifications to the authors list. Authors
would be given written notice (by e-mail and formal letter) if this
were to happen and would have a period of six months to respond and/or
designate a successor before LiveCoMS would do so for them. Typically,
authors are *implicitly* giving a right to do this via licensing under
[Creative Commons - Attribution](https://creativecommons.org/licenses/by/4.0/) or
similar licenses which give others the right to create derivative
works (potentially allowing others to "resurrect" a document which
has been abandoned); however, we expect all authors to *explicitly*
consent to this policy to avoid any confusion. Ordinarily, we expect
this policy will be relevant only in unusual or extreme cases where an
author or authors dies or leaves the field; in most other cases
authors will presumably be available to designate their own successors
or succession plan if a work is valuable to the field and will
continue to need maintenance and the original author(s) are no longer
willing or able to do so. However, we want to plan for the possibility
of unusual events, hence our need for this policy.

Thus, for these reasons, authors submitting to LiveCoMS are agreeing
that others may take over authorship of their article (with
appropriate acknowledgment/recognition of the original authors) if
they have abandoned their article as described above, and that
LiveCoMS may accept revised versions of papers which have amended
authorship in such circumstances.
