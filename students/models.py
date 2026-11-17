from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()

    def __str__(self):
        return self.name
class Subject(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="subjects"
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "student"],
                name="unique_subject_per_student"
            )
        ]
    def __str__(self):
        return self.name