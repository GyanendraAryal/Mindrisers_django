from django.urls import path
from . import views

# app_name="note"
urlpatterns = [
    path("note",views.note,name="note"),
    path("note/create/",views.create_note,name="create_note"),
    path("note/edit/<int:id>/",views.edit_note,name="edit_note"),
    path("note/delete/<int:id>/",views.delete_note, name="delete_note"),
    path("note/toggle/<int:id>/",views.toggle_note,name="toggle_note")
]
