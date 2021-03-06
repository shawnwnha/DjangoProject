# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0002_auto_20180417_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='blogs',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
