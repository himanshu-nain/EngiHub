# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 06:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_file_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploader',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]