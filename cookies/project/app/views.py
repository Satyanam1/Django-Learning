from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def set(req):
    if req.method == 'POST':
        
        n = req.POST.get('username')
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(n,e,p)
        
        if(n and e and p):
           response = render(req,'landing.html',{'msg':"cookies has been sent"})
           response.set_cookie('username',n) 
           response.set_cookie('email',e)
           response.set_cookie('password',p)
           return response
        else:
           return render(req,'landing.html',{'msg':'some value are missing'})
       
    return render(req,'landing.html',{'xyz':True})


def get(req):

    if(req.COOKIES.get('username') and req.COOKIES.get('email') and req.COOKIES.get('password')):


    

    # print(req.COOKIES)
      n=req.COOKIES.get('username')
      e=req.COOKIES.get('email')
      p=req.COOKIES.get('password')
    # print(n,e,p)
    

      data = {
        'username':n,'email':e,'password':p}
    
      return render(req,'landing.html',{'data':data})
    else:
       return render(req,'landing.html',{'msg':'cookies are empty'})

def delete(req):
     if(req.COOKIES.get('username') and req.COOKIES.get('email') and req.COOKIES.get('password')):
       response = render(req,'landing.html',{'msg':'Cookies are deleted'})
       response.delete_cookie('username') 
       response.delete_cookie('email') 
       response.delete_cookie('password')
        
       return response

     else:
     
       return render(req,'landing.html',{'msg':'cookies are not found'})
       
    