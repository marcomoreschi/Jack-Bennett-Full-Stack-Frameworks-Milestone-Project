# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-03 11:50
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200603_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creator_id',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]