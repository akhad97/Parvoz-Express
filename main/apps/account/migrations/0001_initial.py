# Generated by Django 4.1.5 on 2023-04-27 10:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(max_length=255, unique=True, verbose_name='Телефонный номер')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя Фамилия')),
                ('email', models.EmailField(max_length=254)),
                ('region', models.CharField(max_length=100)),
                ('user_role', models.CharField(choices=[('owner', 'owner'), ('moderator', 'moderator'), ('salesman', 'salesman')], max_length=50)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting account.', verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-id',),
            },
        ),
    ]
