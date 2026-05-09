from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Department, Book, University

def home(req):
    students = Student.objects.all()
    departments = Department.objects.all()
    books = Book.objects.all()
    return render(req, 'home.html', {
        'students': students,
        'departments': departments,
        'books': books
    })


def add_student(req):
    if req.method == 'POST':
        name = req.POST.get('student_name')
        email = req.POST.get('email')
        contact = req.POST.get('contact')
        city = req.POST.get('city')

        # Check: email already exists
        if Student.objects.filter(email=email).exists():
            messages.error(req, f'{email} already exists!')
            return redirect('home')

        Student.objects.create(student_name=name, email=email, contact=contact, city=city)
        messages.success(req, f'{name} added successfully!')
        return redirect('home')

    return redirect('home')


def add_department(req):
    if req.method == 'POST':
        dept_name = req.POST.get('dept_name')
        dept_desc = req.POST.get('dept_desc')

        # Check: department already exists
        if Department.objects.filter(dept_name=dept_name).exists():
            messages.error(req, f'{dept_name} already exists!')
            return redirect('home')

        Department.objects.create(dept_name=dept_name, dept_desc=dept_desc)
        messages.success(req, f'{dept_name} added successfully!')
        return redirect('home')

    return redirect('home')


def add_book(req):
    if req.method == 'POST':
        book_name = req.POST.get('book_name')
        author = req.POST.get('author')

        # Check: book already exists
        if Book.objects.filter(book_name=book_name).exists():
            messages.error(req, f'{book_name} already exists!')
            return redirect('home')

        Book.objects.create(book_name=book_name, author=author)
        messages.success(req, f'{book_name} added successfully!')
        return redirect('home')

    return redirect('home')


def assign_book(req):
    if req.method == 'POST':
        student_id = req.POST.get('student')
        book_id = req.POST.get('book')

        student = Student.objects.get(id=student_id)
        book = Book.objects.get(id=book_id)

        # Check: student already has this book
        if book.students.filter(id=student_id).exists():
            messages.error(req, f'{student.student_name} already has {book.book_name}!')
            return redirect('home')

        # ManyToMany — use .add()
        book.students.add(student)
        messages.success(req, f'{book.book_name} assigned to {student.student_name} successfully!')
        return redirect('home')

    return redirect('home')


def add_rollno(req):
    if req.method == 'POST':
        rollno = req.POST.get('rollno')
        created_by = req.POST.get('created_by')
        student_id = req.POST.get('student')
        dept_id = req.POST.get('department')

        # Check: roll no already exists
        if University.objects.filter(rollno=rollno).exists():
            messages.error(req, f'Roll No {rollno} is already taken!')
            return redirect('home')

        # Check: student already has a roll no
        if University.objects.filter(student_id=student_id).exists():
            messages.error(req, 'This student already has a roll number!')
            return redirect('home')

        University.objects.create(
            rollno=rollno,
            created_by=created_by,
            student_id=student_id,
            department_id=dept_id
        )
        messages.success(req, f'Roll No {rollno} added successfully!')
        return redirect('home')

    return redirect('home')