# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_users_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users_board', to='dashboard.Users')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='boards_comments', to='dashboard.Boards'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='boards_messages', to='dashboard.Boards'),
            preserve_default=False,
        ),
    ]
