from django.contrib import admin
from .models import Person,Passport,PhoneNumber,Group

# Register your models here.
admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(PhoneNumber)
admin.site.register(Group)