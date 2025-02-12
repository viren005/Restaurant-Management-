# Generated by Django 5.0.6 on 2024-06-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0004_alter_udetails_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booktable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField()),
                ('numberofper', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'booktable',
            },
        ),
        migrations.AlterField(
            model_name='udetails',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
