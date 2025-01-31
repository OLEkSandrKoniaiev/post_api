# Generated by Django 5.1.5 on 2025-01-27 19:54

from django.db import migrations, models

import core.services.file_service


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profilemodel_age_alter_usermodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to=core.services.file_service.upload_profile_photo),
        ),
    ]
