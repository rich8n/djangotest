# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handicaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='golfer',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='golfer',
            name='suffix',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
