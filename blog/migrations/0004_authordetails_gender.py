# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-14 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170614_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='authordetails',
            name='gender',
            field=models.BooleanField(choices=[(0, '男'), (1, '女')], default=0, max_length=1, verbose_name='性别'),
        ),
    ]
