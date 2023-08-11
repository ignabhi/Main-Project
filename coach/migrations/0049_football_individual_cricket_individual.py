# Generated by Django 4.1.6 on 2023-05-14 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0048_alter_training_reporting_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='football_individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals_scored', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('yellow_card', models.IntegerField()),
                ('red_card', models.IntegerField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.history')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.football_performance')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.football')),
            ],
        ),
        migrations.CreateModel(
            name='cricket_individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs_scored', models.IntegerField()),
                ('wickets_taken', models.IntegerField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.history')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.cricket_performance')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coach.cricket')),
            ],
        ),
    ]