# Generated by Django 4.1.6 on 2023-03-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0019_event_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cricket_performance',
            name='batting_style',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cricket_performance',
            name='bowling_Style',
            field=models.CharField(max_length=100),
        ),
    ]
