# Generated by Django 4.1.5 on 2023-08-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0029_alter_hotel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(null=True, upload_to='hotel_images/.2023-08-10.10-57-43'),
        ),
    ]
