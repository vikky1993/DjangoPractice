# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-15 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurantlocation_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
