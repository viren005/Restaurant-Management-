# Generated by Django 5.0.6 on 2024-07-11 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0012_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='bannerimage',
        ),
    ]
