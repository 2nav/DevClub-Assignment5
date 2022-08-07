from django.shortcuts import render
from Users.models import Course, Student
from Documents.models import Doc
from Communication.models import Announcement


def is_member(grp, user):
    return user.groups.filter(name=grp).exists()


def home(request):
    if is_member('Student', request.user):
        context = {
            'courses': Student.objects.get(user=request.user).courses.all()
        }
    elif is_member('Instructor', request.user):
        context = {
            'courses': Course.objects.filter(instructor=request.user.id)
        }
    else:
        context = {'courses': Course.objects.all()}

    return render(request, 'Users/home.html', context)


def CourseDetailView(request, id):
    context = {
        'course':
        Course.objects.get(id=id),
        'documents':
        Doc.objects.filter(course=Course.objects.get(id=id)),
        'announcements':
        Announcement.objects.filter(course=Course.objects.get(id=id))
    }

    return render(request, 'Users/course_detail.html', context)
