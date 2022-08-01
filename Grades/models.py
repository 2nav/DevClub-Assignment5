from django.db import models
from Users.models import Course, Student


class Grade(models.Model):
    grade = models.FloatField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.student} {self.course} grade'