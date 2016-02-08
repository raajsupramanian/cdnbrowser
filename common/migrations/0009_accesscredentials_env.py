# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0008_auto_20151216_1214'),
    ]

    operations = [
        migrations.AddField(
                model_name='accesscredentials',
                name='env',
                field=models.ForeignKey(default=None, blank=True, to='common.Environment'),
        ),
    ]
