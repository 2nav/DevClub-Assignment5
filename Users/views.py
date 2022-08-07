from http.client import HTTPResponse
from django.shortcuts import render
from Users.models import Course, Instructor, Student
from Documents.models import Doc
from Communication.models import Announcement
from django.contrib.auth.decorators import login_required


def is_member(grp, user):
    return user.groups.filter(name=grp).exists()


@login_required
def home(request):
    if is_member('Student', request.user):
        context = {
            'courses': Student.objects.get(user=request.user).courses.all()
        }
    elif is_member('Instructor', request.user):
        context = {
            'courses':
            Course.objects.filter(instructor=Instructor.objects.get(
                user=request.user))
        }
    else:
        context = {'courses': Course.objects.all()}

    return render(request, 'Users/home.html', context)


@login_required
def CourseDetailView(request, id):
    if request.user in Student.objects.filter(courses=Course.objects.get(
            id=id)) or request.user == Course.objects.get(
                id=id).instructor.user:
        context = {
            'course':
            Course.objects.get(id=id),
            'documents':
            Doc.objects.filter(course=Course.objects.get(id=id)),
            'announcements':
            Announcement.objects.filter(course=Course.objects.get(id=id)),
            'flag':
            True
        }

        return render(request, 'Users/course_detail.html', context)
    else:
        return render(request, 'Users/course_detail.html', {
            "flag": False,
        })
