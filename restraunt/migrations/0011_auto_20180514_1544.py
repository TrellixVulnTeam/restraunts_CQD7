# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-14 10:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt', '0010_auto_20180209_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]