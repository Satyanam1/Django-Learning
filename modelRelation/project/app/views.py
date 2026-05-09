from django.shortcuts import render, redirect
from .models import Student, University,Department
from django.contrib import messages

def Home(req):
    students = Student.objects.all()
    departments = Department.objects.all()
    return render(req, 'home.html', {'students': students,'departments':departments})

def student(req):
    if req.method == 'POST':
        n = req.POST.get('student_name')
        e = req.POST.get('email')
        contact = req.POST.get('contact')
        city = req.POST.get('city')

        if Student.objects.filter(email=e).exists():
            messages.error(req, 'Email already exists!')
            return redirect('Home')
        else:
            Student.objects.create(student_name=n, email=e, contact=contact, city=city)
            messages.success(req, 'Student added successfully!')
            return redirect('Home')

    return redirect('Home')


def Add_roll(req):
    if req.method == 'POST':
        rollno = req.POST.get('rollno')
        created_by = req.POST.get('created_by')
        student_id = req.POST.get('student_name')

        if University.objects.filter(rollno=rollno).exists():
            messages.error(req,f"Roll no {rollno} is already taken by another student!")
            return redirect('Home')

        
        if University.objects.filter(student_name_id=student_id).exists():
            messages.error(req, 'Roll No already assigned to this student!')
            return redirect('Home')

        University.objects.create(
            rollno=rollno,
            created_by=created_by,
            student_name_id=student_id  # directly use the id
        )
        messages.success(req, 'Roll No added successfully!')
        return redirect('Home')

    return redirect('Home')

def department(req):
    if req.method == 'POST':
        d_name = req.POST.get('dept_name')
        d_desc = req.POST.get('dept_desc')
        dept_name = Department.objects.filter(dept_name=d_name,dept_desc=d_desc)

        if dept_name:
            messages.error(req,'dept already exists')
            return redirect('Home')
        
        else:
            Department.objects.create(dept_name=d_name,dept_desc=d_desc)
            messages.success(req,'department added successfully!')
            return redirect('Home')
    return render(req,'home.html')
