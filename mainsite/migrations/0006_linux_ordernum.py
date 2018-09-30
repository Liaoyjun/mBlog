# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20180930_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='linux',
            name='orderNum',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
