# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_linux_ordernum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linux',
            old_name='aid',
            new_name='article',
        ),
    ]
