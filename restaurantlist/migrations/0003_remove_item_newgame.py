# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-05 23:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gamelists1', '0002_auto_20190706_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='newgame',
        ),
    ]
