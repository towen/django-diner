# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe', verbose_name='recipe'),
            preserve_default=False,
        ),
    ]
