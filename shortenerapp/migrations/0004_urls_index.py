# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenerapp', '0003_auto_20180215_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='index',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
