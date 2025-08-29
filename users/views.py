from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')
