# Generated by Django 4.1.6 on 2023-05-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_img_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='C:\\PycharmProjects\x08logging_platform\\static\x07ccounts\\img', null=True, upload_to='images/'),
        ),
    ]
