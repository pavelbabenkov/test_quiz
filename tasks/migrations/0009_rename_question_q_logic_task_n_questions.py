# Generated by Django 4.2 on 2023-04-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_q_choose_option_answers_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Q_logic',
        ),
        migrations.AddField(
            model_name='task',
            name='n_questions',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
