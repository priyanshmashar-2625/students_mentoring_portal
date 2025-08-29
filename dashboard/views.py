from django.shortcuts import render

def admin_dashboard(request):
    return render(request, "dashboard/admin_dashboard.html")

def mentor_dashboard(request):
    return render(request, "dashboard/mentor_dashboard.html")

def student_dashboard(request):
    return render(request, "dashboard/student_dashboard.html")
