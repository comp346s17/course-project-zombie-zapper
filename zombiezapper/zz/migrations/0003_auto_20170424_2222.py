# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zz', '0002_habit_cateogry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='cateogry',
            new_name='category',
        ),
    ]