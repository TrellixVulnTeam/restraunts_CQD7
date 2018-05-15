# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-24 06:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restraunt', '0007_restlist_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restlist',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restlist',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]