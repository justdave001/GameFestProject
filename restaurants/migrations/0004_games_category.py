# Generated by Django 2.0b1 on 2019-01-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20190127_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
