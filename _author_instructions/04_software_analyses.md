---
layout: single
sidebar:
  nav: authors_software_analyses.md
title: Software Analyses
excerpt: What is a publishable software analyis for molecular simulation packages?
permalink: /authors/software_analyses/
---

## What is a publishable software analysis paper for molecular simulation packages?

Software analysis papers describe attempts to perform the same calculation with a range of different simulation packages, or perform analysis of a single simulation package over a series of releases and over different high performance computational resources. In some cases, comparisons of the same calculation with different methods may also be appropriate for a software analysis paper. Such comparisons should be updated periodically with different versions of
the same programs (or potentially, additional programs).

## Additional criteria considered in review of software analysis papers
* Does the manuscript include developers or advanced users of all programs being compared to ensure that comparisons are fair?
* Are best practices in statistical analysis and simulation usage (such as choice of integrator, long range interaction method, and thermostat/barostat) being used in the software analyses?
* Are the methods applied to systems which for which reliable independent data are available?  Are the systems considered of sufficient complexity that readers will find the results convincing and generalizable?
* Have the authors addressed whether a naive user could expect similar performance and why or why not?
* Have the authors clearly identified both (a) the version(s) of the molecular simulations programs used in the comparison (e.g., through revision control tags, a standard version numbering system, or equivalent) and (b) any modifications made to the source code to facilitate the comparison?
* Is the software already published (required) and is it in sufficiently wide usage to need documented comparisons and peformance measures on an ongoing basis? 
* Do the authors supply run scripts, other supporting files, and analysis routines so that the comparison study can, in principle, be replicated? Does the article identify the version of the distributed run scripts that are used?

## Revision schedule for software analyses 
* Articles should be updated when simulation packages have major revisions, or when the standard benchmarks change.
* Run scripts, supporting files, and analysis routines must be provided via version-controlled repositories, with appropriate updates.
