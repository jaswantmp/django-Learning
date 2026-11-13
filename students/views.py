from django.shortcuts import render,redirect, get_object_or_404
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

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect("student_home")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/student_form.html", {"form": form})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect("student_home")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )
