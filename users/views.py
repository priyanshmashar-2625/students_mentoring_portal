from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(username=username, password=password, role=role)
        user.save()
        return redirect('signin')

    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == "admin":
                return redirect('admin_dashboard')
            elif user.role == "mentor":
                return redirect('mentor_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            return render(request, "signin.html", {"error": "Invalid credentials"})
    return render(request, "signin.html")


def forgot_password(request):
    return render(request, 'forgot_password.html')
