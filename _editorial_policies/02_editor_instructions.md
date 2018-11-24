---
layout: single
sidebar:
  nav: editor_instructions.md
title: Instructions for Editors
excerpt: Instructions for editors
permalink: /policies/editor_instructions/
---

This provides instructions to editors handling manuscripts for LiveCoMS.

## Workflow overview

Authors contact LiveCoMS (specifically, the Section Lead Editor reponsible for the corresponding article type) with a presubmission letter, proposing an article in a particular topic area. The Section Lead Editor assigns this presubmission letter to an Associate Editor, who works with the authors to revise the article plans to be suitable for LivCoMS, and the Section Lead Editor signs off on the final plans.
Once the presubmission letter is approved, the author proceeds with article preparation and ultimately submits the article to LiveCoMS.
The Lead Editor then checks that the article is consistent with what was proposed in the presubmission letter, and assigns it to an appropriate Associate Editor who manages the review process and makes a final decision on the manuscript, reporting the final decision to the authors. Usually this Associate Editor will be the same one that handled the original presubmission letters.

## Pre-submission letters

Assuming the subject matter proposed in the presubmission letter is within the scope of LiveCoMS and is otherwise acceptable, the Section Lead Editor assigns this presubmission letter to an Associate Editor. Reasons for the letter not being acceptable include, for example, ignoring key required elements of the presubmission letter or being too similar to existing LiveCoMS articles. The Section Lead Editor signs off on the final presubmission letter, and the Associate Editor notifies the author that the letter is approved.  Instructions for the presubmission letter are [found here](https://github.com/livecomsjournal/livecomsjournal.github.io).

## Pre-review processing

### Lead Editor

The Section Lead Editor:
- Passes the article to an appropriate Associate Editor to manage the review process (unless he or she decides to manage the review process directly). Usually, this will be the Associate Editor who handled the presubmission letter; if not, the Section Lead editor also will communicate the approved presubmission letter.
- Usually will delegate the final decision to the Associate Editor. If the Section Lead Editor anticipates their input may be necessary, they will notify the Associate Editor at the time of them anuscript submission, or if not, as soon as they become aware additional input may be necessary. They may overrule the Associate Editor after acceptance, but this should only be done in exceptional cases, for example, fraud or plagarism. If there are important scientific changes that need to be made in the article that were not caught by Associate Editors previous to acceptance, these can be handled by an unofficial request for revision before the paper is officially posted, or between ASAP posting and the issue publication.

### Associate Editor

Before assigning manuscripts for review, editors have several main tasks:
- Confirms that the article is consistent with the presubmission letter.
- Ensure they do not have a conflict of interest with respect to the work they are to analyze; if they do, [dealing with it as dictated by editorial policy](https://livecomsjournal.github.io/policies/livecoms_bylaws/#iii-conflicts-of-interest).
- Ensure that if any editors are authors on the paper, they are prevented from seeing the manuscript. [See here how to hide the manuscript from them](http://help.scholasticahq.com/customer/en/portal/articles/1728879-can-i-hide-a-manuscript-from-another-editor-?t=565043)
- Check to ensure that the manuscript has appropriate style, grammar, layout, and figure quality to be ready for editing, as in the [instructions for authors](https://livecomsjournal.github.io/authors/policies/). Remember, the journal will not be editing the manuscript, so you need to make a judgment call as to whether the manuscript is well-edited enough to proceed to review, or whether it will need revision for grammar or style *before* sending it for review to avoid wasting the time of the reviewers.
- Identify suitable reviewers, who may include experts suggested by the authors, others in the field you already know of, or authors cited frequently in the article. 
  LiveCoMS generally requires at least two standard reviewers in addition to a student reviewer, though exceptional circumstances (such as extensive community feedback via GitHub) may warrant deviations from this policy. The requirement for a student reviewer for every submission is a unique strength of LiveCoMS that enhances the pedagogical value of every accepted paper.
- The Associate Editor should also notify get the Section Lead ditor if there is any controversy expected (e.g. the reviewers disagree significantly on the merits of the paper, any plagarism potentially evident).


## Review handling

Once an editor has handled the pre-review steps described above, the review process is largely similar to typical journals. The editor:
- Contacts suitable reviewers to request reviews, including a student reviewer, noting our conflict of interest policy. Timing and policy details will be automatically provided to reviewers via the form-letter requests.  Reviews will be due in 15 days, though requests for extension will be routinely granted, for an additional 7-10 days.  In the event a reviewer misses an extended deadline, the editor should request an additional reviewer. 
- Begins the process of conveying reviews to authors once two have been received, unless the need for additional expertise requires a third review. In addition to the two required peer reviews, a student review must also be obtained. A student reivew may be edited to ensure anonymity and proper tone, but not for substance.

- Handles any potential conflict of interests disclosed by reviewers consistent with [editorial policy](https://livecomsjournal.github.io/policies/editorial_board/)
- Makes reviewers aware of the [review criteria](https://livecomsjournal.github.io/authors/policies/reviewer_information), including category-specific review criteria
- Performs a check that the GitHub repository contains all of the files in the submission.
- Ensures reviews are submitted and analyzed in a timely manner (all reviews should be submitted in no more than about 25 days), reaching out to remind reviewers as needed and solicit additional reviews if reviewers are too slow or their analysis conflicts
- Potentially helps ensure reviewer feedback is fair
- Helps preserve anonymity of the reviewers, especially the student reviewer, by editing the reviews if necessary.  Note that the reviewers may choose to waive anonymity by specifically referring to GitHub issues they have filed or otherwise explicitly making it clear they intend to identify themselves.
- Makes a recommendation regarding acceptance, acceptance with minor or major revision, or rejection (keeping in mind the content of the presubmission letter), and communicates this recommendation to the Lead Editor who makes a final decision. Normally the Lead Editor will follow the handling editor's recommendations, but this process is helpful since the Lead will have approved the presubmission letter and thus needs to be involved if a less than favorable decision is to be made.
- If the decision is that the authors must revise, provides appropriate direction (with the Lead Editor) about which comments to address if needed.

Following acceptance, the procedure is:
- Make sure the metadata is complete in the submission (including institution, ORCID, abstract). 
- Have the managing editor get a DOI to the article (correct metadata is needed for this).
 - For the managing editors to obtain a DOI, email cuscholaradmin@colorado.edu whenever a new article (and/or issue) is up. They will generate and register the DOIs and forward the confirmation emails to managing@livecomsjournal.org.  They need the URL of the new article which includes the title, authors, ORCID IDs, and publication date. 
- Have the author do a final check for issues with grammar, word choice, spelling, formatting (including issues with the LaTeX template, placement of figures, etc.) and typos, as normally would be done at the proofs stage. The editor should provide some light assistance if it may be helpful to getting the article out in a timely manner.
- Have the author enable the LiveCoMS footer by including the 'pubversion' class option in the document preamble, fill in the '\datereceived', '\dateaccepted', and '\pubDOI' fields, and provide a recompiled PDF for posting to the editor handling the submission and a managing editor.  The PDF should be accessible on the GitHub repository as `release/LiveCoMS_Article_VX.pdf`, where 'X' is the current article verrsion. The related header image should be at least 1200 pixels wide and in `.jpg` format, and should be available on the GitHub repository as `release/header_VX.jpg`, where 'X' is the current article version.
- Have the author provide a "lede", a 30 word summary of the article that will accompany the article in social media posts.
- Have a managing editor post the PDF as an ASAP article.
- When assigned to an issue, fill in (or have the author fill in) the '\pubvolume', '\pubyear', and '\articlenum' fields, recompile the PDF, and then provide to a managing editor to update the PDF.

