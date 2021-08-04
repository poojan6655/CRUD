"""TechProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home-admin/', views.home_admin, name='home-admin'),
    path('home-emp/', views.home_emp, name='home-emp'),
    path('login/', views.login_fun, name='login-page'),
    path('register/', views.register_fun, name='register-page'),
    path('logout/', views.logout_fun, name='logout-page'),
    path('Create-meeting/', views.create_meeting_fun, name='create-meeting-page'),
    path('meeting-done/', views.meeting_done_fun, name='meeting-done-page'),

    path('edit/<int:pk>', views.edit_fun, name='edit-page'),
    path('edit-emp/<int:pk>', views.edit_emp_fun, name='edit-emp-page'),

    path('delete/<int:pk>', views.delete_fun, name='delete-page'),
    path('delete-emp/<int:pk>', views.delete_emp_fun, name='delete-emp-page'),

    path('update/', views.update_fun, name='update-page'),
    path('update-emp/', views.update_emp_fun, name='update-emp-page'),
]
