from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Course(models.Model):
    code = models.CharField(max_length=6)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    description = models.TextField()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entry_number = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course, through="Register")


class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
