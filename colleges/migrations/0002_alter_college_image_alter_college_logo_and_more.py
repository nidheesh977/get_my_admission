# Generated by Django 4.1.7 on 2023-03-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='image',
            field=models.ImageField(help_text='Select image of size 410x240', upload_to='images/college'),
        ),
        migrations.AlterField(
            model_name='college',
            name='logo',
            field=models.ImageField(help_text='Select image of size 105x105', upload_to='images/college/logos'),
        ),
        migrations.AlterField(
            model_name='collegeimages',
            name='image',
            field=models.ImageField(help_text='Select image of size 650x400', upload_to='images/collegeImages'),
        ),
    ]