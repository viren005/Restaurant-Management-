# Generated by Django 5.0.6 on 2024-07-24 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_alter_chef_last_login_alter_waiter_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 7, 24, 6, 34, 56, 131527, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 7, 24, 12, 4, 56, 131527)),
        ),
    ]
