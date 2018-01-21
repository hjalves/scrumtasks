from django.db import models


class WorkingDay(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)


class PlannedTask(models.Model):
    working_day = models.ForeignKey(WorkingDay, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
