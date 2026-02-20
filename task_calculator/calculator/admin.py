from django.contrib import admin
from .models import InfoByRate, Task, TaskDetail, TypeStages, MyUser

admin.site.register(InfoByRate)
admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(TypeStages)
admin.site.register(MyUser)
