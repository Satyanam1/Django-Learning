from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Passport(models.Model):
    passport_no = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    person = models.OneToOneField(Person, on_delete=models.CASCADE,related_name='passport')

    def __str__(self):
        return self.passport_no
class PhoneNumber(models.Model):
    number = models.CharField(max_length=15)
    number_type = models.CharField(max_length=20)
    person = models.ForeignKey(Person,on_delete=models.CASCADE,related_name='phone_numbers') 

    def __str__(self):
        return self.number   

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    members = models.ManyToManyField(Person,related_name='groups',blank=True)
    def __str__(self):
        return self.group_name