from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("register/", views.student_register, name="student_register"),
    path("update/<int:student_id>/", views.student_update, name="student_update"),
    path("delete/<int:student_id>/", views.student_delete, name="student_delete"),

]