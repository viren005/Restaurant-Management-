# Generated by Django 5.0.6 on 2024-07-24 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waiter', '0003_waitercart_wid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('waitercartid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waiter.waitercart')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
