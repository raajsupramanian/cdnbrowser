# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0006_auto_20151216_1206'),
    ]

    operations = [
        migrations.AlterField(
                model_name='environment',
                name='default',
                field=models.NullBooleanField(default=False),
        ),
    ]
