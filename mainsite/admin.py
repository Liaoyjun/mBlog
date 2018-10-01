from django.contrib import admin

# Register your models here.
from .models import  Article, Linux



class ArticleAdmin(admin.ModelAdmin):
	list_display = ('aid', 'orderNum', 'title', 'pubDate', 'modDate')


class LinuxAdmin(admin.ModelAdmin):
	list_display = ('lid', 'orderNum', 'article_title')

	@staticmethod
	def article_title(obj):
		return obj.article.title

	article_title.admin_order_field = 'article_title'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Linux, LinuxAdmin)


