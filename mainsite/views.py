

# Create your views here.

from django.shortcuts import redirect


from .models import Post
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime



'''
def homepage(request):
	posts = Post.objects.all()
	post_lists = list()
	for count, post in enumerate(posts):
		post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
		post_lists.append("<small>" + str(post.body.encode('utf-8')) + "</small><br><br>")

	return HttpResponse(post_lists)
'''


def homepage(request):
	return HttpResponse(get_template('index.html').render())


def showArticle(request, slug):
	template = get_template('article.html')
	try:
		post = Post.objects.get(slug=slug)
# 改写函数 showArticle(request, slug) 为 showArticle(request, slug, label)
# 其中label为标签，如linux或全部。
# 数据库查询 posts=Post.get(label)


# post=posts(slug)
# 经过判断 当前文章是不是最后的文章
# nextSlug=posts.next(post) 或者 = #

		if post is not None:
			html = template.render(locals())
			return HttpResponse(html)
	except:
		return redirect('/404')


def showArticlesList(request):
	template = get_template('articlesList.html')
	posts = Post.objects.all()
	now = datetime.now()
	html = template.render(locals())
	return HttpResponse(html)


def showAboutPage(request):
	return HttpResponse(get_template('about.html').render())