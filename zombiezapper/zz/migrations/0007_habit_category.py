# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zz', '0006_commitment_date_commited'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
