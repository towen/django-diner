# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 00:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20160110_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='serving_qty',
            new_name='servings',
        ),
    ]
