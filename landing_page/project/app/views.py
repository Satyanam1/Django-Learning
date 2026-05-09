from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.views.decorators.cache import never_cache


# Create your views here.
def home(req):
    students = Student.objects.all()
    return render(req,'home.html',{'students':students})

def about(req):
    return render(req,'about.html')

def login_view(req):
    return render(req,'login.html')
   
def register(req):
    return render(req,'register.html')

def contact(req):    
    return render(req,'contact.html')

def contact_data(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        message = req.POST.get('Message')
        print(name,email,message)
        msg = 'Your message has been sent successfully..'
        return render(req,'contact.html',{'msg':msg})
    
def regis(req): 
    if req.method == 'POST':

        email = req.POST.get('email')
        username = req.POST.get('username')
        number = req.POST.get('number')
        phone = req.POST.get('phone')
        url = req.POST.get('website')
        time = req.POST.get('time')
        date = req.POST.get('date')
        gender = req.POST.get('gender')
        hobby = ",".join(req.POST.getlist('hobby'))
        country = req.POST.get('country')
        message = req.POST.get('message')
        password = req.POST.get('password')
        file = req.FILES.get('file')
        picture = req.FILES.get('picture')
        audio = req.FILES.get('audio')
        video = req.FILES.get('video')

        user = Student.objects.filter(email=email)

        if user:
            msg = 'Email already exist..'
            return render(req,'register.html',{'msg':msg})
            # messages.error(req,'email already existt')
        else:   
          Student.objects.create(username=username,email=email,number=number,phone=phone,file=file,url=url,time=time,date=date,gender=gender,hobby=hobby,country=country,message=message,password=password,picture=picture,audio=audio,video=video)
          
          msg1 = "Registration Successful"
          return render(req,'login.html',{'msg1':msg1})
    return render(req,'register.html')    

@never_cache
def login_data(req):
    if req.method == 'POST':
        email=req.POST.get('email')
        password = req.POST.get('password') 
        user = Student.objects.filter(email=email)
        if user:
            user_data = Student.objects.get(email=email)
            save_pass = user_data.password
            if password == save_pass:
                req.session['user_id'] = user_data.id
                req.session['username']= user_data.username
                return redirect('dashboard')  
            else:
                msg="Email and password have not matched"
                return render(req,'login.html',{'msg1':msg,'email':email})
        else:
            msg = 'Email id is not present in databases' 
            return render(req,'register.html',{'msg2':msg}) 


        # if not Student.objects.filter(email=email).exists():
        #     return render(req,'login.html',{'msg':"Email does not exist.."})  
        
        # user = Student.objects.get(email = email)
        # if user.password != password:
        #     return render(req,'login.html',{'msg':'Email and password do not match..'})
        
        # req.session['user_id'] = user.id
        # req.session['username'] = user.username
        # return redirect('dashboard')
    return render(req,'login.html') 


@never_cache
def dashboard(req):
    # user_data = Student.objects.get(id=x)
    # data = {'username':user_data.username,
    #         'email':user_data.email,
    #         'password':user_data.password
    #         }
    # return render(req,'dashboard.html',{'data':data})

    if 'user_id' in req.session:
        user_id = req.session.get('user_id')
        user_data = Student.objects.get(id = user_id)

        data = {
            'username': user_data.username,
            'gender':user_data.gender,
            'email' : user_data.email,
            'number':user_data.number,
            'hobby':user_data.hobby,

        }
        
        return render(req,'home.html',{'data':data}) 
    else:
        return redirect('login')
   

    # if not req.session.get('user_id'):
        # return redirect('login')
    # return render(req,'home.html',{'username':req.session.get('username'),'email':req.session.get('user_id')})    

@never_cache
def logout_user(req):

    req.session.flush()
    return redirect('login')



