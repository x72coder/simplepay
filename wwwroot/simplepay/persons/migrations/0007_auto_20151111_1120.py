# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_auto_20151111_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='update_time',
            new_name='update_date',
        ),
    ]
