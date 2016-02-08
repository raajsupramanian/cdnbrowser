# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0003_auto_20151216_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
                name='accesscredentials',
                options={'verbose_name_plural': 'Access Details'},
        ),
        migrations.AlterField(
                model_name='accesscredentials',
                name='updated_date',
                field=models.DateTimeField(default=datetime.datetime(2015, 12, 16, 11, 58, 16, 966594, tzinfo=utc)),
        ),
    ]
