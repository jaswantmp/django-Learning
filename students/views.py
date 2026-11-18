import json
import csv
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Student, Subject
from .forms import StudentForm
from django.contrib import messages
from django.db.models import Q
from django.db.models import Avg, Max, Min, Count
from django.db.models import Case, When, Value, CharField
def student_home(request):
    all_students = Student.objects.all()

    # Dashboard statistics from the database
    total_students = all_students.count()
    total_subjects = Subject.objects.count()
    passed_students = all_students.filter(marks__gte=40).count()
    failed_students = all_students.filter(marks__lt=40).count()

    pass_percentage = (
        round((passed_students / total_students) * 100)
        if total_students else 0
    )

    # Search and result filters
    search_query = request.GET.get("q", "").strip()
    result_filter = request.GET.get("result", "")

    students = Student.objects.prefetch_related("subjects").all()

    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |
            Q(subjects__name__icontains=search_query)
        ).distinct()

    if result_filter == "pass":
        students = students.filter(marks__gte=40)
    elif result_filter == "fail":
        students = students.filter(marks__lt=40)

    students = students.order_by("id")

    context = {
        "students": students,
        "total_students": total_students,
        "total_subjects": total_subjects,
        "passed_students": passed_students,
        "failed_students": failed_students,
        "pass_percentage": pass_percentage,
        "search_query": search_query,
        "result_filter": result_filter,
    }

    return render(request, "students/student_home.html", context)


def student_reports(request):
    students = Student.objects.all()

    total_students = students.count()
    passed_students = students.filter(marks__gte=40).count()
    failed_students = students.filter(marks__lt=40).count()

    statistics = students.aggregate(
        average_marks=Avg("marks"),
        highest_marks=Max("marks"),
        lowest_marks=Min("marks"),
    )

    marks_distribution = (
        students.annotate(
            marks_range=Case(
                When(marks__lt=40, then=Value("0–39")),
                When(marks__lt=60, then=Value("40–59")),
                When(marks__lt=80, then=Value("60–79")),
                default=Value("80–100"),
                output_field=CharField(),
            )
        )
        .values("marks_range")
        .annotate(student_count=Count("id"))
    )

    distribution = {
        "0–39": 0,
        "40–59": 0,
        "60–79": 0,
        "80–100": 0,
    }

    for item in marks_distribution:
        distribution[item["marks_range"]] = item["student_count"]


    context = {
        "total_students": total_students,
        "passed_students": passed_students,
        "failed_students": failed_students,
        "pass_percentage": round(
            passed_students * 100 / total_students
        ) if total_students else 0,
        "average_marks": statistics["average_marks"],
        "highest_marks": statistics["highest_marks"],
        "lowest_marks": statistics["lowest_marks"],
        "marks_labels": list(distribution.keys()),
        "marks_counts": list(distribution.values()),
    }

    return render(request, "students/student_reports.html", context)

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
        "students/student_register.html",
        {"form": form}
    ) 

def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        action = request.POST.get("action")

        # Add a new subject
        if action == "add_subject":
            name = request.POST.get("new_subject_name", "").strip()

            if not name:
                messages.error(request, "Subject name cannot be empty.")
            elif len(name) > 100:
                messages.error(
                    request,
                    "Subject name cannot exceed 100 characters."
                )
            elif student.subjects.filter(name__iexact=name).exists():
                messages.error(
                    request,
                    "This student already has this subject."
                )
            else:
                Subject.objects.create(name=name, student=student)
                messages.success(request, "Subject added successfully!")

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

            if not name:
                messages.error(request, "Subject name cannot be empty.")

            elif len(name) > 100:
                messages.error(
                    request,
                    "Subject name cannot exceed 100 characters."
                )

            elif student.subjects.filter(
                name__iexact=name
            ).exclude(id=subject.id).exists():
                messages.error(
                    request,
                    f'You can\'t rename this subject to "{name}" because it already exists for this student.'
                )

            else:
                subject.name = name
                subject.save()
                messages.success(
                    request,
                    "Subject updated successfully!"
                )

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
def export_students_csv(request):
    response = HttpResponse(
        content_type="text/csv"
    )

    response["Content-Disposition"] = (
        'attachment; filename="students_report.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        "ID",
        "Name",
        "Age",
        "Marks",
        "Result",
    ])

    students = Student.objects.all().order_by("id")

    for student in students:
        result = "Pass" if student.marks >= 40 else "Fail"

        writer.writerow([
            student.id,
            student.name,
            student.age,
            student.marks,
            result,
        ])

    return response