from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def set(req):
    if req.method == 'POST':
        n=req.POST.get('username')
        e=req.POST.get('email')
        p=req.POST.get('password')

        req.session['username'] = n
        req.session['email'] = e
        req.session['password'] = p

        return render(req,'landing.html',{'msg':"Data set successfully"})

    return render(req,'landing.html',{'set':True})

def get(req):
    if 'username' in req.session and 'email' in req.session and 'password' in req.session:
        n = req.session.get('username')
        e = req.session.get('email')
        p = req.session.get('password')

        data = {'username':n,'email':e,'password':p}

        return render(req,'landing.html',{'msg':'Data Get Successfully','data':data})
    else:       
      return render(req,'landing.html',{'msg':'Data denied'})

def delete(req):
    if 'username' in req.session and 'email' in req.session and 'password' in req.session:

        del req.session['username']
        del req.session['email']
        del req.session['password']

        return render(req,'landing.html',{'msg':"Data Deleted"})
    else:
        return render(req,'landing.html',{'msg':'No Data available'})
