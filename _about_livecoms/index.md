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
field and require ongoing updates.  See the main [About page](https://www.livecomsjournal.org/about) for more info.

{% for collection in site.collections %}
  {% if collection.label == "about_livecoms" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
