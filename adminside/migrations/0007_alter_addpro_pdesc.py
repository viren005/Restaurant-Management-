# Generated by Django 5.0.6 on 2024-06-21 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0006_addpro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpro',
            name='pdesc',
            field=models.CharField(max_length=500),
        ),
    ]
