# Generated by Django 5.0.6 on 2024-09-13 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0038_alter_manager_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 9, 13, 15, 18, 26, 652131)),
        ),
    ]
