from django.db import models

# Create your models here.
class Student(models.Model):
   Username = models.CharField(max_length=100)
   email = models.EmailField()
   number = models.IntegerField()
   phone = models.CharField(max_length=12)
   file = models.FileField(upload_to='uploads/',null=True,blank=True)
   url = models.URLField(null=True)
   time = models.TimeField(null=True)
   date = models.DateTimeField(null=True)
   gender = models.CharField(max_length=15,null=True)
   hobby = models.CharField(max_length=100,null=True)
   country=models.CharField(max_length=50,null=True)
   message = models.TextField(null=True)
   password = models.CharField(max_length=50,null=True)
   hidden = models.CharField(max_length=100,null=True)