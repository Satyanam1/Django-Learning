from django.shortcuts import render,redirect

from django.contrib import messages

def home(req):
    return render(req,'home.html')


def my_render(req):
    messages.warning(req,"data sent successfully!")
    return render(req,'home.html')

def my_redirect(req):
    messages.info(req,'this is an important information regarding update!!!')
    return redirect('home')