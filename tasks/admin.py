from django.contrib import admin

from tasks.models import WorkingDay, PlannedTask, ExecutedTask, Project


class PlannedTaskInline(admin.TabularInline):
    model = PlannedTask
    extra = 1


class ExecutedTaskInline(admin.TabularInline):
    model = ExecutedTask
    extra = 1


class WorkingDayAdmin(admin.ModelAdmin):
    list_display = ('date', 'entry_time', 'working_time', 'breaks',
                    'planned_tasks', 'executed_tasks')
    model = WorkingDay
    inlines = [PlannedTaskInline, ExecutedTaskInline]

    def planned_tasks(self, obj):
        return obj.planned_tasks.count()

    def executed_tasks(self, obj):
        return obj.executed_tasks.count()


admin.site.register(WorkingDay, WorkingDayAdmin)
admin.site.register(Project)
admin.site.register(PlannedTask)
admin.site.register(ExecutedTask)
