# Generated by Django 5.0.6 on 2024-07-23 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_tables_alter_chef_last_login_alter_waiter_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 7, 23, 9, 26, 48, 802085, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 7, 23, 9, 26, 48, 802085, tzinfo=datetime.timezone.utc)),
        ),
    ]
