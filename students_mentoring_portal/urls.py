from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from dashboard import views as dash_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index, name='index'),                 # Landing Page
    path('signin/', user_views.signin, name='signin'),
    path('signup/', user_views.signup, name='signup'),
    path('forgot-password/', user_views.forgot_password, name='forgot_password'),

    path('dashboard/admin/', dash_views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/mentor/', dash_views.mentor_dashboard, name='mentor_dashboard'),
    path('dashboard/student/', dash_views.student_dashboard, name='student_dashboard'),
]
