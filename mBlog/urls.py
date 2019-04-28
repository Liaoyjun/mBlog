"""
================================================================================
* File name:
* Author:LYJ
* Description: mBlog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
--------------------------------------------------------------------------------
* Attention: There are two method to match the url, one is to match the head of the url,
the other is to use regular expression. When using regular expression, it will pass the
paremeters the the function one by one. The first parameter is the request, the others
are the values of "(\w+)".
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content: Modify the code according to the google code style.
================================================================================
"""

# TODO(LYJ)add comment and regular expression usage.
from django.contrib import admin
from django.urls import path, re_path
from mainsite.views import index_page
from mainsite.views import show_article
# from mainsite.views import show_articles_list_according_to_category
# from mainsite.views import show_articles_list_according_to_tag
from mainsite.views import show_about_page
from mainsite.views import error_404
from mainsite.views import show_contact_page
from mainsite.views import show_cpu_temperature
from django.contrib.sitemaps.views import sitemap
from mainsite.views import BlogSitemap
from mainsite.views import ArticleList
from mainsite.views import ArticleListAccordingToCategory
from mainsite.views import ArticleListAccordingToTag

urlpatterns = [
    path('admin/', admin.site.urls),
    path('404/', error_404),
    path('', index_page),
    path('about/', show_about_page),
    path('contact/', show_contact_page),

    path('article/all/', ArticleList.as_view()),
    re_path(r'^article/tag/(?P<tag>\w+)/$', ArticleListAccordingToTag.as_view()),
    re_path(r'^article/(?P<category>\w+)/$', ArticleListAccordingToCategory.as_view()),
    re_path(r'^article/(\w+)/(\w+)/$', show_article),
    # re_path(r'^post/(?P<classification>\w+)/(?P<aid>\w+)/$', showArticlesList3)
    # re_path(r'^article/tag/(\w+)/$', show_articles_list_according_to_tag),
    # re_path(r'^article/(\w+)/$', show_articles_list_according_to_category),
    # re_path(r'^article/(\w+)/$', ArticleListAccordingToCategory.as_view()),

    # for the sitemap function
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': BlogSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
    #show CPU Temperature
    re_path(r'^temp/', show_cpu_temperature),


]



