# TODO(LYJ):difference between ..model and .model
from ..models import Category
from ..models import Article
from django import template
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_all_category_name():
	return Category.objects.all()


@register.simple_tag
def get_words_number_of_article(article_text):
	return len(article_text)

@register.simple_tag
def get_number_of_articles_of_category():
	return Category.objects.annotate(number_of_articles=Count('article'))