# Generated by Django 4.1.5 on 2023-12-04 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_flightcalculation_is_confirm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flightcalculation',
            old_name='is_confirm',
            new_name='confirmed',
        ),
    ]
