# Generated by Django 4.1.5 on 2023-08-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_guide_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
