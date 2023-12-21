# Generated by Django 4.1.5 on 2023-12-08 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0030_alter_landingdata_landing_img_and_more'),
        ('account', '0008_alter_user_agent_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='percent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='AgentCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tourpackage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='package.tourpackage')),
            ],
            options={
                'verbose_name': 'AgentCalculation',
                'verbose_name_plural': 'AgentCalculation',
                'ordering': ('-id',),
            },
        ),
    ]
