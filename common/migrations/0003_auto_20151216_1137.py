# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0002_auto_20151215_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
                name='accesscredentials',
                options={'verbose_name_plural': 'Access Credentials'},
        ),
        migrations.AddField(
                model_name='environment',
                name='default',
                field=models.NullBooleanField(),
        ),
        migrations.AlterField(
                model_name='accesscredentials',
                name='updated_date',
                field=models.DateTimeField(default=datetime.datetime(2015, 12, 16, 11, 37, 8, 339128, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
                name='accesscredentials',
                table='access_details',
        ),
    ]
