# Generated by Django 4.1.5 on 2023-12-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_user_is_accountant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agent_id',
            field=models.CharField(blank=True, choices=[('NMA1', 'NMA1'), ('NMA2', 'NMA2'), ('NMA3', 'NMA3'), ('NMA4', 'NMA4'), ('QQN', 'QQN'), ('MRN', 'MRN'), ('AZN', 'AZN'), ('TAS', 'TAS'), ('SKD', 'SKD')], max_length=255, null=True),
        ),
    ]
