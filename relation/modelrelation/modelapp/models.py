from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.student_name

class Department(models.Model):
    dept_name = models.CharField(max_length=50, unique=True)
    dept_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name
    
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    students = models.ManyToManyField(Student, related_name='books', blank=True)

    def __str__(self):
        return self.book_name    
    
class University(models.Model):
    rollno = models.CharField(max_length=10, unique=True)
    alloted_date = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=50)

    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='university')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='universities')

    def __str__(self):
        return self.rollno
