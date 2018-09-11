---
title: "Living Journal of Computational Molecular Science"
layout: archive
permalink: /about/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/fuzzy-molecules-cropped.jpg
excerpt: "About LiveCoMS"
---

The Living Journal of Computational Molecular Science (LiveCoMS)
provides a peer-reviewed home for manuscripts which share best
practices in molecular modeling and simulation. These works are living
documents, regularly updated with community input, and can include
perpetual updated reviews, tutorials, comparisons between software
packages, and other documents which aim to improve the studies in the
field and require ongoing updates.

**Sustainability**: We believe our model for LiveCoMS will ensure the journal's longevity and have significant impact on the field, and have budgeted and planned accordingly. However, as this is a publishing experiment, we are taking several safeguards to ensure research published with LiveCoMS is available for posterity. First, authors retain ownership over their work and control of their GitHub repository, allowing them to reuse it however they see fit, and archive it in any way they like. Second, the University of California library system has agreed to archive each year's publications from LiveCoMS in their eScholarship online repository, ensuring the material is archived for the long term in a way which is independent of our publishing model. 

{% for collection in site.collections %}
  {% if collection.label == "about_livecoms" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
