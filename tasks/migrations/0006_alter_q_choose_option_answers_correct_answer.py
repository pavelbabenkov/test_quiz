# Generated by Django 4.2 on 2023-04-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_q_choose_option_answers_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='q_choose_option_answers',
            name='correct_answer',
            field=models.BooleanField(),
        ),
    ]
