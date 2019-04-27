"""
================================================================================
* File name:
* Author:LYJ
* Description: Django admin site setting file, manage the database moudles and
register them here.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04
* Modify content:
+ import admin
+ from .models import Article
+ Define and register basic admin models. Define list_display.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content: Modify code according to google code style.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-27
* Modify content:
+ Category Tag
+ class CategoryAdmin, TagAdmin
================================================================================
"""


from django.contrib import admin

from .models import  Article
from .models import  Category
from .models import Tag


class ArticleAdmin(admin.ModelAdmin):
	"""Admin class of Article"""
	list_display = ('aid', 'sequence_number', 'title', 'category' ,'publish_date', 'modify_date')


# class LinuxAdmin(admin.ModelAdmin):
# 	"""Admin class of Linux"""
# 	list_display = ('lid', 'sequence_number', 'article_title')

	# Use the @ label define a function to show the detail of foreigner key
	# @staticmethod
	# def article_title(obj):
	# 	return obj.article.title
	#
	# article_title.admin_order_field = 'article_title'


class CategoryAdmin(admin.ModelAdmin):
	"""Admin class of Category"""
	list_display = ('cid', 'name')


class TagAdmin(admin.ModelAdmin):
	"""Admin class of Category"""
	list_display = ('tid', 'name')


# register the database moudles and the corresponding  admin classes.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
