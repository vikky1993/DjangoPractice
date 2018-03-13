# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=220)),
                ('title_description', models.TextField(null=True, blank=True)),
                ('title_btn', models.CharField(default=b'Join', max_length=50)),
                ('title_btn_url', models.CharField(max_length=50, null=True, blank=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
