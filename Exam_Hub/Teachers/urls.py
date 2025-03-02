from django.contrib import admin
from django.urls import path
#from Home import views


from . import views

urlpatterns = [
    path('login/', views.teacher_login, name='teacher-login'),
    path('portal/', views.teacher_dashboard, name='teacher-portal'),
    path('lesson-list/', views.lesson_list, name='lesson_list'),
    path('add-exam/', views.add_exam, name='add_exam'),
    path('add-lesson/', views.add_lesson, name='add_lesson'),
    path('publish-results/', views.publish_results, name='publish_results'),
    path('profile/', views.view_profile, name='view_profile'),
    path('Question_set/', views.Question_set, name='Question_set'),
]