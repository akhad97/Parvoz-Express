# Generated by Django 4.1.5 on 2023-08-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0010_alter_transport_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='image',
            field=models.ImageField(null=True, upload_to='transport_images/.2023-08-24.15-20-26'),
        ),
        migrations.AlterField(
            model_name='transportcalculation',
            name='remained_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]