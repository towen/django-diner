# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 00:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_remove_recipe_instructions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='unit',
        ),
    ]
