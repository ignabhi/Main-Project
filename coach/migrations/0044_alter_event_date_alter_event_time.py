# Generated by Django 4.1.6 on 2023-05-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0043_alter_football_performance_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]