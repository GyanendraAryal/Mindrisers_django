from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "status")
    search_fields = ("title", "id")
    list_filter = ("status",)
    list_per_page = 2


# admin.site.register(TodoList, TodoListAdmin) either this or use decorators.
