from django.forms import ModelForm

from .models import Task, TaskDetail, InfoByRate


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'customer']


class TaskDetailForm(ModelForm):
    class Meta:
        model = TaskDetail
        exclude = ('task', )


class InfoByRateForm(ModelForm):
    class Meta:
        model = InfoByRate
        fields = ['stage', 'name_stage_info', 'rate', 'note']
