from django.shortcuts import render, redirect
from .forms import  StudentSignupForm
from .models import Student,Organization


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            pass1 = request.POST.get('password')
            pass2 = request.POST.get('password2')
            if pass1 == pass2:
                form.save()
                return redirect('home')
            else:
                form.add_error(None, "Passwords don't match")
            # Redirect to success page
    else:
        form = StudentSignupForm()
    return render(request, 'student_signup.html', {'form': form})


def students_login(request):
    if request.method == 'POST':
        enrolment_no = request.POST.get('enrolment_no')
        password = request.POST.get('password')

        student = Student.objects.get(enrolment_no=enrolment_no)
        user = student.name
        if student.password == password:
            return redirect('suser_home')
        
    return render(request, 'students_login.html')

def organisation_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        organization = Organization.objects.get(email=email)
        if organization.password == password:
            return redirect('user_home')
        
    return render(request, 'admin.html')
