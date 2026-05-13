from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Register
from django.core.mail import send_mail
import random


def register(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        password = req.POST.get('password')
        city = req.POST.get('city')

      
        if Register.objects.filter(email=email).exists():
            messages.error(req, f'{email} already exists!')
            return redirect('register')
        
        send_mail(
          "Registration",
          "Thank You for registering!!.",
          "satya949496@gmail.com",
          [email],
          fail_silently=False,
)
        Register.objects.create(
            name=name,
            email=email,
            password=password,
            city=city
        )
        messages.success(req, f'Welcome {name}! Registered successfully!')
        return redirect('register')

    return render(req, 'register.html')



def login(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        try:
            user = Register.objects.get(email=email, password=password)
            messages.success(req, f'Welcome back {user.name}!')
            return redirect('login')
        except Register.DoesNotExist:
            messages.error(req, 'Invalid email or password!')
            return redirect('login')

    return render(req, 'login.html')


def forgot_password(req):
    if req.method == 'POST':
        email = req.POST.get('email')

        if not Register.objects.filter(email=email).exists():
            messages.error(req, 'No account found with this email!')
            return redirect('forgot_password')

        otp = random.randint(100000, 999999)

        req.session['otp'] = otp
        req.session['email'] = email

    
        send_mail(
            subject='Password Reset OTP',
            message=f'Your OTP for password reset is: {otp}\n\nDo not share this with anyone!',
            from_email='satya949496@gmail.com',
            recipient_list=[email],
        )

        messages.success(req, f'OTP sent to {email}!')
        return redirect('verify_otp')

    return render(req, 'forgot.html')


def verify_otp(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        entered_otp = req.POST.get('otp')

        # Get OTP from session
        session_otp = req.session.get('otp')
        session_email = req.session.get('email')

        print(f"entered otp : {entered_otp} | session_otp: {session_otp}")
        print(f"entered email: {email} session_email: {session_email}")
        print(f"OTP Type: {type(entered_otp)} | session_otp: {type(session_otp)}")

        # Check email and OTP match
        if email == session_email and int(entered_otp) == session_otp:
            # OTP correct → go to reset password
            return redirect('reset_password')
        else:
            messages.error(req, 'Invalid OTP or Email!')
            return redirect('verify_otp')

    return render(req, 'verify_otp.html')


def reset_password(req):
    if req.method == 'POST':
        new_password = req.POST.get('new_password')
        confirm_password = req.POST.get('confirm_password')

        # Check passwords match
        if new_password != confirm_password:
            messages.error(req, 'Passwords do not match!')
            return redirect('reset_password')

        # Get email from session
        email = req.session.get('email')

        # Update password
        user = Register.objects.get(email=email)
        user.password = new_password
        user.save()

        # Clear session
        del req.session['otp']
        del req.session['email']

        messages.success(req, 'Password reset successfully! Please login.')
        return redirect('login')

    return render(req, 'reset_password.html')
 