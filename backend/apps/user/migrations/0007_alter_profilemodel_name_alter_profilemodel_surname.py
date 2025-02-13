# Generated by Django 5.1.6 on 2025-02-06 19:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profilemodel_age_alter_profilemodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Za-z]{1,19}$', 'Only alphabetic letters allowed (1 to 19 characters).')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Za-z]{1,19}$', 'Only alphabetic letters allowed (1 to 19 characters).')]),
        ),
    ]
