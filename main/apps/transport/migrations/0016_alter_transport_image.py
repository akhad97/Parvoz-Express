# Generated by Django 4.1.5 on 2023-08-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0015_alter_transport_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='image',
            field=models.ImageField(null=True, upload_to='transport_images/.2023-08-04.10-39-36'),
        ),
    ]
