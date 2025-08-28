from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html', {"user": request.user})

@login_required
def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html', {"user": request.user})

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html', {"user": request.user})
