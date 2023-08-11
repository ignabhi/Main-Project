# Generated by Django 4.1.6 on 2023-03-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coach', '0024_remove_training_event_name_training_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='details',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='achievements',
            name='event_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user_auth',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
