# Generated by Django 2.0b1 on 2019-01-27 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_games_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
