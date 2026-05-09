from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_name} ({self.email})"

class Department(models.Model):
    dept_name = models.CharField(max_length=50,unique=True)
    dept_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name


class University(models.Model):
    rollno = models.CharField(max_length=10)
    alloted_date = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=50)
    student_name = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='xyz')   
    student_dept = models.ForeignKey(Department,on_delete=models.CASCADE) 

    def __str__(self):
        return self.rollno 

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    sub_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    rollno = models.ManyToManyField(University)

    def __str__(self):
        return self.book_name   