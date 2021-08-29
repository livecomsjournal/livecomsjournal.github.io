---
title: "Living Journal of Computational Molecular Science"
layout: archive
permalink: /authors/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/fuzzy-molecules-cropped.jpg
excerpt: "Author instructions"
---

LiveCoMS handles several different types of manuscripts including [Best Practices Guides](https://livecomsjournal.github.io/authors/best_practices/), [Perpetual Reviews](https://livecomsjournal.github.io/authors/perpetual_reviews/), [Software Analyses](https://livecomsjournal.github.io/authors/software_analyses/), and [Tutorials and Training Articles](https://livecomsjournal.github.io/authors/tutorials/).
Authors wishing to submit to LiveCoMS should briefly review our [guidelines for authors](https://livecomsjournal.github.io/authors/policies/) and send a pre-submission inquiry to the appropriate [Lead Editor](https://www.livecomsjournal.org/index.php/livecoms/about/editorialTeam).
Once this is approved, a brief overview of the process is as follows:
- Prepare your manuscript in LaTeX using a suitable public GitHub repository, using our [LaTeX template](https://github.com/livecomsjournal/article_templates) appropriate for your article type, making sure you adhere to the relevant direction in our [General Author Instructions](https://livecomsjournal.github.io/authors/policies/) as well as the instructions specific to your article type (linked below).
- Carefully edit and check the format of your article, since LiveCoMS will neither edit nor typeset your article for you
- Submit a PDF of your final version via the [LiveCoMS website](livecomsjournal.org).

{% for collection in site.collections %}
  {% if collection.label == "author_instructions" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
