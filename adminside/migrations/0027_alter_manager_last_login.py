# Generated by Django 5.0.6 on 2024-07-22 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0026_alter_manager_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 7, 22, 12, 4, 24, 3565, tzinfo=datetime.timezone.utc)),
        ),
    ]
