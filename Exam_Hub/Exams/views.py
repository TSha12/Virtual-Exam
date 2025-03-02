from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionPaper, Question
from .forms import QuestionPaperForm, QuestionForm
from django.contrib.auth.decorators import login_required

@login_required
def add_question_paper(request):
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_question_papers')
    else:
        form = QuestionPaperForm()
    return render(request, 'add_question_paper.html', {'form': form})

@login_required
def list_question_papers(request):
    question_papers = QuestionPaper.objects.all()
    return render(request, 'list_question_papers.html', {'question_papers': question_papers})

@login_required
def add_question(request, paper_id):
    question_paper = get_object_or_404(QuestionPaper, id=paper_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_question_paper', paper_id=paper_id)
    else:
        form = QuestionForm(initial={'question_paper': question_paper})
    return render(request, 'add_question.html', {'form': form, 'question_paper': question_paper})

@login_required
def view_question_paper(request, paper_id):
    question_paper = get_object_or_404(QuestionPaper, id=paper_id)
    questions = Question.objects.filter(question_paper=question_paper)
    return render(request, 'view_question_paper.html', {'question_paper': question_paper, 'questions': questions})
