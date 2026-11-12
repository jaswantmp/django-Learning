from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
def student_home(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_home.html",
        {"students": students}
    )
def student_register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Student registered successfully!"
            )
            return redirect("student_home")
    else:
        form = StudentForm()

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )   