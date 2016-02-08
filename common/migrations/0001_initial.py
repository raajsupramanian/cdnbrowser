# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
                name='AccessCredentials',
                fields=[
                    ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                    ('name', models.CharField(max_length=100)),
                    ('access_key', models.CharField(max_length=200)),
                    ('secret', models.CharField(max_length=200)),
                    ('created_date', models.DateTimeField(default=None, blank=True)),
                    ('updated_date',
                     models.DateTimeField(default=datetime.datetime(2015, 12, 15, 15, 2, 9, 691504, tzinfo=utc))),
                ],
                options={
                    'db_table': 'access_credentials',
                },
        ),
        migrations.CreateModel(
                name='Environment',
                fields=[
                    ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                    ('name', models.CharField(max_length=50)),
                    ('description', models.TextField(max_length=200)),
                ],
                options={
                    'db_table': 'environment',
                },
        ),
    ]
