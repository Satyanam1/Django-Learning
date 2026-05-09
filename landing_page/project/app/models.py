from django.db import models


# Create your models here.
class Student(models.Model):
   
   username = models.CharField(max_length=100)
   email = models.EmailField()
   number = models.IntegerField()
   phone = models.CharField(max_length=12)
   url = models.URLField()
   time = models.TimeField()
   date = models.DateTimeField()
   gender = models.CharField(max_length=15)
   hobby = models.CharField(max_length=100)
   country=models.CharField(max_length=50)
   message = models.TextField()
   password = models.CharField(max_length=50)
   file = models.FileField(upload_to='uploads/')
   picture = models.ImageField(upload_to='images/',blank=True,null=True)
   audio = models.FileField(upload_to='audio/',blank=True,null=True)
   video = models.FileField(upload_to='video/',null=True,blank=True)
  
   
   

   # def __str__(self):
   #    return self.Username+' '+self.email + str(self.number)  
    
    
