from django.contrib import admin

from .models import Student,Department,University,Book

# Register your models here.
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(University)
admin.site.register(Book)