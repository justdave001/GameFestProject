# Generated by Django 2.0b1 on 2019-01-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changes',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]