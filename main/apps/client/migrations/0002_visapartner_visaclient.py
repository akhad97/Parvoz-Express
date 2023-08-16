# Generated by Django 4.1.5 on 2023-08-07 13:23

from django.db import migrations, models
import django.db.models.deletion
import main.apps.client.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0026_alter_hotel_image'),
        ('visa', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('passport_expiration_date', models.DateField()),
                ('series', models.CharField(max_length=100)),
                ('series_number', models.PositiveIntegerField()),
                ('passport_image', models.ImageField(upload_to=main.apps.client.models.upload_visa_partner_passport_images)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='VisaClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('passport_expiration_date', models.DateField()),
                ('series', models.CharField(max_length=100)),
                ('series_number', models.PositiveIntegerField()),
                ('passport_img', models.ImageField(upload_to=main.apps.client.models.upload_visa_client_passport_images)),
                ('room_type', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('visa_file', models.ImageField(null=True, upload_to=main.apps.client.models.upload_visa_file)),
                ('is_badge', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotel')),
                ('visa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visa.visa')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ('-id',),
            },
        ),
    ]
