# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20181001_1155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
