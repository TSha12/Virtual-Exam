from django.contrib import admin
from django.urls import path
#from Home import views

from django.urls import path
from . import views

urlpatterns = [
    path('add-question-paper/', views.add_question_paper, name='add_question_paper'),
    path('question-papers/', views.list_question_papers, name='list_question_papers'),
    path('question-paper/<int:paper_id>/', views.view_question_paper, name='view_question_paper'),
    path('add-question/<int:paper_id>/', views.add_question, name='add_question'),
]
