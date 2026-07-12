from django.db import models


# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(null=True, blank=False)


# models.py -> migration_file -> database_table
# create_class makemigrations migrate
