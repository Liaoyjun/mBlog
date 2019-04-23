"""
================================================================================
* File name:
* Author:LYJ
* Description: Django admin site setting file, manage the database moudles and
register them here.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content: Modify the code according to the google code style.
================================================================================
"""


from django.contrib import admin
from .models import  Article
from .models import  Linux


class ArticleAdmin(admin.ModelAdmin):
	"""Admin class of Article"""
	list_display = ('aid', 'orderNum', 'title', 'publish_date', 'modify_date')


class LinuxAdmin(admin.ModelAdmin):
	"""Admin class of Linux"""
	list_display = ('lid', 'orderNum', 'article_title')

	# Use the @ label define a function to show the detail of foreigner key
	@staticmethod
	def article_title(obj):
		return obj.article.title

	article_title.admin_order_field = 'article_title'


# register the database moudles and the corresponding  admin classes.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Linux, LinuxAdmin)


