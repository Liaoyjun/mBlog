# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('aid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.CharField(max_length=400)),
                ('body', models.TextField()),
                ('pubDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('modDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('picURL', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('-pubDate',),
            },
        ),
        migrations.CreateModel(
            name='Linux',
            fields=[
                ('lid', models.IntegerField(primary_key=True, serialize=False)),
                ('aid', models.ForeignKey(to='mainsite.Article', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ('-lid',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
