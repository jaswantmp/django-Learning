from django.urls import path
from . import views

urlpatterns = [
    path("", views.student_home, name="student_home"),
    path("register/", views.student_register, name="student_register"),
    path("update/<int:student_id>/", views.student_update, name="student_update"),
    path("delete/<int:student_id>/", views.student_delete, name="student_delete"),
    path("subject/register/", views.subject_register, name="subject_register"),
    path("reports/", views.student_reports, name="student_reports"),
    path("export/csv/", views.export_students_csv, name="export_students_csv"),
    
]   