---
layout: default
---
This article describes how [LiveCoMS](http://www.livecomsjournal.org) article preparation and submission work, as well as giving details of the review process, revisions, authorship, and other aspects.

# Table of Contents

- [Submission Process](#the-process-of-submitting-an-article-to-livecoms)
  - [Article types](#types-of-articles)
  - [General guidelines](#general-article-guidelines)
- [Before Submission](#before-submission)
  - [Presubmission letter](#presubmission-letter)
  - [Article preparation](#preparation-of-your-article-for-submission)
- [Submission and the Review Process](#submission-and-the-review-process)
  - [Article submission](#article-submission)
  - [The review process](#the-review-process)
  - [Review criteria](#review-criteria)
  - [The revision process](#the-revision-process)
- [Updating LiveCoMS Articles](#updating-livecoms-articles)
  - [Getting community help with updates](#engaging-the-community-in-improving-articles)
  - [Paper writing as code development](#paper-writing-as-code-development)
- [Authorship and Changes to Authorship](#authorship-and-changes-to-authorship)
- [Other Policies for Submitted Articles](#other-policies-for-submitted-articles)
  - [Funding Compliance](#funding-compliance)
  - [Licensing](#licensing)
  - [Prior publication](#policy-on-prior-publication)

# The Process of Submitting an Article to LiveCoMS

## Introduction

Submitting an article to LiveCoMS is substantially different from submitting an article to most journals. 
In this article, we lay out the process by which authors create an article, submit it to LiveCoMS, and update it over time to create a living document.  

## General Article Guidelines

There are no explicit length limits on any manuscript. 
Articles do not need to contain original research, but may contain it.

## Types of Articles

Click each type of article for more information for submitting an article of that type.

- [Best Practices Guides](best_practices.md)

- [Perpetual Reviews](perpetual_reviews.md)

- [Comparisons of Molecular Simulation Packages](compare_simulations.md)

- [Tutorials](tutorials.md)

- ["Lessons Learned"](lessons_learned.md)

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
LiveCoMS [provides template LaTeX files to start from](http://www.github.com/livecoms/author_templates), and instructions for exactly how to structure the documents. 
We require that articles submitted to LiveCoMS use the provided templates so that the journal has a consistent visual presentation.
Additionally, articles should include clear links to, and mention of, the relevant GitHub repository and encourage community participation/feedback via GitHub. 

For an example of an article hosted on GitHub in this style (though not a LiveCoMS article), see [the following perpetual review](https://github.com/MobleyLab/benchmarksets). 


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
templates](http://www.github.com/livecoms/author_templates), discussed above) and a link to the GitHub site for the article.

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

LiveCoMS does not require any copyright transfer to the journal.  
Instead, LiveCoMS requires articles use a license which allows LiveCoMS to distribute the articles freely consistent with Open Access requirements. 
We recommend that all submissions to LiveCoMS be released by the author under a Creative Commons By Attribution license version 4.0; however, other licenses may be acceptable with justification.

## Policy on Prior Publication

Documents should not have been submitted in the current form to another journal, or be simultaneously under consideration for publication another journal. 
Preprints do not count as prior publication. 
Documents that are major revisions of previously published articles are welcomed. 
However, authors should ensure that material they develop for the journal does not have rights reserved by other journals from such previous publication that impede release under open licenses. 
Some journals, for example, *Annual Reviews* lets the authors retain the right to create derivative works, which could perhaps be exercised in preparing a review to be published in LiveCoMS. 

If an article is an adaptation of a previously published article, it must be noted in the cover letter, and major changes noted. 
Evaluating whether such changes constitute a significant revision will be part of the review process.


