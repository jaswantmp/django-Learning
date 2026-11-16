
from django.contrib import admin
from .models import Student, Subject


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "marks")
    search_fields = ("name",)
    list_filter = ("age", "marks")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "student")
    search_fields = ("name",)
    list_filter = ("student",)