# Generated by Django 2.1.1 on 2019-04-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0010_auto_20190424_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
