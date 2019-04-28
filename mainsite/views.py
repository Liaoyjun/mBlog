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
from .models import Category
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
from django.views.generic import ListView


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


class ArticleList(ListView):
	model = Article
	template_name = 'mainsite/article_list/article_list.html'
	context_object_name = 'articles'
	paginate_by = 3

	def get_queryset(self):
		return super(ArticleList, self).get_queryset().order_by('sequence_number')

	def get_context_data(self, **kwargs):
		"""
		在视图函数中将模板变量传递给模板是通过给 render 函数的 context 参数传递一个字典实现的，
		例如 render(request, 'blog/index.html', context={'post_list': post_list})，
		这里传递了一个 {'post_list': post_list} 字典给模板。
		在类视图中，这个需要传递的模板变量字典是通过 get_context_data 获得的，
		所以我们复写该方法，以便我们能够自己再插入一些我们自定义的模板变量进去。
		"""

		# 首先获得父类生成的传递给模板的字典。
		context = super().get_context_data(**kwargs)

		# 父类生成的字典中已有 paginator、page_obj、is_paginated 这三个模板变量，
		# paginator 是 Paginator 的一个实例，
		# page_obj 是 Page 的一个实例，
		# is_paginated 是一个布尔变量，用于指示是否已分页。
		# 例如如果规定每页 10 个数据，而本身只有 5 个数据，其实就用不着分页，此时 is_paginated=False。
		# 关于什么是 Paginator，Page 类在 Django Pagination 简单分页：http://zmrenwu.com/post/34/ 中已有详细说明。
		# 由于 context 是一个字典，所以调用 get 方法从中取出某个键对应的值。
		paginator = context.get('paginator')
		page = context.get('page_obj')
		is_paginated = context.get('is_paginated')

		# 调用自己写的 pagination_data 方法获得显示分页导航条需要的数据，见下方。
		pagination_data = self.pagination_data(paginator, page, is_paginated)

		# 将分页导航条的模板变量更新到 context 中，注意 pagination_data 方法返回的也是一个字典。
		context.update(pagination_data)

		# 将更新后的 context 返回，以便 ListView 使用这个字典中的模板变量去渲染模板。
		# 注意此时 context 字典中已有了显示分页导航条所需的数据。
		return context

	@staticmethod
	def pagination_data(paginator, page, is_paginated):
		if not is_paginated:
			# 如果没有分页，则无需显示分页导航条，不用任何分页导航条的数据，因此返回一个空的字典
			return {}

		# 当前页左边连续的页码号，初始值为空
		left = []

		# 当前页右边连续的页码号，初始值为空
		right = []

		# 标示第 1 页页码后是否需要显示省略号
		left_has_more = False

		# 标示最后一页页码前是否需要显示省略号
		right_has_more = False

		# 标示是否需要显示第 1 页的页码号。
		# 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
		# 其它情况下第一页的页码是始终需要显示的。
		# 初始值为 False
		first = False

		# 标示是否需要显示最后一页的页码号。
		# 需要此指示变量的理由和上面相同。
		last = False

		# 获得用户当前请求的页码号
		page_number = page.number

		# 获得分页后的总页数
		total_pages = paginator.num_pages

		# 获得整个分页页码列表，比如分了四页，那么就是 [1, 2, 3, 4]
		page_range = paginator.page_range

		if page_number == 1:
			# 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）。
			# 此时只要获取当前页右边的连续页码号，
			# 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]。
			# 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
			right = page_range[page_number:page_number + 2]

			# 如果最右边的页码号比最后一页的页码号减去 1 还要小，
			# 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
			if right[-1] < total_pages - 1:
				right_has_more = True

			# 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
			# 所以需要显示最后一页的页码号，通过 last 来指示
			if right[-1] < total_pages:
				last = True

		elif page_number == total_pages:
			# 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空），
			# 此时只要获取当前页左边的连续页码号。
			# 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
			# 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
			left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

			# 如果最左边的页码号比第 2 页页码号还大，
			# 说明最左边的页码号和第 1 页的页码号之间还有其它页码，因此需要显示省略号，通过 left_has_more 来指示。
			if left[0] > 2:
				left_has_more = True

			# 如果最左边的页码号比第 1 页的页码号大，说明当前页左边的连续页码号中不包含第一页的页码，
			# 所以需要显示第一页的页码号，通过 first 来指示
			if left[0] > 1:
				first = True
		else:
			# 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号，
			# 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码。
			left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
			right = page_range[page_number:page_number + 2]

			# 是否需要显示最后一页和最后一页前的省略号
			if right[-1] < total_pages - 1:
				right_has_more = True
			if right[-1] < total_pages:
				last = True

			# 是否需要显示第 1 页和第 1 页后的省略号
			if left[0] > 2:
				left_has_more = True
			if left[0] > 1:
				first = True

		data = {
			'left': left,
			'right': right,
			'left_has_more': left_has_more,
			'right_has_more': right_has_more,
			'first': first,
			'last': last,
		}

		return data


class ArticleListAccordingToCategory(ArticleList):

	def get_queryset(self):
		category = self.kwargs.get('category')
		return super(ArticleListAccordingToCategory, self).get_queryset().filter(category=category).order_by('sequence_number')


class ArticleListAccordingToTag(ArticleList):

	def get_queryset(self):
		tag = self.kwargs.get('tag')
		print("test", tag)
		return super(ArticleListAccordingToTag, self).get_queryset().filter(tag=tag).order_by('sequence_number')


# def show_articles_list_according_to_category(request, category_name):
# 	"""return the articles list requested.
#
# 	:param request:
# 	:param category_name:
# 	:return:
# 	"""
# 	template = get_template('mainsite/article_list/article_list.html')
# 	articles = list()
# 	if operator.eq(category_name, 'all'):
# 		articles = Article.objects.all().order_by('sequence_number')
# 	else:
# 		articles = Article.objects.all().filter(category=category_name).order_by('sequence_number')
# 	html = template.render(locals())
# 	return HttpResponse(html)
#
#
# def show_articles_list_according_to_tag(request, tag_name):
# 	"""return the articles list requested.
#
# 	:param request:
# 	:param tag_name:
# 	:return:
# 	"""
# 	template = get_template('mainsite/article_list/article_list.html')
# 	articles = list()
#
# 	articles = Article.objects.all().filter(tag=tag_name).order_by('sequence_number')
# 	html = template.render(locals())
# 	return HttpResponse(html)


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
