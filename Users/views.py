from django.shortcuts import render
from django.views.generic import DetailView

from Users.models import Course
from Documents.models import Doc


def is_member(grp, user):
    return user.groups.filter(name=grp).exists()


def home(request):
    if is_member('Student', request.user):
        context = {'courses': request.user.courses.all()}
    elif is_member('Instructor', request.user):
        context = {
            'courses': Course.objects.filter(instructor=request.user.id)
        }
    else:
        context = {'courses': Course.objects.all()}

    return render(request, 'Users/home.html', context)


def CourseDetailView(request, id):
    context = {
        'course': Course.objects.get(id=id),
        'documents': Doc.objects.filter(course=Course.objects.get(id=id))
    }

    return render(request, 'Users/course_detail.html', context)
