from django.shortcuts import render,redirect, get_object_or_404
from .models import Student, Subject
from .forms import StudentForm
from django.contrib import messages
def student_home(request):
    students = Student.objects.prefetch_related("subjects").all()

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
        action = request.POST.get("action")

        # Add a new subject
        if action == "add_subject":
            name = request.POST.get("new_subject_name", "").strip()

            if name:
                Subject.objects.create(
                    name=name,
                    student=student
                )
                messages.success(request, "Subject added successfully!")
            else:
                messages.error(request, "Subject name cannot be empty.")

            return redirect("student_update", student_id=student.id)

        # Edit an existing subject
        elif action == "update_subject":
            subject_id = request.POST.get("subject_id")
            subject = get_object_or_404(
                Subject, id=subject_id, student=student
            )

            name = request.POST.get(
                f"subject_name_{subject.id}", ""
            ).strip()

            if name:
                subject.name = name
                subject.save()
                messages.success(request, "Subject updated successfully!")
            else:
                messages.error(request, "Subject name cannot be empty.")

            return redirect("student_update", student_id=student.id)

        # Delete an existing subject
        elif action == "delete_subject":
            subject_id = request.POST.get("subject_id")
            subject = get_object_or_404(
                Subject, id=subject_id, student=student
            )
            subject.delete()
            messages.success(request, "Subject deleted successfully!")

            return redirect("student_update", student_id=student.id)

        # Update student details
        elif action == "save_student":
            form = StudentForm(request.POST, instance=student)

            if form.is_valid():
                form.save()
                messages.success(request, "Student updated successfully!")
                return redirect("student_home")

    else:
        form = StudentForm(instance=student)

    subjects = student.subjects.all()

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "student": student,
            "subjects": subjects,
        }
    )


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
def subject_register(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Subject added successfully!")
            return redirect("student_home")
    else:
        form = SubjectForm()

    return render(
        request,
        "students/subject_form.html",
        {"form": form}
    )