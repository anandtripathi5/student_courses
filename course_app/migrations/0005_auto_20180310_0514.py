# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-10 05:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_studentcoursemap'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='course',
        ),
        migrations.AlterModelTable(
            name='studentcoursemap',
            table='student_course_map',
        ),
    ]
