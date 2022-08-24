# Generated by Django 4.1 on 2022-08-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0006_stationmanager_account_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationmanager',
            name='account_status',
        ),
        migrations.AddField(
            model_name='stationmanager',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
