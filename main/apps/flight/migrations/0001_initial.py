# Generated by Django 4.1.5 on 2023-08-18 05:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('aviacompany_name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_arrival_1', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_seats_1', models.IntegerField(blank=True, null=True)),
                ('full_name_1', models.CharField(blank=True, max_length=100, null=True)),
                ('landing_date_1', models.DateField(blank=True, null=True)),
                ('landing_time_1', models.DateTimeField(blank=True, null=True)),
                ('day_of_week_1', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_departure_1', models.CharField(blank=True, max_length=100, null=True)),
                ('departure_date_1', models.DateField(blank=True, null=True)),
                ('departure_time_1', models.DateTimeField(blank=True, null=True)),
                ('phone_number_1', models.CharField(blank=True, max_length=50, null=True)),
                ('aviacompany_name_2', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_arrival_2', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_name_2', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_seats_2', models.IntegerField(blank=True, null=True)),
                ('full_name_2', models.CharField(blank=True, max_length=100, null=True)),
                ('landing_date_2', models.DateField(blank=True, null=True)),
                ('landing_time_2', models.DateTimeField(blank=True, null=True)),
                ('day_of_week_2', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_departure_2', models.CharField(blank=True, max_length=100, null=True)),
                ('departure_date_2', models.DateField(blank=True, null=True)),
                ('departure_time_2', models.DateTimeField(blank=True, null=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=50, null=True)),
                ('aviacompany_name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_arrival_3', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_seats_3', models.IntegerField(blank=True, null=True)),
                ('full_name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('landing_date_3', models.DateField(blank=True, null=True)),
                ('landing_time_3', models.DateTimeField(blank=True, null=True)),
                ('day_of_week_3', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_departure_3', models.CharField(blank=True, max_length=100, null=True)),
                ('departure_date_3', models.DateField(blank=True, null=True)),
                ('departure_time_3', models.DateTimeField(blank=True, null=True)),
                ('phone_number_3', models.CharField(blank=True, max_length=50, null=True)),
                ('aviacompany_name_4', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_arrival_4', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_name_4', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_seats_4', models.IntegerField(blank=True, null=True)),
                ('full_name_4', models.CharField(blank=True, max_length=100, null=True)),
                ('landing_date_4', models.DateField(blank=True, null=True)),
                ('landing_time_4', models.DateTimeField(blank=True, null=True)),
                ('day_of_week_4', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_departure_4', models.CharField(blank=True, max_length=100, null=True)),
                ('departure_date_4', models.DateField(blank=True, null=True)),
                ('departure_time_4', models.DateTimeField(blank=True, null=True)),
                ('phone_number_4', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Flight',
                'verbose_name_plural': 'Flights',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='FlightType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(choices=[('Direct flight', 'Direct flight'), ('Charter flight', 'Charter flight')], max_length=100)),
            ],
            options={
                'verbose_name': 'Flight Type',
                'verbose_name_plural': 'Flight Types',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='FlightCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('number_of_seat', models.IntegerField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('prepayment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calculations', to='flight.flight')),
            ],
            options={
                'verbose_name': 'FlightCalculation',
                'verbose_name_plural': 'FlightCalculations',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='FlightBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=50)),
                ('is_viewed', models.BooleanField(default=False)),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
            ],
            options={
                'verbose_name': 'FlightBook',
                'verbose_name_plural': 'FlightBooks',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flighttype'),
        ),
    ]