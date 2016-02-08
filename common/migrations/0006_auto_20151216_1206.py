# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0005_auto_20151216_1204'),
    ]

    operations = [
        migrations.AlterField(
                model_name='accesscredentials',
                name='updated_date',
                field=models.DateTimeField(default=None, blank=True),
        ),
    ]
