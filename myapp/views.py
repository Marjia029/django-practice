from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import StudentForm

def home(request):
    return render(request, 'home.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('student_success')  # Redirect after successful submission
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def student_success(request):
    return render(request, 'student_success.html')
