# Generated by Django 4.1 on 2022-09-02 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationrequest',
            name='station_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('0', 'SUPER_ADMIN'), ('1', 'STATION_MANAGER')], default='0', max_length=50),
        ),
    ]