from django.urls import path
from . import views

urlpatterns = [
    path("templates/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("templates/mentor/", views.mentor_dashboard, name="mentor_dashboard"),
    path("templates/student/", views.student_dashboard, name="student_dashboard"),
]
