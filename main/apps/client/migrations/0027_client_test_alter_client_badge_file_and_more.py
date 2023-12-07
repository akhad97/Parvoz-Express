# Generated by Django 4.1.5 on 2023-12-07 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0026_remove_client_contract_signin_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='test',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='badge_file',
            field=models.FileField(null=True, upload_to='badge_client_files/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contract_file',
            field=models.FileField(null=True, upload_to='client_contract_files/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contract_signin_image',
            field=models.ImageField(null=True, upload_to='client_contract_signin_images/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='client',
            name='passport_img',
            field=models.ImageField(null=True, upload_to='client_images/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='client',
            name='visa_file',
            field=models.FileField(null=True, upload_to='visa_files/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='badge_file',
            field=models.FileField(null=True, upload_to='badge_partner_files/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='passport_image',
            field=models.ImageField(null=True, upload_to='pass_partner_images/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='visa_file',
            field=models.FileField(null=True, upload_to='pass_visa_files/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='visaclient',
            name='passport_img',
            field=models.ImageField(null=True, upload_to='visa_client_pass_imgs/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='visaclient',
            name='visa_file',
            field=models.FileField(null=True, upload_to='visa_client_files/.2023-12-07.10-33-18'),
        ),
        migrations.AlterField(
            model_name='visapartner',
            name='passport_image',
            field=models.ImageField(null=True, upload_to='visa_partner_pass_imgs/.2023-12-07.10-33-18'),
        ),
    ]
