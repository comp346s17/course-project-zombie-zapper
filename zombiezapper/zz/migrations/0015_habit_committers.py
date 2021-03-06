# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 20:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zz', '0014_profile_commitments'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='committers',
            field=models.ManyToManyField(related_name='users_committed', through='zz.Commitment', to=settings.AUTH_USER_MODEL),
        ),
    ]
