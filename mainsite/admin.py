from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')


admin.site.register(Post, PostAdmin)
