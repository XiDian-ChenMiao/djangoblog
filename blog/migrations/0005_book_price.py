# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-14 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_authordetails_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=5, verbose_name='书籍价格'),
        ),
    ]
