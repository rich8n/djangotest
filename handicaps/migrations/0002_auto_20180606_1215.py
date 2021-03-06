# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handicaps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfer',
            name='role',
            field=models.CharField(blank=True, choices=[('Member', 'Member'), ('Captain', 'Captain')], default='Member', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='golfer',
            name='status',
            field=models.CharField(choices=[('Team', 'Team'), ('Substitute', 'Substitute'), ('Inactive', 'Inactive')], default='Team', max_length=12),
        ),
        migrations.AlterField(
            model_name='golfer',
            name='tees',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
