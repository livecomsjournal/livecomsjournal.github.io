---
layout: single
sidebar:
  nav: authors_policies.md
title: General Author Instructions
excerpt: Overview of article preparation, submission, and review.
permalink: /authors/policies/
---

This article describes how [LiveCoMS](http://www.livecomsjournal.org) article preparation and submission work, and provides details covering the review process, revisions, authorship, and other aspects.

## Introduction

Submitting an article to LiveCoMS is substantially different from submitting an article to most journals.
In this article, we lay out the process by which authors create an article, submit it to LiveCoMS, and update it over time to create a living document.  

## General Article Guidelines

There are no explicit length limits on any manuscript.
Articles do not need to contain original research, but may contain it.
Currently, articles in LiveCoMS must be submitted as one of the article types noted below.

## Types of Articles

Click each type of article for more information for submitting an article of that type.

- [Best Practices Guides](/authors/best_practices/) lay out recommendations for best practices or key issues to consider in a particular area of computational molecular science.

- [Perpetual Reviews](/authors/perpetual_reviews/) provide a review of a particular topical area, from the author's/authors' perspective, but are maintained to reflect the latest developments.

- [Software Analyses](/authors/software_analyses/) attempt to perform the same calculation with a range of different simulation programs.

- [Tutorials and Training Articles](/authors/tutorials/) provide walkthroughs and are accompanied by supporting files for use as training material or instructional materials on important general principles or calculations in molecular science.

- [Lessons Learned](/authors/lessons_learned/) highlight failed studies on a particular topic that are instructive/provide important lessons, helping new authors avoid mistakes encountered previously by others.

# Before Submission

## Presubmission Letter

Before submitting article, authors **must** send a presubmission inquiry letter to the [Lead Editor for the relevant area](http://www.livecomsjournal.org/editorial-board) (and see these emails below as wee). We **strongly** encourage writers of prospective articles to send this inquiry letter in the early stages of drafting an article.
The presubmission inquiry letter should be no more than **one page** in length, and should include:
* An outline the scope of the proposed contribution
* An explanation how the proposed manuscript differs from existing published work
* Whether the manuscript is adapted from a previous article (and identify the article if so), and if permissions to use this previous document have been obtained if necessary. As long as necessary permissions have been obtained, and the article will contain substantive new work, then previous publication of parts of the work does not prejudice acceptance.
* A summary of the expertise that the proposed authors have on the subject
* A description of the plan for how the article will be updated, including the plan for transfering authorship if the original authors are unable to update it.
* The proposed license enabling the article to be released freely to the public (see [Licensing](https://livecomsjournal.github.io/authors/policies/index.html#licensing) below for recommendations)
* Some article types have **additional requirements** for the presubmission letter; see the section instructions above for these additional requirements.

Potential authors submitting a presubmission letter will typically receive an answer within two weeks with either encouragement for a full submission, a suggestion to engage with previous authors to extend an existing articles, or suggestions for more suitable publication routes.
Articles should be submitted within six months of a notification of encouragement.

Section Leads can be contacted at:
- Tutorials: [tutorials@livecomsjournal.org](mailto:tutorials@livecomsjournal.org)
- Best practices: [bestpractices@livecomsjournal.org](mailto:bestpractices@livecomsjournal.org)
- Lessons learned: [lessonslearned@livecomsjournal.org](mailto:lessonslearned@livecomsjournal.org)
- Perpetual reviews: [reviews@livecomsjournal.org](mailto:reviews@livecomsjournal.org)
- Softwarer Analyses: [software@livecomsjournal.org](mailto:software@livecomsjournal.org)


## Preparation of Your Article For Submission

The authors should prepare the document using
[LaTeX](https://www.latex-project.org/) in a public repository owned
by one of the authors (or their organization/group) on [GitHub](https://www.github.com).
LiveCoMS [provides template LaTeX files to start from](https://github.com/livecomsjournal/article_templates) for the different article types; category-specific guidelines are [linked above](https://livecomsjournal.github.io/authors/policies/#types-of-articles) and additional guidance on document structure is given in the structure of the [LaTeX templates](https://github.com/livecomsjournal/article_templates) themselves and comments therein.
We require that articles submitted to LiveCoMS use the provided templates so that the journal has a consistent visual presentation.
Additionally, articles should include clear links to, and mention of, the relevant GitHub repository and encourage community participation/feedback via GitHub, as indicated in the provided templates.

### Copyright license

In order to publish the article, LiveCoMS requires that authors sign [an additional contributor license](/assets/pdf/LiveCoMS_contributor_license.pdf) to clarify LiveCoMS rights to publish the article, regardless of the license the author uses in their own release of the article on GitHub.  This document also to confirms that the authors grant the publisher the right to distribute their article and that the authors are legally entitled to do so for all the material in the article.  

This agreement is a license, *not a copyright transfer*; authors retain the copyright for their works, and therefore authors are not restricted in their own use or distribution of their work in any way by this document.

### Writing style and editing

Articles for LiveCoMS should aim to be as clear as possible, as they are intended to aid new members of the community, not just experts in the field.

It is particularly important to note that **LiveCoMS does not edit articles in detail, so it is important to arrange for your own editing**.
In order to keep costs to authors at a minimum, we do not employ copy editors, so be sure to arrange for your own editing.
You may receive some comments from your editor and/or the peer reviewers that point out typos or other issues, but you **should not rely** on this for your editing process.

In general we recommend authors follow the [ACS Style Guide](http://pubs.acs.org/isbn/9780841239999) and especially the sections on:
- [Writing and word usage](http://pubs.acs.org/doi/pdf/10.1021/bk-2006-STYG.ch004), noting the advice to use direct, declarative sentences, often in active voice
- [Editorial style](http://pubs.acs.org/doi/pdf/10.1021/bk-2006-STYG.ch010)
- [Grammar, spelling, and punctuation](http://pubs.acs.org/doi/pdf/10.1021/bk-2006-STYG.ch009)
- References: in the BibTeX file, enter journals with their standard abbreviations (per [CASSI](http://cassi.cas.org/search.jsp)) and titles in Title Case. As with the main text, check that any special characters are rendered correctly in the final PDF.

We also find Plaxco's [The Art of Writing Science](http://dx.doi.org/10.1002/pro.514) to be a particularly helpful concise summary of our desired style.

Articles can have any length; however, you should be as concise as possible.

### Article layout

You are responsible for preparing your article PDF and materials in the way you want them to appear in LiveCoMS [using our templates](http://www.github.com/livecomsjournal/article_templates), so it is important to take some care as to how your submitted materials look.
LiveCoMS will not be separately typesetting your article for you, so be careful that your materials are laid out well.
Be sure to pay particular attention to:
- Place your figures and tables appropriately in the document (following the paragraph that first references them), rather than collecting them at the end. Do not not move the figures and tables in the LaTeX document to change where they appear. Instead, use the [LaTeX placement options](https://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions) to adjust positioning.
- Use consistent (and legible) font sizes in figures and tables; our LaTeX template uses OpenSans; we recommend its use if possible in figures as well. See additional discussion on [figures](#figures) below.
- Check that all special characters appear correctly in the rendered PDF.

### References

References should be prepared in BibTeX format, as discussed further in our [article templates](https://github.com/livecomsjournal/article_templates/blob/master/bibliography_guidelines.md) repository, and cited in LaTeX as normal.
Our templates provide a bibliography style file (`.bst`) and use the `natbib` package; they will standardize format of your references to a reasonable extent.
However, it is still important that your references use Title Case for article titles, and that they use journal title abbreviations.
You are responsible for checking that any special characters appear properly, and otherwise ensuring that your final reference list is correct and well-formatted, including sufficient detail.
We suggest that authors use tools such as [Fix BibTeX](https://github.com/jaimergp/fixbibtex) to check the integrity of entries in their bibliography.
We point out that such tools may not correct BibTeX entries with perfect accuracy; authors are still ultimately reponsible for ensuring the correctness of their article's bibliography.
Pay particular attention to formatting of non-journal articles as it is easy to end up omitting key citation information for content like software, poster presentations, preprints or other materials.

Authors may benefit from automated tools to curate/check BibTeX files against automatic online sources, such as [betterbib](https://github.com/nschloe/betterbib). Such checks typically still require manual curation, but they can be very helpful in identifying potential errors or mistakes. 

### Figures

Our largest concern in the construction and preparation of figures is their quality in the final PDF, so we do not *require* any specific image format for figures.
Rather, figures should:
- Appear polished in the final PDF of the article, even if zoomed in a great deal
- Be of sufficiently high quality that they look good printed, in both color and grayscale (which has implications for color choices)
- Be stylistically consistent with the rest of the paper (ideally using OpenSans as the font, and having similar font sizes/styles to the rest of the paper)
- Use words, symbols, and units for axis labels, *e.g.* not just a plot of sigma vs. r but words should explain what sigma and r are, and what units they use
- Use self-contained captions so that the point of the figure can be understood without referring to details in the text
- Not be so large that the final PDF is an inconveniently large file (typically larger than 10 MB due to e-mail attachment sizes, though exceptions can be made)

Our specific graphical goals can usually be best met by making as many figures as possible in a vector graphics format such as `.svg`, `.pdf`, `.eps`, or similar, as these can be zoomed to an arbitrary level and maintain high quality, but also maintain modest sizes.
If you are using bitmapped graphics, we highly discourage the use of `.jpg` or other lossy formats and instead recommend `.tif`, `.png` or similar.
If you do use such graphics formats, pay particular attention to them to ensure that resolution is sufficient so that they look excellent even if zoomed or printed at high quality, as you can expect more issues with these formats than for vector graphics.
As a general rule, ensure bitmapped graphics are 300 DPI or better when produced at the size at which they will appear in your final PDF.

To ensure font sizes are as intended, make sure to create your figure at the planned size and specify the desired font size, rather than creating a large figure with the desired font size and shrinking it (resulting in text smaller than intended).

We recommend making use of both single column and two column figures as appropriate depending on the width of the content you wish to include.

### Tables

As with figures, our main concern with tables is their quality in your final PDF.
Overall table formatting is up to you, but tables should have clear labels, provide clear captions, and have columns which are clearly labeled with symbols, units, and all other relevant quantities necessary to understand what is presented.
As with figures, captions should be relatively self-contained so that the main point of tables can be understood without referring to full details in the text.

### Error analysis

All original computational/numerical work presented in LiveCoMS is expected to include appropriate error analysis/error bars, and it should be clearly indicated how any error analysis was done and what quantities are presented (standard error in the mean, confidence interval (at what percentile), etc.)
All data presented should have error bars if available, though if drawn from literature data where no uncertainties were presented we understand if they cannot be given (though this should be noted).
Preliminary guidance can be obtained from the yet-to-be-peer-reviewed [Best Practices manuscript](https://github.com/dmzuckerman/Sampling-Uncertainty/) on quantifying uncertainty.

### Preprints

Ultimately, assuming your article passes peer review, LiveCoMS will host a published version of your article, and you will have what essentially constitutes a preprint available on GitHub as well.
However, you are also free to post your article to standard preprint servers, such as:

* [ArXiv](https://arxiv.org)
* [BioRxiv](https://www.biorxiv.org)
* [ChemRxiv](https://chemrxiv.org/)
* [Faculty of 1000 Research](https://f1000research.com)
* Any of the [Open Science Framework preprint servers](https://osf.io/preprints/) (engrXiv, etc.)

Posting to a preprint server can be done at any time prior to submission.

# Submission and the Review Process

## Article submission

### Abstract
There is no specific word limit for the abstract, but it should be short and descriptive. During submission, check that the abstract as entered into the submission software appears as you intend, especially watching out for copied and pasted carriage returns that break lines.

### Main Manuscript

The main article manuscript should be of type .pdf, created using the [LiveCoMS templates](https://github.com/livecomsjournal/article_templates), discussed above) and a link to the GitHub site for the article.
[General Scholastica submission instructions are available through on the Scholastica help page](http://help.scholasticahq.com/customer/portal/articles/1218626), our journal management system. 

There are a [few additional LiveCoMS submission instructions](http://www.livecomsjournal.org/for-authors).  

Please make sure the metadata is correct. This includes affiliations, including department if applicable, for all authors, ORCID ID's for all authors. 
This can be done by looking at the "preview" view of the abstract before submissiomn - it is easy to include extraneous carriage returns that mess up the formatting, which the editors can't change it for you, and which reviewers will see. 

The authors must also submit with the final article PDF:

  * As a single PDF file, a copy of their presubmission letter, appended with the response recieved from the Section Lead Editor approving the presubmission and specifying any changes or modifications to the scope the editors requested. The authors should also include a description of deviations, if any, from what was laid out in the presubmission letter, with a rationale for why the changes were made. This should be uploaded as a "Supporting File", with the descriptor "Presubmission Letter".
  * A key graphic or representative cover image. This should be something which graphically portrays in general terms the subject area you are focusing on or the aims of the paper. This is not a table of contents abstract, as it will be automatically cropped and resized when being shared in different formats.  It should be at least 1200 pixels across, though in most cases 2500 pixels across is better, and should be wider than it is high. It must be in `.jpg` format. This image is important to choose carefully, as it is the image that will appear on the article's front page and whenever the paper is shared on social media. We suggest something evocative of the research, but again, containing less scientific detail than, say, the table of contents abstract for an ACS journal.
  * Any Supporting Files, such as Jupyer notebooks, videos, etc. that are intended for distribution with the final paper should also be uploaded at this time. There is no explicit limit to the number of files that can be added, though if there are many similar data files, they should be uploaded as a `.tgz`ed or `.zip`ed directory and include a README file.  Data should be uploaded in nonproprietary formats (.pdf instead of .ppt/.pptx/.key, .csv instead of .xls or .xlsx). Supporting files should be described in the article itself, as there are no page limits. If there are simulation input files or data files included as part of your article, they should be placed into a single compressed .zip directory, with a README.txt or .md file fully explaining how to use the files, as “Supporting Files”. 
  * For the keywords section, please put the type of manuscript being submitted (one of either “Best Practices”, “Living Reviews”, " Comparisons of Molecular Simulation Packages", “Lessons Learned”, and “Tutorials”) and up to four other short terms or keywords.

As part of the submission form, authors will suggest 4-5 reviewers.

## The review process

The review process generally begins with an editor reviewing your document to check that it is ready for review (e.g., that it uses suitable English, is laid out appropriately and legibly, etc.) and subsequently selecting reviewers.
If there are major issues at this stage, your article may be returned for revision prior to review.
Reviews will generally be anonymous, though reviewers will be allowed to make themselves known if they desire.
Reviewers can also participate directly in revisions through the GitHub website, whether or not they remain anonymous.
For example, a reviewer could choose to submit a very brief review addressing only suitability questions, and then provide extensive feedback to the authors on the GitHub issue tracker, allowing discussion of how the article should be revised to be done openly.
This open revision approach may be particularly suitable for articles which will become community resources.

A key criteria for articles in LiveCOMS is that they should be useful to a range of researchers, but especially beginning researchers.
Thus, all submitted manuscripts will be reviewed by a graduate students or postdoc invited by the editorial board.

Authors are also encouraged to have other researchers review their content, with comments and responses handled via the article's GitHub issue tracker.
A history of revisions in response to community concerns, questions and suggestions will impact the review process favorably.

For more information about the role of reviewers and the criteria they are asked to use, please see the [Reviewer Information](https://livecomsjournal.github.io/policies/reviewer_information/).


## The revision process

If manuscript revision is requested, authors will typically be asked to re-submit within 4 weeks for minor revisions and 8 weeks for major revisions.
After this time, a revised manuscript may be handled as a new submission.

Your revised manuscript should be accompanied by detailed responses to the reviewers' comments and a summary of changes made to the manuscript. You should also include as an additional file a version that highlights changes in the manuscript.  [LatexDiff](https://ctan.org/pkg/latexdiff?lang=en), with documentation [here](https://mirror.hmc.edu/ctan/support/latexdiff/doc/latexdiff-man.pdf)  is one tool that can be used generate this version. If there are formatting issues, we suggest downloading the more recent template files, which may fix some formatting concerns.  We suggest documenting general categories of changes requested by the reviewers as separate GitHub issues, but that is not required for resubmission.

## Upon acceptance

After acceptance of your article, the first task is to prepare an appropriate "ASAP" version of the article which will be posted to the journal's website prior to publication of the next issue. Several steps, outlined below, are required. Note that ASAP version will essentially be final, as only minor corrections as detailed below will be permitted prior to publication as part of an issue.
- Verify that the metadata is complete in the submission. This includes institutions with departments (if applicable) for all authors, ORCID ID for all authors, and a correctly formatted abstract. Enable the LiveCoMS footer by including the `ASAPversion` class option in the document preamble, and fill in the `\datereceived` and `\dateaccepted` fields.
- Send a signed copy of the [contributor license release form](https://livecomsjournal.github.io/assets/pdf/LiveCoMS_contributor_license.pdf) to `managing@livecomsjournal.org`. As a reminder, this license does not transfer any copyright, but makes it easier for LiveCoMS to publish the article by clarifying that author does indeed have the right to distribute the article open source. See [copyright licence](https://livecomsjournal.github.io/authors/policies/#copyright-license) section for more information. 
- Within a few days of verifying the metadata and providing the lede, you will be notified by the editors about the volume, year, article number, and DOI (which will not yet be active, but will become active after posting the ASAP article). Finalize the LiveCoMS footer by changing the `ASAPversion` class to the `pubversion` class option in the document preamble, and use this information to fill in the `\pubvolume`, `\pubissue`, `\pubyear`, `\articlenum`, and `\pubDOI` fields.   
- Do a final check for issues with grammar, word choice, spelling, formatting (including issues with the LaTeX template, placement of figures, etc.) and typos. This step replaces the galley proofs stage in many other journal article preparation processes. Please [reference the appropriate part of the author instructions](https://livecomsjournal.github.io/authors/policies/#writing-style-and-editing) for what to look for in final checks and updating. Note that authors bear ultimate responsibility for ensuring the writing is of good quality. Editors may suggest improvements, but this is at their discretion.
- Recompile the PDF, and check it into your GitHub repository under the folder `releases/LiveCoMS_Article_ASAP_VX.pdf`, where 'X' is the current article version, along with any final corrections as noted above.
- The represenatative header image (which was submitted in the original submission for review, but can be updated at this point if desired) should be available on the GitHub repository as `releases/header_VX.jpg`, where again 'X' is the current article version, and notify the editor when this has been done. 
- After being published as an ASAP article, but before the article is published in the next regularly scheduled issue, you will have a final chance to fix minor typos and inaccuracies (but not substantive content). Beyond that, any typos will remain in the LiveCoMS version until the next peer-reviewed version.  Changes can of course be made at any time in the authors’ maintained version on GitHub, which is linked from the article itself.  The managing editors will notify you approximately a week before the official release of the issue that your article will appear in.
- At that point, after making these corrections, recompile the PDF, and check it into your GitHub repository under the folder `releases/LiveCoMS_Article_VX.pdf`, where 'X' is the current article version.
- At this point, you should tag the state of the repository as a release ([see instructions for this](https://help.github.com/articles/creating-releases/)), with name `published-version-VX`, where again, 'X' is the current version, and notify the editor of the paper that you have updated the article for issue publication.

# Updating LiveCoMS Articles

A unique aspect of LiveCoMS is article versioning. New versions of manuscripts can be submitted for peer review, to be treated as new publications, with new DOI’s. Authors are therefore encouraged to involve the community in reviewing, improving, and (if warranted) expanding their work, with comments and responses done via the GitHub issue tracker.

We understand that in the evolving lifetime of such a perpetual article, there may be changes in authorship. Our principle is that participants (e.g. new authors, people providing feedback) should receive credit for their contributions. A complete description of LiveCoMS policies for publication credit can be found in the [guide for writing an article for LiveCoMS](https://livecomsjournal.github.io/).

Once peer reviewed, articles receive new [digital object identifiers (DOIs)](https://www.doi.org/) and are published on the LiveCoMS site as new versions.
This allows authors to receive credit for ongoing work they do on their articles.

Authors are encouraged to make updates to articles in their GitHub repositories as frequently as warranted. When the author feels the article is sufficiently different from a previously published LiveCoMS article, they can submit a new version for publication. A description of the versioning process can be found in the guide for writing an article for LiveCoMS. Release of new peer-reviewed versions via LiveCoMS is warranted only when changes become particularly extensive or important, and authors must justify why a peer-reviewed update is needed. As a rough guide, versioning should typically be done no more frequently than every 12-24 months.

The review process for an update to a LiveCoMS article is similar to the review process for the initial version.  
Important additional review criteria for a revision will include whether or not issues the community raised on the article's issue tracker were responded to, and whether the revision includes sufficient new material.

Certain categories of article may need revision at different frequencies.
For information on the review frequencies, see [author information for each of the types of articles](#types-of-articles).

LiveCoMS uses a versioning scheme for articles according to the basic form of `(major version).(minor version)`. The `(major version)` increments following peer review. Prior to initial publication, articles intended for LiveCoMS should use version numbers less than 1.0. Once accepted for the first time, the article becomes Article v1.0. Both the ASAP articles initially posted and the final version published as part of an issue are considered Article V1.0, but the ASAP versions are marked as such on the pdf. When updating the GitHub version of the article, authors should update the version number, for example, something like Article v1.1, such that the minor version indicates a revision to the peer-reviewed major version. In between peer-reviewed, journal-published versions, which are denoted Article VX.0, where X is an integer, authors should use numbers >X.0 and <X+1.0 in the GitHub version, until the article is accepted the next time to LiveCoMS, when its version number is incremented to X+1.0. Authors are free may adopt any other versioning conventions that do not contract the essential `(major version).(minor version)` scheme, such as descriptive tags or a third `(patch verison)`, if desired. 

## Engaging the Community in Improving Articles

We require GitHub use for papers as it provides an easy mechanism for community feedback on the paper, allowing questions, comments, or additions.
Community members can easily [file issues](https://help.github.com/articles/about-issues/) on these topics, and then these can be incorporated into new versions of the article. This can help LiveCoMS articles truly become living documents.
Please note: The issue tracker for these documents is not just for *problems* with the articles, but also for general discussion, feedback, questions, and so on---basically, for any type of discussion about the article.

We are sympathetic to the fact that some commenters may wish to provide feedback to authors outside of GitHub.
This can be done via any suitable means, such as contacting the relevant authors directly.


## Paper Writing as Code Development

This model of updatable papers, curated with community input, allows paper-writing to become much more like code development -- a process of iterative improvement.
This approach can be called [paper writing as code development](https://livecomsjournal.github.io/about/paper_code), and allows authors to benefit from well-established practices and tools which help code developers.

# Authorship and Changes to Authorship

LiveCoMS' focus on "living" documents, can make authorship attribution complicated as the document evolves and more people contribute.
Our key principle is that participants should get credit for their contributions, whether they write the document, provide feedback, file issues, or participate in other ways.

However, different types of credit may be warranted.
In general, changes which constitute writing a significant part of the article merit authorship, but not those which only modify small portions.

In order to acknowledge more minor contributors, people who offer comments/citations that are used in the paper should be listed on the relevant GitHub repository README Markdown file, and should be listed in the acknowledgments section of the paper.
However, if the current authors feel that the contributions rise to the level of authorship, they can add new authors when the next major version is submitted.

Exactly what constitutes a "significant" contribution is by necessity subjective, and authors should endeavor to be generous.
In general, LiveCoMS expects that authors and contributors will be able to sort out these issues amicably. Authors should determine the author order among themselves.
We offer the following guidelines for contributors:
- *Contributors who deserve authorship*: If contributions are particularly significant (e.g., resulting in a new section added the manuscript),
 addition to authorship may be warranted. Ideally, contributors concerned about authorship should, before contributing, discuss with existing authors whether their contribution will merit authorship.
- *Contributions not being accepted*: If contributors are making suggestions or proposing changes which are being
ignored or rejected, the contributors should first strive to convince the authors and community of the contributions' merit
by providing sufficiently compelling data and arguments. If this fails, the lack of engagement with issues raised may become a factor considered by the editors during the review process of subsequent versions of the paper.
- *Review of subsequent versions*: GitHub provides an automatic mechanism for tracking contributions via the GitHub repository's history. This should be examined when revised versions of the article are being considered for publication both to ensure appropriate credit is being given, and to check that authors are engaging with and addressing substantial issues raised by the community. A failure to substantively engage in discussions on issues raised may prevent new updates of the work from being accepted.

# Other Policies for Submitted Articles

Articles do not need to contain original research, but may do so.

There are no explicit length limits on any manuscript, but authors are reminded that excessive length discourages readership. In cases where the authors find a lengthy article is required, careful organization with descriptive sectioning is highly recommended.

## Funding Compliance
Authors are required to report funding sources and grant/award numbers relevant to the manuscript for ALL authors.

Authors should note whether any funding could be perceived as a conflict of interest, e.g., an article describing software in which an author has a financial interest.

## Licensing

LiveCoMS does not request or allow any copyright transfer.

However, in order to submit to LiveCoMS, authors must provide, at
minimum, a license for LiveCoMS to publish the article and distribute
it free of charge. We recommend that the authors release the article
under an open source license such as [Creative Commons
  Attribution](https://creativecommons.org/licenses/by/4.0/) (also known as CC-BY) releasing the document for anyone to copy and
redistribute the material in any medium or format, and remix,
transform, and build upon the material for any purpose, even
commercially.  Making it available to all makes it possible
for LiveCoMS to publish it, and for the community to edit and
contribute.  We highly recommend the CC-BY license in order to ensure
your work can reach and help the broadest audience possible, and
suggest that when considering the appropriate license you [read this analysis](http://openaccess.ox.ac.uk/2013/06/13/cc-by-what-does-it-mean-for-scholarly-articles-3/).

Other more restrictive licenses may be permissible as long as LiveCoMS
has the permission to publish and excerpt from the document.
A different license might be needed if someone other than the authors has some rights to
the material (for example, if it was previously published in another journal). Generally, we only allow a more restrictive license in
these cases, but are happy to discuss any licensing concerns. Please ask the managing editors
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
Preprints are not considered prior publication.
Documents that are major revisions of previously published articles are welcomed.
However, authors should ensure that any material they publish in LiveCoMS is not subject to licensing restrictions (such as from another journal) which impedes its release under the selected license.
Some journals let the authors retain the right to create derivative works, which could perhaps be exercised in preparing a review to be published in LiveCoMS.
Authors are responsible for obtaining all needed permissions to include previously published material, including figures.

If an article is an adaptation of a previously published article, it must be noted in the submission cover letter and major changes noted.
Evaluating whether such changes constitute a significant revision will be part of the review process.

## Author contributions and order

Authors should, to the extent possible, determine the author order among themselves.  
Each work must have a section describing the actual contributions of
authors (and of those acknowledged) to provide clarity, and journal
templates include such a section.  Please note: since this is an
electronic-only journal, there is no length limit when describing
the authors' contributions, so we recommend describing what authors
actually did rather than simply categorizing them in a small number of
predefined roles as might be done in more conventional journals.
<!-- MRS: still need to add that section of the templates somewhat -->  

## Abandoned Documents

By the submission of their paper, document, or materials, **all the
authors consent that if they no longer are willing or able to maintain
their work, LiveCoMS may assign another individual or individuals to
do so**, with appropriate modifications to the authors list. Authors
will first be given written notice (by e-mail and formal letter) if this
were to happen and would have a period of six months to respond and/or
designate a successor before LiveCoMS would do so for them. Typically,
authors are *implicitly* giving a right to do this via licensing under
[Creative Commons - Attribution](https://creativecommons.org/licenses/by/4.0/) or
similar licenses which give others the right to create derivative
works (potentially allowing others to "resurrect" a document which
has been abandoned). However, all authors must *explicitly*
consent to this policy to avoid any confusion. Ordinarily, we expect
this policy will be relevant only in unusual or extreme cases where an
author or authors leaves the field; in most other cases
authors will presumably be available to designate their own successors
or succession plan if a work is valuable to the field and will
continue to need maintenance and the original author(s) are no longer
willing or able to do so in a timely manner.

Thus, for these reasons, authors submitting to LiveCoMS are agreeing
that others may take over authorship of their article (with
appropriate acknowledgment/recognition of the original authors) if
they have abandoned their article as described above, and that
LiveCoMS may accept revised versions of papers which have amended
authorship in such circumstances.
