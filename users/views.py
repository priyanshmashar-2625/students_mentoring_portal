from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    role = request.GET.get("role")
    if role == "admin":
        return redirect("admin_signin")
    elif role == "mentor":
        return redirect("mentor_signin")
    elif role == "student":
        return redirect("student_signin")
    return redirect("index")

def forgot_password(request):
    return render(request, 'forgot_password.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def admin_signin(request):
    return render(request, "users/admin_signin.html")

def mentor_signin(request):
    return render(request, "users/mentor_signin.html")

def student_signin(request):
    return render(request, "users/student_signin.html")

def signup(request):
    return render(request, "users/signup.html")