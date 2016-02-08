# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('common', '0011_auto_20151216_1401'),
    ]

    operations = [
        migrations.CreateModel(
                name='Bucket',
                fields=[
                    ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                    ('name', models.CharField(max_length=200)),
                    ('creation_date', models.DateTimeField(default=None)),
                    ('access', models.ForeignKey(to='common.AccessCredentials')),
                ],
                options={
                    'db_table': 'bucket',
                },
        ),
    ]
