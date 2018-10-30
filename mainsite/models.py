from django.db import models
from django.utils import timezone

# Create your models here.

"""
Define the database model here, you can define the return value of the model and the default oder.
When using foreigner key, you have to manually add a sentence "on_delete=models.CASCADE" on the migrations files.

"""



class Article(models.Model):
	aid = models.CharField(primary_key=True, max_length=200)
	orderNum = models.IntegerField()

	title = models.CharField(max_length=200)
	abstract = models.CharField(max_length=400)
	body = models.TextField()
	pubDate = models.DateTimeField(default=timezone.now)
	modDate = models.DateTimeField(default=timezone.now)

	picURL =  models.CharField(max_length=200)
	class Meta:
		ordering = ('-pubDate',)

	def __unicode__(self):
		return self.title



class Linux(models.Model):
	lid = models.CharField(primary_key=True, max_length=200)
	orderNum = models.IntegerField()
	article = models.ForeignKey('Article', on_delete=models.CASCADE)

	class Meta:
		ordering = ('-lid',)

	def __unicode__(self):
		return self.lid
