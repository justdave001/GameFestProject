# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-07 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gamelists1', '0007_item_gamedangler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='Gamedangler',
        ),
    ]
