from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Course(models.Model):
    code = models.CharField(max_length=6)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField()
    credit = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.code


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entry_number = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course, through="Register")

    def __str__(self) -> str:
        return self.user.username


class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
