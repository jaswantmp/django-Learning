from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("register/", views.student_register, name="student_register"),
]