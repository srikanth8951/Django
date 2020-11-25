from django.db import models

# Create your models here.
"""
Django provides a builtin database called sqlite3.
That is configured inside setting.py. 
"""
class Student(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.FloatField()
    # In order to create a class we must inherit the subclass Model(gjango.db.models.Model)
    def __str__(self):
        return self.name
    