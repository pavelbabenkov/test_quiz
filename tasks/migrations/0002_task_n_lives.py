# Generated by Django 4.2 on 2023-04-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='n_lives',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
