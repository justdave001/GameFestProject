# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-06 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_gameslocation_owner'),
        ('Gamelists1', '0006_remove_item_gameresemblance'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Gamedangler',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='games.gamesLocation'),
            preserve_default=False,
        ),
    ]
