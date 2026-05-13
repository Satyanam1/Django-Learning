from django.db import models
import uuid
from django.utils import timezone

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
   