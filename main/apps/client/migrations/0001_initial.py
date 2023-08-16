# Generated by Django 4.1.5 on 2023-08-16 18:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visa', '0001_initial'),
        ('package', '0001_initial'),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
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
                ('passport_img', models.ImageField(null=True, upload_to='client_images/.2023-08-16.18-12-46')),
                ('room_type', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('visa_file', models.FileField(null=True, upload_to='visa_files/.2023-08-16.18-12-46')),
                ('is_badge', models.BooleanField(default=False)),
                ('outfit_size', models.CharField(max_length=50, null=True)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotel_clients', to='hotel.hotel')),
                ('tour_package', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tourpackage_clients', to='package.tourpackage')),
                ('visa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visa.visa')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
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
                ('passport_img', models.ImageField(null=True, upload_to='visa_client_pass_imgs/.2023-08-16.18-12-46')),
                ('room_type', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('visa_file', models.FileField(null=True, upload_to='visa_client_files/.2023-08-16.18-12-46')),
                ('is_badge', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.hotel')),
                ('visa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visa.visa')),
            ],
            options={
                'verbose_name': 'VisaClient',
                'verbose_name_plural': 'VisaClients',
                'ordering': ('-id',),
            },
        ),
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
                ('passport_image', models.ImageField(null=True, upload_to='visa_partner_pass_imgs/.2023-08-16.18-12-46')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('visa_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.visaclient')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Partner',
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
                ('passport_image', models.ImageField(null=True, upload_to='pass_partner_images/.2023-08-16.18-12-46')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('visa_file', models.FileField(null=True, upload_to='pass_visa_files/.2023-08-16.18-12-46')),
                ('is_badge', models.BooleanField(default=False)),
                ('outfit_size', models.CharField(max_length=50, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ('-id',),
            },
        ),
    ]
