# Generated by Django 4.1.6 on 2023-04-12 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0034_history_event_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='sport_type',
        ),
    ]
