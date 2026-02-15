from django.forms import ModelForm

from .models import Task, TaskDetail


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class TaskDetailForm(ModelForm):
    class Meta:
        model = TaskDetail
        exclude = ('task', )
