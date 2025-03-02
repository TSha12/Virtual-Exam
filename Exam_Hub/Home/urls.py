from django.contrib import admin
from django.urls import path
#from Home import views



from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('index.html', views.home_view, name='home_view'),
    path('about.html', views.about, name='about'),
    path('features.html', views.features, name='features'),
    path('contact.html', views.contact, name='contact'),
    path('teacher-login.html', views.teacher, name='teacher-login'),
    path('teacher-signup.html', views.teacher_sign, name='teacher-signup'),
    path('student-login.html', views.student_login, name='student-login'),
    path('student-signup.html', views.student_sign, name='student-signup'),
]

