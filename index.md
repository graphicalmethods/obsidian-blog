---
title: 
header: 
description:
link: /
layout: default
---

{% for post in site.posts %}
  <p>
    <a href="{{ post.url | absolute_url }}">{{ post.title }}</a><br>
      {{ post.date | date_to_string }}
  </p>
  <hr>
{% endfor %}