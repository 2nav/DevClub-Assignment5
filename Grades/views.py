from django.shortcuts import render
from Users.views import is_member
from .models import Grade
from Users.models import Course


def home(request):
    if is_member('Student', request.user):
        context = {'grades': Grade.objects.filter(student=request.user)}
    elif is_member('Instructor', request.user):
        context = {
            'grades':
            Grade.objects.filter(course__in=Course.objects.filter(
                instructor=request.user.id))
        }
    else:
        context = {'grades': Grade.objects.all()}

    return render(request, 'Grades/home.html', context)