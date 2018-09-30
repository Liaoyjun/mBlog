from django.contrib import admin

# Register your models here.
from .models import Post, Article, Linux


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')



class ArticleAdmin(admin.ModelAdmin):
	list_display = ('aid', 'orderNum', 'title', 'pubDate', 'modDate')


class LinuxAdmin(admin.ModelAdmin):
	list_display = ('lid', )


admin.site.register(Post, PostAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Linux, LinuxAdmin)


