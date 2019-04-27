"""
================================================================================
* File name:
* Author:LYJ
* Description: Create views here.
* Attention:
================================================================================
* Modifier:LYJ
* Modification time: 2019-04
* Modify content:
+ from .models import Article
+ import redirect for calling redirect()
+ import get_template for calling get_template()
+ import HttpResponse for calling HttpResponse()
+ import operator for calling operator.eq().
+ import os for calling os.popen().
+ import markdown, from django.utils.text import slugify, from markdown.extensions.toc import TocExtension
for using MarkDown in def show_article.
+ def index_page, error_404, show_article, show_articles_list_according_to_category,
show_articles_list_according_to_tag, show_about_page, show_contact_page, show_cpu_temperature.
+ Class BlogSitemap
* Additional explanation:
(*) get_template(): will search html template according to directory under
path of BASE_DIR/templates.
(*) template.render():  transfer variables to the html template.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content: Modify the code according to the google code style.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-27
* Modify content:
+
================================================================================
"""


from .models import Article
from django.shortcuts import redirect
from django.template.loader import get_template
from django.http import HttpResponse
# from datetime import datetime
from django.contrib.sitemaps import Sitemap
import os # Used to get the cpu temperature of pi
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
import operator


def index_page(request):
	"""Return index page

	:param request: /
	:return:
	"""


	return HttpResponse(get_template('mainsite/index.html').render())


def error_404(request):
	"""Return 404 page

	:param request: /404/
	:return:
	"""

	return HttpResponse(get_template('mainsite/error_404.html').render())


def show_article(request, category, aid):
	"""Return the article requested according to category name and aid。

	:param request: /article/(\w+)/(\w+)/
	:param category: Category that the article belongs to.
	Used to define the urls of next or previous button.
	:param aid: Id of the article.
	:return:
	"""

	# If an error is triggered here, redirect to 404 page.
	try:
		# initialize variable
		articles = list()
		classes = list()
		idList = list()
		preId = -1
		nextId = -1
		n = 0

		template = get_template('mainsite/article/article.html') # Get html template

		# Get articles list according to category
		if operator.eq(category, 'all'):
			articles = Article.objects.all().order_by('sequence_number')
		else:
			articles = Article.objects.all().filter(category=category).order_by('sequence_number')

		n = articles.count() # the amount of articles.

		# Generate id list from the articles list.
		# Id list stores all of the id of articles in articles list.
		for article in articles:
			idList.append(article.aid)

		article = Article.objects.get(aid=aid) # Get article requested.

		# Use Markdown to render article, including code hightlight and
		# generating content of article.
		md = markdown.Markdown(extensions=[
		'markdown.extensions.extra', # extention for abbreviation, table, and etc.
		# TODO(LYJ)
		# 'markdown.extensions.codehilite', # extention for code highlight.
		# 'markdown.extensions.toc', # inclede extention of generating the content of article.
		TocExtension(slugify=slugify), # Make the anchor of content more beautiful.
        ])
		article.text = md.convert(article.text)
		article.toc = md.toc

		article.increase_views() # increase views time.

		index = idList.index(article.aid) # get index of the current article.

		# Find preId and nextId of the current article.
		if index != 0:
			preId = idList[index-1]
		if index != n-1:
			nextId = idList[index+1]

		if article is not None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/404')


def show_articles_list_according_to_category(request, category_name):
	"""return the articles list requested.

	:param request:
	:param category_name:
	:return:
	"""
	template = get_template('mainsite/article_list/article_list.html')
	articles = list()
	classes = list()
	print("test")
	if operator.eq(category_name, 'all'):
		articles = Article.objects.all().order_by('sequence_number')
	else:
		articles = Article.objects.all().filter(category=category_name).order_by('sequence_number')
	html = template.render(locals())
	return HttpResponse(html)


def show_articles_list_according_to_tag(request, tag_name):
	"""return the articles list requested.

	:param request:
	:param tag_name:
	:return:
	"""
	template = get_template('mainsite/article_list/article_list.html')
	articles = list()
	classes = list()

	articles = Article.objects.all().filter(tag=tag_name).order_by('sequence_number')
	html = template.render(locals())
	return HttpResponse(html)


def show_about_page(request):
	"""Return the about page.

	:param request:
	:return:
	"""
	return HttpResponse(get_template('mainsite/about_author_page.html').render())


# TODO(LYJ): Improve comment.
def show_contact_page(request):
	"""Return the about page.

	:param request:
	:return:
	"""
	return HttpResponse(get_template('mainsite/contact.html').render())


class BlogSitemap(Sitemap):
	"""Basic class for displaying the sitemap of the blog.

	Need to import Sitemap first.
	modify_date and aid are attributes from data model Article
	"""
	changefreq = "daily"
	priority = 0.5

	def items(self):
		return Article.objects.all()

	def lastmod(self, obj):
		return obj.modify_date

	def location(self, obj):
		return obj.aid


# TODO(LYJ):Use js to realize this function.
def show_cpu_temperature(request):
	"""Get the cpu temperature of pi.

	:param request:
	:return:
	"""

	template = get_template('show_pi_temperature.html')
	res = os.popen('vcgencmd measure_temp').readline()
	CPU_temp = res.replace("temp=", "").replace("'C\n", "")
	# print('CPU Temperature = ' + CPU_temp)
	html = template.render(locals())
	return HttpResponse(html)
