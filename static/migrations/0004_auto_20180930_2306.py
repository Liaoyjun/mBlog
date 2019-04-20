# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_linux_ordernum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='aid',
            field=models.CharField(primary_key=True, max_length=200, serialize=False),
        ),
        migrations.AlterField(
            model_name='linux',
            name='lid',
            field=models.CharField(primary_key=True, max_length=200, serialize=False),
        ),
    ]
