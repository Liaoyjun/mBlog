"""
================================================================================
* File name:
* Author:LYJ
* Description: Define database models, return value and default sequence number.
* Attention: When using foreigner key, have to manually add a sentence
"on_delete=models.CASCADE" on the migrations files.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04
* Modify content:
+ import models, timezone
+ Define basic models. Define attributes, ranking index, def __unicode__(self).
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content: Modify code according to google code style.
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-27
* Modify content:
+ class Category, Tag
+ foreign key category, tag in class Ariticle
+ attribute views in class Ariticle.
+ def increase_views in class Ariticle
================================================================================
"""


from django.db import models
from django.utils import timezone


class Category(models.Model):
	"""

	"""
	cid = models.CharField(primary_key=True, max_length=200)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.cid


class Tag(models.Model):
	"""

	"""
	tid = models.CharField(primary_key=True, max_length=200)
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.tid


class Article(models.Model):
	"""Basic class of post article"""
	aid = models.CharField(primary_key=True, max_length=200) # aid is used as the slug.
	sequence_number = models.IntegerField()
	title = models.CharField(max_length=200)
	abstract = models.CharField(max_length=400)
	text = models.TextField()
	publish_date = models.DateTimeField()
	modify_date = models.DateTimeField(default=timezone.now)
	# TODO(LYJ):add picture_URL
	# picture_URL =  models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag)
	views = models.IntegerField(default=0)

	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	class Meta:
		ordering = ('-publish_date',)  # Ordered by published data

	def __unicode__(self):
		return self.aid


# class Linux(models.Model):
# 	"""Basic class of category linux"""
# 	lid = models.CharField(primary_key=True, max_length=200)
# 	sequence_number = models.IntegerField()
# 	article = models.ForeignKey('Article', on_delete=models.CASCADE)
#
# 	class Meta:
# 		ordering = ('-lid',)
#
# 	def __unicode__(self):
# 		return self.lid
