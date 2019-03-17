"""mBlog URL Configuration

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
"""


from django.contrib import admin
from django.urls import path, re_path
from mainsite.views import homepage, showArticle, showArticlesList, showAboutPage
from django.contrib.sitemaps.views import sitemap
from mainsite.views import BlogSitemap

"""
There are two method to match the url, one is to match the head of the url, the other is to use regular expression.
When using regular expression, it will pass the paremeters the the function one by one. The first parameter is the request, the others are the values of "(\w+)".
"""
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', showAboutPage),
    re_path(r'^article/(\w+)/(\w+)/$', showArticle),
    # re_path(r'^post/(?P<classification>\w+)/(?P<aid>\w+)/$', showArticlesList3)
    re_path(r'^article/(\w+)/$', showArticlesList),

    # for the sitemap function
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': BlogSitemap}}, name='django.contrib.sitemaps.views.sitemap')
]



