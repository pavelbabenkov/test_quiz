# Generated by Django 4.2 on 2023-04-18 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_q_choose_option_options_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='q_choose_option_answers',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q_choose_option_answerss', to='tasks.q_choose_option'),
        ),
    ]