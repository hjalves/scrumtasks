from django.contrib import admin

from tasks.models import WorkingDay, PlannedTask, ExecutedTask, Project

admin.site.register(WorkingDay)
admin.site.register(Project)
admin.site.register(PlannedTask)
admin.site.register(ExecutedTask)
