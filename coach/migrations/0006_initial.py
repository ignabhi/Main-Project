# Generated by Django 4.1.6 on 2023-02-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coach', '0005_delete_auth_user_coach'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
                ('rules', models.CharField(max_length=100)),
                ('required_candidates', models.IntegerField()),
                ('coordinator', models.CharField(max_length=50)),
                ('coordinator_cont_info', models.IntegerField()),
            ],
        ),
    ]