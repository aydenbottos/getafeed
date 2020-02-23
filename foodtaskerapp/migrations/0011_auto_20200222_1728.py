# Generated by Django 3.0.3 on 2020-02-22 06:28

from django.db import migrations, models
import storages.backends.ftp


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0010_auto_20200217_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=models.ImageField(storage=storages.backends.ftp.FTPStorage(), upload_to='meal_images/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(storage=storages.backends.ftp.FTPStorage(), upload_to='restaurant_images/'),
        ),
    ]
