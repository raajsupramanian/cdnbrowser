# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
                model_name='accesscredentials',
                name='updated_date',
                field=models.DateTimeField(default=datetime.datetime(2015, 12, 15, 15, 3, 8, 114432, tzinfo=utc)),
        ),
    ]
