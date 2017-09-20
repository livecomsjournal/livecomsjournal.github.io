---
title: "Living Journal of Computational Molecular Science"
layout: splash
permalink: /
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/livecoms-splash.jpg
excerpt: "Submission, review, and editorial policies"
intro: 
  - excerpt: 'This website details the submission, review, and editorial policies of LiveCoMS, the Living Journal of Computational Molecular Science. Please visit [www.livecomsjournal.org](http://www.livecomsjournal.org) for more information.'
---

{% include feature_row id="intro" type="center" %}

{% for collection in site.collections %}
  {% if collection.label == "policies" %}
    {% for post in collection.docs %}
      {% include archive-single.html %}
    {% endfor %}
  {% endif %}
{% endfor %}

