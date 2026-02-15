from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskDetailForm, TaskForm
from .models import Task, TaskDetail, InfoByRate


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        default_stage = InfoByRate.objects.all()
        if form.is_valid():
            new_object = form.save()
            for stage in default_stage:
                TaskDetail.objects.create(
                    task=new_object,
                    stage=stage.stage,
                    time_spent=0,
                    name_stage_task=stage.name_stage_info
                )
            return redirect('task_details', pk=new_object.id)
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def add_detail(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.task = task
            detail.save()
            return redirect('task_details', pk=task.pk)
    else:
        form = TaskDetailForm()
    return render(request, 'add_detail.html', {'form': form, 'task': task})


def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    details = task.details.all().select_related('name_stage_task').order_by(
        'name_stage_task__numb', 'id'
        )
    return render(request, 'task_details.html',
                  {'task': task, 'details': details})


def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'delete_confirmation.html', {'object': task})


def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_details', pk=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def delete_detail(request, pk):
    detail = get_object_or_404(TaskDetail, id=pk)
    task_id = detail.task.id
    if request.method == 'POST':
        detail.delete()
        return redirect('task_details', pk=task_id)
    return render(request, 'delete_confirmation.html', {'object': detail})


def edit_detail(request, pk):
    detail = get_object_or_404(TaskDetail, id=pk)
    if request.method == 'POST':
        form = TaskDetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('task_details', pk=detail.task.id)
    else:
        form = TaskDetailForm(instance=detail)
    return render(request, 'edit_detail.html',
                  {'form': form, 'detail': detail})


def info_by_rate(request):
    info = InfoByRate.objects.all().select_related('name_stage_info')
    context = {
        'info': info,
    }
    return render(request, 'info_by_rate.html', context=context)
