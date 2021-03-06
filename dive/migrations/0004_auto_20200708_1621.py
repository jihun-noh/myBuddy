# Generated by Django 3.0.6 on 2020-07-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dive', '0003_auto_20200707_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divepoint',
            name='latitude',
            field=models.DecimalField(decimal_places=20, max_digits=999),
        ),
        migrations.AlterField(
            model_name='divepoint',
            name='longitude',
            field=models.DecimalField(decimal_places=20, max_digits=999),
        ),
    ]
