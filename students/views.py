from django.shortcuts import render

def student_home(request):
    students = [
        {"name": "Arun", "marks": 85},
        {"name": "Priya", "marks": 92},
        {"name": "Kumar", "marks": 42},
        {"name": "Divya", "marks": 76}
    ]

    return render(
        request,
        "students/student_home.html",
        {"students": students}
    )