from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Q_logic, Q_choose_option, Q_choose_option_answer
from django.contrib.auth.models import User
from .forms import NewQuestionForm

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def task_questions(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'questions.html', {'task': task})

def new_q_logic(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        q_text = request.POST['question']
        correct_answer = request.POST['answer']

        user = User.objects.first()  # TODO: get the currently logged in user

        question = Q_logic.objects.create(
            q_text=q_text,
            correct_answer=correct_answer,
            n_order=task.n_questions+1,
            task=task
        )

        task.n_questions=task.n_questions+1

        task.n_lives = task.n_lives+1
        task.save()

        return redirect('task_questions', pk=task.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_q_logic.html', {'task': task})


def edit_q_logic(request, pk, q_logic_pk):
    question = get_object_or_404(Q_logic, task__pk=pk, pk=q_logic_pk)

    if request.method == 'POST':
        q_text = request.POST['question']
        correct_answer = request.POST['answer']
        question.q_text=q_text
        question.correct_answer=correct_answer
        question.save()
        return redirect('task_questions', pk=question.task.pk)  # TODO: redirect to the created topic page

    return render(request, 'edit_q_logic.html', {'question': question})

def delete_q_logic(request, pk, q_logic_pk):
    question = get_object_or_404(Q_logic, task__pk=pk, pk=q_logic_pk)
    task=get_object_or_404(Task, pk=pk)

    for q_logic in task.qs_logic.all():
        if q_logic.n_order > question.n_order:
            q_logic.n_order = q_logic.n_order - 1
            q_logic.save()

    for q_choose_option in task.qs_choose_option.all():
        if q_choose_option.n_order > question.n_order:
            q_choose_option.n_order = q_choose_option.n_order - 1
            q_choose_option.save()

    task.n_questions=task.n_questions-1
    task.save()

    question.delete()
    # task.n_lives = task.n_lives - 1
    # task.save()

    return render(request, 'questions.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()

    return render(request, 'home.html')

def new_q_choose_option(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        q_text = request.POST['question']
        user = User.objects.first()  # TODO: get the currently logged in user

        question = Q_choose_option.objects.create(
            q_text=q_text,
            n_order=task.n_questions + 1,
            task=task,
        )

        task.n_questions = task.n_questions + 1

        correct_answer = int(request.POST['correct_answer'])

        for i in range(1, 5):
            answer_st = "answer_" + str(i)
            if request.POST[answer_st] != "":
                new_answer=Q_choose_option_answer.objects.create(
                    q_text=request.POST[answer_st],
                    correct_answer=False,
                    option_n=i,
                    q_choose_option=question,
                )
                if correct_answer == i:
                    new_answer.correct_answer = True
                new_answer.save()
                question.options_count=i
                question.save()

        task.n_lives = task.n_lives+1
        task.save()

        return redirect('task_questions', pk=task.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_q_choose_option.html', {'task': task})


def edit_q_choose_option(request, pk, q_choose_option_pk):
    q_choose_option = get_object_or_404(Q_choose_option, task__pk=pk, pk=q_choose_option_pk)

    if request.method == 'POST':
        q_text = request.POST['question']
        q_choose_option.q_text=q_text
        q_choose_option.save()

        correct_answer = int(request.POST['correct_answer'])

        i=0

        for q_choose_option_answer in q_choose_option.q_choose_option_answers.all():
            i=i+1
            answer_st = "answer_" + str(i)
            q_choose_option_answer.q_text=request.POST[answer_st]
            q_choose_option_answer.correct_answer = False
            if correct_answer == q_choose_option_answer.option_n:
                q_choose_option_answer.correct_answer = True
            q_choose_option_answer.save()

        return redirect('task_questions', pk=q_choose_option.task.pk)  # TODO: redirect to the created topic page

    return render(request, 'edit_q_choose_option.html', {'q_choose_option': q_choose_option})

def delete_q_choose_option(request, pk, q_choose_option_pk):
    question = get_object_or_404(Q_choose_option, task__pk=pk, pk=q_choose_option_pk)
    task=get_object_or_404(Task, pk=pk)

    for q_logic in task.qs_logic.all():
        if q_logic.n_order > question.n_order:
            q_logic.n_order = q_logic.n_order - 1
            q_logic.save()

    for q_choose_option in task.qs_choose_option.all():
        if q_choose_option.n_order > question.n_order:
            q_choose_option.n_order = q_choose_option.n_order - 1
            q_choose_option.save()

    task.n_questions = task.n_questions - 1
    task.save()

    question.delete()
    # task.n_lives = task.n_lives - 1
    # task.save()

    return render(request, 'questions.html', {'task': task})