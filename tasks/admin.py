from django.contrib import admin

from tasks.models import WorkingDay, PlannedTask

admin.site.register(WorkingDay)
admin.site.register(PlannedTask)
