# Generated by Django 4.2.3 on 2023-08-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0003_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
    ]
