# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-07 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_auto_20180307_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration_in_days',
            field=models.IntegerField(blank=True, default=1, help_text='Duration of course in days'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(blank=True, default=100, help_text='Price in dollar of course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.TextField(blank=True, help_text='Enter a brief description of the course', max_length=1000),
        ),
    ]