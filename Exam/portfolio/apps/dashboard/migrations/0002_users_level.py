# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='level',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
