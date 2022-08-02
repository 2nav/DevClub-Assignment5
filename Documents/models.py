from django.db import models
from django.utils import timezone

from Users.models import Course


class Doc(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    doc_url = models.URLField(max_length=2043)
    date_added = models.DateTimeField(default=timezone.now)
