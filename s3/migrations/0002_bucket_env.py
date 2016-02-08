# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0011_auto_20151216_1401'),
        ('s3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
                model_name='bucket',
                name='env',
                field=models.ForeignKey(default=None, blank=True, to='common.Environment', null=True,
                                        verbose_name=b'Environment'),
        ),
    ]
