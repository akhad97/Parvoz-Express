# Generated by Django 4.1.5 on 2023-07-19 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_alter_departflight_day_of_week_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departflight',
            name='aviacompany',
        ),
        migrations.RemoveField(
            model_name='departflight',
            name='flight_type',
        ),
        migrations.RemoveField(
            model_name='returnflight',
            name='aviacompany',
        ),
        migrations.RemoveField(
            model_name='returnflight',
            name='flight_type',
        ),
        migrations.DeleteModel(
            name='AviaCompany',
        ),
    ]
