# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-07 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gamelists1', '0011_item_gamedangler'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Gamedangler',
            new_name='Gamegangler',
        ),
    ]
