from django.urls import path
from . import views

# app_name="todo"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("task/", views.task, name="task"),
    path("task/create/", views.create, name="create"),
    path("task/edit/<int:id>/", views.edit, name="edit"),
    path("task/delete/<int:id>/",views.delete, name="delete" ),
    path("task/toggle/<int:id>/",views.toggle,name="toggle")
]
