# Generated by Django 3.0.6 on 2020-06-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20200620_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationpost',
            name='obs_lat',
            field=models.DecimalField(decimal_places=15, max_digits=999),
        ),
        migrations.AlterField(
            model_name='observationpost',
            name='obs_lon',
            field=models.DecimalField(decimal_places=15, max_digits=999),
        ),
    ]
