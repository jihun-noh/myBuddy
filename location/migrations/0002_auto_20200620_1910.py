# Generated by Django 3.0.6 on 2020-06-20 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observationpost',
            old_name='obs_post_nm',
            new_name='obs_post_name',
        ),
    ]
