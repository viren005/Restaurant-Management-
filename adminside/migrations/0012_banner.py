# Generated by Django 5.0.6 on 2024-07-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0011_rename_addpro_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannername', models.CharField(max_length=100)),
                ('bannerdescription', models.CharField(max_length=1000)),
                ('bannerimage', models.URLField()),
            ],
            options={
                'db_table': 'banner',
            },
        ),
    ]
