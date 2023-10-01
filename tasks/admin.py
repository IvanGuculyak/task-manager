from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tasks.models import Position, TaskType, Task, Worker

admin.site.register(Position)
admin.site.register(TaskType)


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ["name", "priority", "task_type",]
    list_filter = ["priority", "task_type",]
    search_fields = ["name", "priority",]


@admin.register(Worker)
class AdminWorker(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("position",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("position", "first_name", "last_name")}),)
