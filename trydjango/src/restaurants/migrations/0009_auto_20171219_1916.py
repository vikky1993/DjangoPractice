# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20171219_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
