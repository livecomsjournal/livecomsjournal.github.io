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

{% for collection in site.collections %}
  {% if collection.label == "author_instructions" %}
    {% for post in collection.docs %}
	  {% if post.layout != "archive" %}
        {% include archive-single.html %}
	  {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
