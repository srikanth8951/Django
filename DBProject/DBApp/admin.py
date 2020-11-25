from django.contrib import admin
from DBApp.models import Student
# Register your models here.
# This file is used to register our modules to admin interface.
class StudentAdmin(admin.ModelAdmin):
    l = ['number', 'name', 'marks']


admin.site.register(Student, StudentAdmin)
