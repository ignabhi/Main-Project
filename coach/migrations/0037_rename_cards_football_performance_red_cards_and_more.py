# Generated by Django 4.1.6 on 2023-04-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0036_alter_problem_recovery_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='football_performance',
            old_name='cards',
            new_name='red_cards',
        ),
        migrations.AddField(
            model_name='football_performance',
            name='yellow_cards',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
