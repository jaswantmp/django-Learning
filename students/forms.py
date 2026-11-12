
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    name = forms.CharField(label="Student Name")
    class Meta:
        model = Student
        fields = ["name", "age", "marks"]

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if not name:
            raise forms.ValidationError("Name cannot be empty.")

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
