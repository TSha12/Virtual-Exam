from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Exam, Lesson, Teacher, Result, TeacherProfile
from django.contrib.auth.decorators import login_required
from .forms import LessonForm, ExamForm, ResultForm
from django.contrib.auth.models import User

def teacher_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if not user.is_staff:  # Ensure only staff can log in
                messages.error(request, "You are not authorized to access this portal.")
                return redirect("teacher-login")

            teacher_profile = TeacherProfile.objects.get(user=user)

            if not teacher_profile.is_approved:  # Check if the teacher is approved
                messages.error(request, "Your account is pending approval. Please contact the admin.")
                return redirect("teacher-login")

            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("teacher-portal")  # Redirect to teacher portal
            else:
                messages.error(request, "Invalid credentials. Please try again.")

        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
        except TeacherProfile.DoesNotExist:
            messages.error(request, "Teacher profile not found. Please contact admin.")

    return render(request, "teacher-login.html")


def teacher_dashboard(request):
   return render(request, "teacher-portal.html")

@login_required(login_url='/Teachers/login/')
def add_lesson(request):
    if request.method == "POST":
        form = LessonForm(request.POST, teacher=request.user)  # Pass teacher
        if form.is_valid():
            form.save()
            return redirect('lesson_list')  # Redirect to lessons page
    else:
        form = LessonForm(teacher=request.user)  # Pass teacher

    return render(request, 'add-lesson.html', {'form': form})

@login_required(login_url='/Teachers/login/')
def add_exam(request):

    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.teacher = request.user
            exam.save()
            return redirect('Question_set')
    else:
        form = ExamForm()
    return render(request, 'add-exam.html', {'form': form})

@login_required(login_url='/Teachers/login/')
def publish_results(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.published = True  # Ensure the result is published
            result.save()
            return redirect('publish_results')  # Redirect to avoid multiple form submissions
    else:
        form = ResultForm()

    results = Result.objects.all()  # Fetch all results to display

    return render(request, 'publish-results.html', {'form': form, 'results': results})


def view_profile(request):
    return render(request, 'teacher-profile.html', {'teacher': request.user})

def Question_set(request):
    return render(request,'add_question_paper.html')

@login_required
def lesson_list(request):
    lessons = Lesson.objects.filter(teacher=request.user)  # Fetch only teacher's lessons
    return render(request, 'lesson_list.html', {'lessons': lessons})
