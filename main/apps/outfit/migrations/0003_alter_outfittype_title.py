# Generated by Django 4.1.5 on 2023-08-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outfit', '0002_alter_outfit_outfit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfittype',
            name='title',
            field=models.CharField(choices=[('Kamzul', 'Kamzul'), ("Qo'l sumka", "Qo'l sumka"), ('Yon sumka', 'Yon sumka'), ('Beyjik', 'Beyjik'), ("Ro'mol", "Ro'mol"), ('Futbolka', 'Futbolka'), ("Pinka ko'ylak", "Pinka ko'ylak"), ('Exrom', 'Exrom'), ('Bagach sumka', 'Bagach sumka'), ('Yaxtak va Shalvar', 'Yaxtak va Shalvar'), ("Ofis sovg'asi", "Ofis sovg'asi")], max_length=100),
        ),
    ]
