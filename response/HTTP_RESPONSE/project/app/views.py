from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    data = '{'',x'':10'',y'':20,z'':30}'
    return HttpResponse(data,content_type='application/json')