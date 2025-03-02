from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.


def home_view(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            ['toemail@code.com']
        )
        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request, 'contact.html',{})
    
def teacher(request):
    return render(request, 'teacher-login.html')

def teacher_sign(request):
    return render(request, 'teacher-signup.html')

def student_login(request):
    return render(request, 'student-login.html')

def student_sign(request):
    return render(request, 'student-signup.html')