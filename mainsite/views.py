# Create your views here.

from django.shortcuts import redirect
from .models import  Article, Linux
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime


# return the homepage
# # The method of get_template will search the html file under the path BASE_DIR/templates
def homepage(request):
	return HttpResponse(get_template('index.html').render())


def showArticle(request, className, aid):
# if something error happen here, it will redirect to 404 page
	try:
		articles = list()
		classes = list()
		preId = -1
		nextId = -1
		n = 0
		template = get_template('article.html')
		idList = list()

## get a list "articles" which contain the articles requested.
## n is the length of the "articles".
		if className == 'all':
			articles = Article.objects.all().order_by('orderNum')
			n = articles.count()
		else:
			if className == 'linux':
				classes = Linux.objects.all().order_by('orderNum')

			for every in classes:
				articles.append(Article.objects.get(aid=every.article.aid))
			n = len(articles)

## Get the article requested.
		article = Article.objects.get(aid=aid)

# Get the id list from the "articles" list.
		for article in articles:
			idList.append(article.aid)

## Get the current index.
		index = idList.index(article.aid)

## Get the preId and nextId.
		if index != 0:
			preId = idList[index-1]
		if index != n-1:
			nextId = idList[index+1]

## Return the request.
		if article is not None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/404')



# return the articles list according to the list name
def showArticlesList(request, className):
	template = get_template('articlesList.html')
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
def showAboutPage(request):
	return HttpResponse(get_template('about.html').render())