# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_courses', '0003_auto_20161019_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='new_courses.Course'),
        ),
    ]
