# Generated by Django 4.1.5 on 2023-12-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0033_monthlyexpense_alter_landingdata_landing_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyexpense',
            name='margin',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='landingdata',
            name='landing_img',
            field=models.ImageField(null=True, upload_to='landing_imgs/.2023-12-19.12-31-13'),
        ),
        migrations.AlterField(
            model_name='pdfimage',
            name='airplane',
            field=models.ImageField(null=True, upload_to='pdf_imgs/.2023-12-19.12-31-13'),
        ),
        migrations.AlterField(
            model_name='pdfimage',
            name='airplane_wing',
            field=models.ImageField(null=True, upload_to='pdf_imgs/.2023-12-19.12-31-13'),
        ),
        migrations.AlterField(
            model_name='pdfimage',
            name='logo',
            field=models.ImageField(null=True, upload_to='pdf_imgs/.2023-12-19.12-31-13'),
        ),
        migrations.AlterField(
            model_name='pdfimage',
            name='mecca',
            field=models.ImageField(null=True, upload_to='pdf_imgs/.2023-12-19.12-31-13'),
        ),
        migrations.AlterField(
            model_name='pdfimage',
            name='plane',
            field=models.ImageField(null=True, upload_to='pdf_imgs/.2023-12-19.12-31-13'),
        ),
        migrations.AlterField(
            model_name='pdfimage',
            name='visa',
            field=models.ImageField(null=True, upload_to='pdf_imgs/.2023-12-19.12-31-13'),
        ),
        migrations.AlterField(
            model_name='pdfimage',
            name='wave',
            field=models.ImageField(null=True, upload_to='pdf_imgs/.2023-12-19.12-31-13'),
        ),
    ]
