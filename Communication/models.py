from django.db import models
from django.utils import timezone
from Users.models import Course


class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    txt = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)