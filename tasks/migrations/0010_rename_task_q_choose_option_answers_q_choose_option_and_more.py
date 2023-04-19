# Generated by Django 4.2 on 2023-04-18 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_rename_question_q_logic_task_n_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='q_choose_option_answers',
            old_name='task',
            new_name='q_choose_option',
        ),
        migrations.AddField(
            model_name='q_choose_option',
            name='n_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='q_logic',
            name='n_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='q_logic',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qs_logic', to='tasks.task'),
        ),
    ]
