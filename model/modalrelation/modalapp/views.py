from django.shortcuts import render,redirect
from .models import Person,Passport,PhoneNumber,Group

from django.contrib import messages

# Create your views here.
def home(req):
    persons = Person.objects.all()
    groups = Group.objects.all()
    return render(req,'home.html',{'persons':persons,'groups':groups})

def add_person(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        city = req.POST.get('city')

        Person.objects.create(name=name,age=age,city=city)
        messages.success(req,'person added successfully')
        return redirect('home')
    return redirect('home')

def add_passport(req):
    if req.method == 'POST':
        passport_no = req.POST.get('passport_no')
        country = req.POST.get('country')
        person_id = req.POST.get('person')
        if Passport.objects.filter(passport_no=passport_no).exists():
            messages.error(req,f'passport{passport_no} already exists')
            return redirect('home')
        
        if Passport.objects.filter(person_id=person_id).exists():
            messages.error(req, 'This person already has a passport!')
            return redirect('home')

        Passport.objects.create(passport_no=passport_no,country=country,person_id=person_id)
        return redirect('home')
    return redirect('home')
def add_phone(req):
    if req.method == 'POST':
        number = req.POST.get('number')
        number_type = req.POST.get('number_type')
        person_id = req.POST.get('person')

        if PhoneNumber.objects.filter(number=number).exists():
            messages.error(req,f'phone {number} already exists')
            return redirect('home')
        PhoneNumber.objects.create(number=number,number_type=number_type,person_id=person_id)
        messages.success(req,'Phone Number added successfully!')
        return redirect('home')
    return redirect('home')

def add_group(req):
    if req.method == 'POST':
        group_name = req.POST.get('group_name')
        if Group.objects.filter(group_name=group_name).exists():
            messages.error(req,f'{group_name} group already exists!')
            return redirect('home')
        Group.objects.create(group_name=group_name)
        messages.success(req,f'{group_name} group created successfullY!')
        return redirect(req,'home')
    return redirect('home')

def join_group(req):
    if req.method == 'POST':
        person_id = req.POST.get('person_id')
        group_id = req.POST.get('group')
        person = Person.objects.get(id = person_id)
        group = Group.objects.get(id=group_id)  

        if group.members.filter(id=person_id).exists():
            messages.error(req,f'{person.name} is already in {group.group_name}')
            return redirect('home')
        group.members.add(person)
        messages.success(req,f'{person.name} added to {group.group_name} successfully!')
        return redirect('home')
    return redirect('home')