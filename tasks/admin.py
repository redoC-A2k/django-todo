from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Task, Tag, TaskStatus


def mark_complete(model, request, queryset):
    queryset.update(status=TaskStatus.COMPLETED)
mark_complete.short_description = "Mark selected tasks as complete"


class TaskAdmin(admin.ModelAdmin):
    fields = [("content", "deadline"), "tags"]

    list_display = ["content", "status", "deadline", "foo"]
    list_editable = ["status"]
    actions = [mark_complete]
    list_filter = ["status","deadline"]
    search_fields = ["content","tags__name"]
    ordering = ["deadline"]

    def get_ordering(self, request: HttpRequest) :
        if request.user.is_superuser:
            return ["status"]
        else :
            return ["deadline"]


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)
