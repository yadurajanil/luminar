from django.contrib import admin

from schoolapp.models import Student,School

# Register your models here.
admin.site.register(School)
admin.site.register(Student)