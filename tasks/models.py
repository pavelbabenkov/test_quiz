from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=300, unique=True)
    n_lives=models.PositiveIntegerField(default=0)
    n_questions=models.PositiveIntegerField(default=0)

class Q_logic(models.Model):
    q_text = models.CharField(max_length=4000)
    correct_answer = models.BooleanField(null=True)
    n_order = models.PositiveIntegerField(default=0)
    task = models.ForeignKey(Task, related_name='qs_logic', on_delete=models.CASCADE, blank=True, null=True)

class Q_choose_option(models.Model):
    q_text = models.CharField(max_length=4000)
    options_count=models.PositiveIntegerField(default=0)
    n_order = models.PositiveIntegerField(default=0)
    task = models.ForeignKey(Task, related_name='qs_choose_option', on_delete=models.CASCADE, blank=True, null=True)

class Q_choose_option_answer(models.Model):
    q_text = models.CharField(max_length=4000)
    option_n=models.PositiveIntegerField(default=0)
    correct_answer=models.BooleanField(null=False)
    q_choose_option = models.ForeignKey(Q_choose_option, related_name='q_choose_option_answers', on_delete=models.CASCADE, blank=True, null=True)