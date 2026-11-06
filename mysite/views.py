from django.shortcuts import render

def home(request):
    context = {
        "name": "Jaswant",
        "completed": False,
        "course": "Django Fundamentals",
        "topics": ["Python", "Django", "Machine Learning"],
    }
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")