from django.shortcuts import render
from .models import Student
from django.forms.models import model_to_dict
# Create your views here.
# def queryxyz(req):
    # data = Student.objects.get(id=1)
    # data = Student.objects.first()
    # data = Student.objects.last()
    # data = Student.objects.get(name = 'satyanam') # get() returned more than one student -- it returned 2
    # data  = model_to_dict
    # return render(req,'demo.html',data)
    # n= data.get('username')
    # e=data.get('email')
    # print(n,e)
    # print(data)
    # return render(req,'demo.html',{'data':data})

# def ctreate_data(req):

     
    #  Student.objects.create(Username='Satyanam',email='satya9494@gmail.com',number=9572949496,phone='9934160423',file='resume/default.pdf',url='https//www.google.com',time='06:50',date='2002-10-15',gender='male',hobby='coding',country='India',message="hey,it's me",password='abcde',hidden='faaa')

    #   Student.objects.create(Username='Shubham',email='satya949496@gmail.com',number=9572949496,phone='9934160423',file='resume/default.pdf',url='https//www.instagram.com',time='06:50',date='2002-10-15',gender='male',hobby='coding',country='India',message="hey,it's me",password='abcde',hidden='hey')  # for single objects
    

    # Student.objects.bulk_create([Student(Username = 'Rahul',email='rahul@gmail.com',phone='9572949496',number=9572949495),Student(Username="Ashu",email='AshuS@gmai.com',phone='500000',number=5200),Student(Username='hey',email='hey@gmail.com',phone='9652020',number=52002155)])
    # Student.objects.get_or_create(Username='Rahul',email='rahul@gmail.com',phone='9572949496',number=9572949495)
    # Student.objects.get_or_create(Username='Ram',email='ram@gmail.com',phone='9572949496',number=9572949495)  # Agar hai data to error aayega nhi hai to bna dega

def multiple_objects(req):
    data=Student.objects.all()
    # print(data)
    # print(data.values())
    # print(data.values_list())
    # print(list(data.values()))
    # return render(req,'demo.html',{"x":data})

    # data= Student.objects.filter(Username="Shubham")
    # print(data)
    # data= Student.objects.order_by('Username') # Ascending
    # print(data)
    # data= Student.objects.order_by('-Username')  # Descending
    # print(data)
    # data= Student.objects.order_by('Username')[0:3] 
    # print(data)
    # data= Student.objects.order_by('Username')[0] # First data
    # print(data)
    # data= Student.objects.order_by('-Username')[0]  # last data
    # print(data)

    data = Student.objects.exclude(Username='hey')  # hey ko hatake baki sb print karega
    print(data)


# def new_change(req):
#     # Student.objects.filter(id=1).update(name='Sattu')
#     # Student.objects.filter(gender='male').update(name='Sattu')
#     data = Student.objects.get(id=5)
#     print(data.Username,data.email)
#     data.Username='heyy'
#     data.save()
    


# def delete_data(req):
    #  Student.objects.filter(id=2).delete() # deleting single objects
    #  Student.objects.filter(gender='male').delete() # deleting multiple objects    