from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Labels
from django.utils.translation import gettext


class Tasks(models.Model):
    name = models.CharField(gettext('name'),
                            max_length=120, unique=True,)
    description = models.TextField(
        gettext('Description'), blank=True,)
    created_at = models.DateTimeField(auto_now_add=True,)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author',)
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, related_name='status',
        verbose_name=gettext('status'),)
    executor = models.ForeignKey(
        User, blank=True, on_delete=models.PROTECT,
        related_name='executor', verbose_name=gettext('executor'),)
    labels = models.ManyToManyField(
        Labels, blank=True, related_name='labels', through='LabelTask',
        verbose_name=gettext('labels'),)

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    labels = models.ForeignKey(Labels, on_delete=models.RESTRICT)
