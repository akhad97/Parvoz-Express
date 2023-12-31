# Generated by Django 4.1.5 on 2023-08-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='gender_type',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='human_development',
            field=models.CharField(choices=[('Infant', 'Infant'), ('Child', 'Child'), ('Adult', 'Adult')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport_img',
            field=models.ImageField(null=True, upload_to='client_images/.2023-08-18.15-46-40'),
        ),
        migrations.AlterField(
            model_name='client',
            name='visa_file',
            field=models.FileField(null=True, upload_to='visa_files/.2023-08-18.15-46-40'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='passport_image',
            field=models.ImageField(null=True, upload_to='pass_partner_images/.2023-08-18.15-46-40'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='visa_file',
            field=models.FileField(null=True, upload_to='pass_visa_files/.2023-08-18.15-46-40'),
        ),
        migrations.AlterField(
            model_name='visaclient',
            name='passport_img',
            field=models.ImageField(null=True, upload_to='visa_client_pass_imgs/.2023-08-18.15-46-40'),
        ),
        migrations.AlterField(
            model_name='visaclient',
            name='visa_file',
            field=models.FileField(null=True, upload_to='visa_client_files/.2023-08-18.15-46-40'),
        ),
        migrations.AlterField(
            model_name='visapartner',
            name='passport_image',
            field=models.ImageField(null=True, upload_to='visa_partner_pass_imgs/.2023-08-18.15-46-40'),
        ),
    ]
