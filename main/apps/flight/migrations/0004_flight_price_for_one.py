# Generated by Django 4.1.5 on 2023-12-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_alter_flightcalculation_remained_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price_for_one',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
