# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0004_auto_20151216_1158'),
    ]

    operations = [
        migrations.AlterField(
                model_name='accesscredentials',
                name='updated_date',
                field=models.DateTimeField(default=datetime.datetime(2015, 12, 16, 12, 4, 24, 994138, tzinfo=utc)),
        ),
    ]
