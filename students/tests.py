from django.test import TestCase
from .models import Student


class StudentModelTest(TestCase):

    def test_student_creation(self):

        student = Student.objects.create(
            name="Jaswant",
            age=19,
            marks=90
        )

        self.assertEqual(student.name, "Jaswant")
        self.assertEqual(student.age, 19)
        self.assertEqual(student.marks, 90)
    def test_student_str(self):

        student = Student.objects.create(
            name="Arun",
            age=20,
            marks=80
        )

        self.assertEqual(str(student), "Arun")
    def test_student_count(self):

        Student.objects.create(
            name="A",
            age=20,
            marks=70
        )

        Student.objects.create(
            name="B",
            age=21,
            marks=80
        )

        self.assertEqual(
            Student.objects.count(),
            2
        )
    def test_filter_students(self):

        Student.objects.create(
            name="A",
            age=20,
            marks=95
        )

        Student.objects.create(
            name="B",
            age=19,
            marks=40
        )

        toppers = Student.objects.filter(
            marks__gt=90
        )

        self.assertEqual(
            toppers.count(),
            1
        )
    
    def test_students_with_failing_marks(self):
        Student.objects.create(
            name="Student A",
            age=19,
            marks=25
        )

        Student.objects.create(
            name="Student B",
            age=20,
            marks=35
        )

        Student.objects.create(
            name="Student C",
            age=21,
            marks=75
        )

        failing_students = Student.objects.filter(
            marks__lt=40
        )

        self.assertEqual(failing_students.count(), 2)

class StudentViewTest(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            name="Arun",
            age=20,
            marks=85
        )

    def test_student_list_page(self):
        response = self.client.get("/students/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Arun")

    def test_student_registration_page(self):
        response = self.client.get("/students/register/")

        self.assertEqual(response.status_code, 200)

    def test_student_edit_page(self):
        response = self.client.get(
            f"/students/update/{self.student.id}/"
        )

        self.assertEqual(response.status_code, 200)

    def test_student_delete_confirmation_page(self):
        response = self.client.get(
            f"/students/delete/{self.student.id}/"
        )

        self.assertEqual(response.status_code, 200)
