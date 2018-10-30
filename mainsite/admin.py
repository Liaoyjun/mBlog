from django.contrib import admin

# Register your models here.
from .models import  Article, Linux

"""
It is the Django admin site setting file, if you wang to manage the database moudle, you have to register it here.
"""


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('aid', 'orderNum', 'title', 'pubDate', 'modDate')


class LinuxAdmin(admin.ModelAdmin):
	list_display = ('lid', 'orderNum', 'article_title')
# Use the @ label define a function to show the detail of foreigner key
	@staticmethod
	def article_title(obj):
		return obj.article.title
	article_title.admin_order_field = 'article_title'

# register the database moudle and the corresponding  admin class.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Linux, LinuxAdmin)


