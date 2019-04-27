"""
================================================================================
* File name:
* Author:LYJ
* Description: Define custom tags and related function.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-27
* Modify content:
+ from ..models import Category Tag
+ from django import template for calling template.Library()
+ from django.db.models.aggregates import Count or calling Count()
* Additional explanation:
(*) @register.simple_tag: register the function as a custom tag.
"""

# TODO(LYJ):difference between ..model and .model
from ..models import Category
from ..models import Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library() # Instantiate Class template.Library

@register.simple_tag
def get_all_category_name():
	return Category.objects.all()


@register.simple_tag
def get_words_number_of_article(article_text):
	return len(article_text)


@register.simple_tag
def get_number_of_articles_of_category():
	return Category.objects.annotate(number_of_articles=Count('article'))


@register.simple_tag
def get_all_tag_name():
	return Tag.objects.all()