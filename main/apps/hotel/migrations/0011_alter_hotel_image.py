# Generated by Django 4.1.5 on 2023-08-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_alter_hotel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(null=True, upload_to='hotel_images/.2023-08-24.15-20-26'),
        ),
    ]
