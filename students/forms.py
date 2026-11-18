
from django import forms
from .models import Student, Subject



class StudentForm(forms.ModelForm):
    name = forms.CharField(
        label="Student Name",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter student's full name",
            "autocomplete": "name",
        })
    )

    class Meta:
        model = Student
        fields = ["name", "age", "marks"]
        widgets = {
            "age": forms.NumberInput(attrs={
                "placeholder": "Enter age (1–100)",
                "min": 1,
                "max": 100,
            }),
            "marks": forms.NumberInput(attrs={
                "placeholder": "Enter marks (0–100)",
                "min": 0,
                "max": 100,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if not name:
            raise forms.ValidationError(
                "Name cannot be empty."
            )

        return name

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age < 1 or age > 100:
            raise forms.ValidationError(
                "Age must be between 1 and 100."
            )

        return age

    def clean_marks(self):
        marks = self.cleaned_data["marks"]

        if marks < 0 or marks > 100:
            raise forms.ValidationError(
                "Marks must be between 0 and 100."
            )

        return marks

    def clean(self):
        cleaned_data = super().clean()

        age = cleaned_data.get("age")
        marks = cleaned_data.get("marks")

        if age is not None and marks is not None:
            if marks > 90 and age < 18:
                raise forms.ValidationError(
                    "Students under 18 cannot have marks above 90."
                )

        return cleaned_data

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name", "student"]
