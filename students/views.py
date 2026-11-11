from django.shortcuts import render
from .models import Student

def student_home(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_home.html",
        {"students": students}
    )