# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-03 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20161203_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frequency',
            name='is_daily',
        ),
        migrations.RemoveField(
            model_name='frequency',
            name='is_monthly',
        ),
        migrations.RemoveField(
            model_name='frequency',
            name='is_weekly',
        ),
        migrations.RemoveField(
            model_name='frequency',
            name='is_yearly',
        ),
        migrations.AddField(
            model_name='frequency',
            name='frequency',
            field=models.CharField(default='Default', max_length=100),
            preserve_default=False,
        ),
    ]