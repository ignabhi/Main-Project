# Generated by Django 4.1.6 on 2023-03-22 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0025_achievements_details_achievements_event_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='football_performance',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.football'),
        ),
    ]
