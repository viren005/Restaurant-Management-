# Generated by Django 5.0.6 on 2024-07-23 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_alter_chef_last_login_alter_tables_tableno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 7, 23, 11, 16, 17, 753710, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 7, 23, 16, 46, 17, 753710)),
        ),
    ]
