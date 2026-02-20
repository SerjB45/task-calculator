from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    is_manager = models.BooleanField(default=False, verbose_name='Менеджер')

    def __str__(self):
        return self.username


class TypeStages(models.Model):
    numb = models.IntegerField(verbose_name='Номер стадии')
    name_stage = models.CharField(max_length=50,
                                  verbose_name='Наименование стадии')

    def __str__(self):
        return self.name_stage


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название задачи')
    total_time = models.FloatField(default=0, verbose_name='Итоговое время')
    customer = models.CharField(max_length=100, verbose_name='Заказчик',
                                blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    created_by = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Создатель')

    def __str__(self):
        return self.title


class TaskDetail(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name='details',
                             verbose_name='Связанная задача')
    stage = models.CharField(max_length=255, verbose_name='Этап разработки')
    time_spent = models.FloatField(
        verbose_name='Время, потраченное на этот этап')
    name_stage_task = models.ForeignKey(TypeStages,
                                        on_delete=models.DO_NOTHING,
                                        related_name='task_details',
                                        verbose_name='Стадия',
                                        default=1)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата обновления')

    def save(self, *args, **kwargs):
        old_time = getattr(self, '_old_time', None)

        if not old_time:
            try:
                current_instance = TaskDetail.objects.get(id=self.id)
                old_time = current_instance.time_spent
            except TaskDetail.DoesNotExist:
                old_time = 0

        self.task.total_time -= old_time
        self.task.total_time += self.time_spent
        self.task.save()
        super().save(*args, **kwargs)
        self._old_time = self.time_spent

    def delete(self, *args, **kwargs):
        self.task.total_time -= self.time_spent
        self.task.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.stage}: {self.time_spent}"


class InfoByRate(models.Model):
    stage = models.TextField(verbose_name='Этап разработки')
    rate = models.TextField(verbose_name='Оценка')
    note = models.TextField(verbose_name='Примечание')
    name_stage_info = models.ForeignKey(TypeStages,
                                        on_delete=models.DO_NOTHING,
                                        related_name='info_by_rate',
                                        verbose_name='Стадия')

    def __str__(self):
        return f"{self.stage}: {self.rate}"
