# Generated by Django 4.1.6 on 2023-05-07 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0041_alter_event_date_alter_event_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cricket_performance',
            old_name='bowling_Style',
            new_name='bowling_style',
        ),
    ]
