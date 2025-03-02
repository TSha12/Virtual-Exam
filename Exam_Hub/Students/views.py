from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib import messages
from Teachers.models import Lesson, Exam, Result
from django.contrib.auth.decorators import login_required
from Exams.models import QuestionPaper, Question
from .forms import ExamAttemptForm
from django.contrib.auth.models import User
from django.utils.timezone import now

def student_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)  # Assuming email is used as username

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("student-portal")  # Redirect to student's portal
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, "student-login.html")

def student_dashboard(request):
   return render(request, "student-portal.html")


@login_required
def student_portal(request):
    student = request.user  # Assuming student is logged in
    lessons = Lesson.objects.all()
    exams = Exam.objects.filter(date__lte=now())  # Show only published exams
    results = Result.objects.filter(student=student, published=True)  # Show only published results

    return render(request, 'student_portal.html', {
        'student': student,
        'lessons': lessons,
        'exams': exams,
        'results': results
    })


@login_required
def take_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    question_paper = get_object_or_404(QuestionPaper, title=exam.name)
    questions = Question.objects.filter(question_paper=question_paper)
    
    if request.method == "POST":
        form = ExamAttemptForm(request.POST, questions=questions)
        if form.is_valid():
            score = form.calculate_score()
            result = Result(student=request.user, exam=exam, score=score, published=True)
            result.save()
            return redirect("student-portal")
    else:
        form = ExamAttemptForm(questions=questions)
    
    return render(request, 'take_exam.html', {'exam': exam, 'questions': questions, 'form': form})
