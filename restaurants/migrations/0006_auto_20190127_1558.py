# Generated by Django 2.0b1 on 2019-01-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_games_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='games',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
