# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20180930_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linux',
            name='orderNum',
        ),
        migrations.AlterField(
            model_name='article',
            name='aid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='linux',
            name='lid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
