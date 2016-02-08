# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0010_auto_20151216_1231'),
    ]

    operations = [
        migrations.AlterField(
                model_name='accesscredentials',
                name='env',
                field=models.ForeignKey(default=None, blank=True, to='common.Environment', null=True,
                                        verbose_name=b'Environment'),
        ),
    ]
