from django.db import models
from django.utils import timezone
from Users.models import Course
from django.contrib.auth.models import User


class Announcement(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    txt = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)


class Message(models.Model):
    txt = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(User,
                               related_name="sender",
                               on_delete=models.CASCADE)
    reciever = models.ForeignKey(User,
                                 related_name="reciever",
                                 on_delete=models.CASCADE)
