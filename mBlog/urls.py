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


from django.contrib import admin
from django.urls import path, re_path
from mainsite.views import index_page
from mainsite.views import test
from mainsite.views import testAP
from mainsite.views import show_article
from mainsite.views import show_articles_list
from mainsite.views import show_about_page
from mainsite.views import show_contact_page
from mainsite.views import show_cpu_temperature
from django.contrib.sitemaps.views import sitemap
from mainsite.views import BlogSitemap


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('about/', show_about_page),
    path('contact/', show_contact_page),
    re_path(r'^article/(\w+)/(\w+)/$', show_article),
    # re_path(r'^post/(?P<classification>\w+)/(?P<aid>\w+)/$', showArticlesList3)
    re_path(r'^article/(\w+)/$', show_articles_list),
    # for the sitemap function
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': BlogSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
    #show CPU Temperature
    re_path(r'^temp/', show_cpu_temperature),
    path('TAL/', test),
    path('TAP/', testAP)
]



