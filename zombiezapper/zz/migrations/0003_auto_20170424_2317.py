# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zz', '0002_auto_20170424_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.IntegerField(blank=True),
        ),
    ]
