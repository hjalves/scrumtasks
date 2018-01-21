from django.db import models
from django.utils.timezone import timedelta


class WorkingDay(models.Model):
    date = models.DateField()
    # This needs to be datetime in order to preserve timezone
    entry = models.DateTimeField(blank=True, null=True)
    working_time = models.DurationField(blank=True, null=True)
    breaks = models.DurationField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)

    @property
    def entry_time(self):
        if self.entry is not None:
            return self.entry.time()

    @property
    def exit(self):
        if self.entry is not None and self.working_time is not None:
            # noinspection PyTypeChecker
            return (self.entry + self.working_time +
                    (self.breaks or timedelta()))

    @property
    def exit_time(self):
        if self.exit is not None:
            return self.exit.time()


class Project(models.Model):
    name = models.CharField(max_length=100)
    redmine = models.CharField(max_length=100, blank=True)
    gitlab = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PlannedTask(models.Model):
    working_day = models.ForeignKey(WorkingDay, on_delete=models.CASCADE,
                                    related_name='planned_tasks')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                null=True, blank=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class ExecutedTask(models.Model):
    DONE = 'D'
    DOING = 'O'
    TASK_STATE_CHOICES = (
        (DONE, 'Done'),
        (DOING, 'Doing')
    )

    working_day = models.ForeignKey(WorkingDay, on_delete=models.CASCADE,
                                    related_name='executed_tasks')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                null=True, blank=True)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=1, choices=TASK_STATE_CHOICES,
                             default=DONE)
    time_spent = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
