# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 06:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='commment',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]
