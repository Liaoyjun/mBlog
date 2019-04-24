# TODO(LYJ):difference between ..model and .model
from ..models import Category
from django import template

register = template.Library()

@register.simple_tag
def get_all_category_name():
	return Category.objects.all()