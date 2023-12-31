# Generated by Django 4.1.5 on 2023-08-18 12:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=120)),
                ('nickname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Guide',
                'verbose_name_plural': 'Guides',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=120)),
                ('nickname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ManagerCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('quantity_by_room_type', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('prepayment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.manager')),
            ],
            options={
                'verbose_name': 'ManagerCalculation',
                'verbose_name_plural': 'ManagerCalculations',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='GuideCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('quantity_by_room_type', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('prepayment', models.DecimalField(decimal_places=2, max_digits=20)),
                ('remained_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.guide')),
            ],
            options={
                'verbose_name': 'GuideCalculation',
                'verbose_name_plural': 'GuideCalculations',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='guide',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managers', to='employee.manager'),
        ),
    ]
