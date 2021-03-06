# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenerapp', '0002_auto_20180215_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='statistics', max_length=30)),
                ('total_clicks', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='urls',
            options={'ordering': ['-count']},
        ),
    ]
