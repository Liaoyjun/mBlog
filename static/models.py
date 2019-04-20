"""
================================================================================
* File name:
* Author:LYJ
* Description: Define database models, return value and default rank oder here.
* Attention: When using foreigner key, have to manually add a sentence
"on_delete=models.CASCADE" on the migrations files.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content: Modify the code according to the google code style.
================================================================================
"""

from django.db import models
from django.utils import timezone


# TODO(LYJ): Change the attribute name according to google code style.
class Article(models.Model):
	"""Basic class of post article"""
	aid = models.CharField(primary_key=True, max_length=200)
	orderNum = models.IntegerField()
	title = models.CharField(max_length=200)
	abstract = models.CharField(max_length=400)
	body = models.TextField()
	pubDate = models.DateTimeField(default=timezone.now)
	modDate = models.DateTimeField(default=timezone.now)
	picURL =  models.CharField(max_length=200)

	class Meta:
		ordering = ('-pubDate',)  # Ordered by published data

	def __unicode__(self):
		return self.title


# TODO(LYJ): Change the attribute name according to google code style.
class Linux(models.Model):
	"""Basic class of category linux"""
	lid = models.CharField(primary_key=True, max_length=200)
	orderNum = models.IntegerField()
	article = models.ForeignKey('Article', on_delete=models.CASCADE)

	class Meta:
		ordering = ('-lid',)

	def __unicode__(self):
		return self.lid
