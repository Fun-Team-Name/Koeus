# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2018-09-27 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_room_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='score',
        ),
    ]
