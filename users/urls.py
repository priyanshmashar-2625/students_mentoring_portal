# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("signin/admin/", views.admin_signin, name="admin_signin"),
    path("signin/mentor/", views.mentor_signin, name="mentor_signin"),
    path("signin/student/", views.student_signin, name="student_signin"),
    path("signup/", views.signup, name='signup'),
    path("forgot-password/", views.forgot_password, name="forgot_password"),

    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/mentor/", views.mentor_dashboard, name="mentor_dashboard"),
    path("dashboard/student/", views.student_dashboard, name="student_dashboard"),
]
