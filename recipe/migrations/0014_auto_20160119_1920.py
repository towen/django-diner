# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 19:20
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0013_auto_20160110_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='recipe/%Y/%m/%d'),
        ),
    ]