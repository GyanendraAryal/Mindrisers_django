from django.db import models

# models.py -> migration_file -> database_table
# create_class makemigrations migrate


# class TodoList(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     status =models.BooleanField(default=False)
#     date= models.DateField()


# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False, blank=True)
    # date = models.DateField()

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.title
