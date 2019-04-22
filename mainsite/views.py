"""
================================================================================
* File name:
* Author:LYJ
* Description: Create views here.
* Attention:
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content: Modify the code according to the google code style.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-17
* Modify content: Improve the front end.
"""


from django.shortcuts import redirect
from .models import Article
from .models import Linux
from django.template.loader import get_template
from django.http import HttpResponse
# from datetime import datetime
from django.contrib.sitemaps import Sitemap
import os # Used to get the cpu temperature of pi
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension



def index_page(request):
	"""Return the index page

	:param request:
	:return:
	"""
	# get_template method will search the html template file under
	# the path BASE_DIR/templates
	return HttpResponse(get_template('mainsite/index.html').render())


def show_article(request, className, aid):
	"""Return the article requested

	:param request:
	:param className:
	:param aid:
	:return:
	"""

	# If an error is triggered here, redirect to 404 page.
	try:
		articles = list()
		classes = list()
		preId = -1
		nextId = -1
		n = 0

		# template = get_template('article.html')
		template = get_template('mainsite/article/article.html')
		idList = list()

		# get a list "articles" which contains the articles requested.
		if className == 'all':
			articles = Article.objects.all().order_by('orderNum')
			n = articles.count() # the length of the "articles".
		else:
			if className == 'linux':
				classes = Linux.objects.all().order_by('orderNum')

			for every in classes:
				articles.append(Article.objects.get(aid=every.article.aid))
			n = len(articles)

		# Get the id list from the "articles" list.
		# id list store all the id of the articles that match the class chosen.
		for article in articles:
			idList.append(article.aid)

		# Get the article requested.
		article = Article.objects.get(aid=aid)
		# Use Markdown to render the article, including hightlighting the code,
		# generating the content of article.
		md = markdown.Markdown(extensions=[
		# inclede extention of abbreviation, table, etc.
		'markdown.extensions.extra',
		# TODO(LYJ):code hightlight
		# inclede extention of highlighting code.
		'markdown.extensions.codehilite',
			# inclede extention of generating the content of article.
		# 'markdown.extensions.toc',
		TocExtension(slugify=slugify),
        ])
		article.body = md.convert(article.body)
		article.toc = md.toc




		# Get the current index of the article according the aid
		index = idList.index(article.aid)

		# Get the preId and nextId.
		if index != 0:
			preId = idList[index-1]
		if index != n-1:
			nextId = idList[index+1]

		# Return the request.
		if article is not None:
				# Use render method to transfer variables to the html template.
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/404')


def show_articles_list(request, className):
	"""return the articles list requested.

	:param request:
	:param className:
	:return:
	"""
	template = get_template('mainsite/article_list/article_list.html')
	articles = list()
	classes = list()

	if className == 'all':
		articles = Article.objects.all().order_by('orderNum')
	else:
		if className == 'linux':
			classes = Linux.objects.all().order_by('orderNum')

		for every in classes:
			articles.append(Article.objects.get(aid=every.article.aid))

	html = template.render(locals())
	return HttpResponse(html)

# return the aboutpage
def show_about_page(request):
	"""Return the about page.

	:param request:
	:return:
	"""
	return HttpResponse(get_template('mainsite/about_author_page.html').render())


# return the aboutpage
def show_contact_page(request):
	"""Return the about page.

	:param request:
	:return:
	"""
	return HttpResponse(get_template('mainsite/contact.html').render())

class BlogSitemap(Sitemap):
	"""Basic class for displaying the sitemap of the blog.

	Need to import Sitemap first.
	modDate and aid are attributes from data model Article
	"""
	changefreq = "daily"
	priority = 0.5

	def items(self):
		return Article.objects.all()

	def lastmod(self, obj):
		return obj.modDate

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
