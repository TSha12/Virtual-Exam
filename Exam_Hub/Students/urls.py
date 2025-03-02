from django.contrib import admin
from django.urls import path
#from Home import views


from . import views

urlpatterns = [
    path('login/', views.student_login, name='student-login'),
    path('portal/', views.student_dashboard, name='student-portal'),
    path('exam/<int:exam_id>/', views.take_exam, name='take-exam'),

    path('student-portal/', views.student_portal, name='student_portal'),
 
]
