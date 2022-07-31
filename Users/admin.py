from django.contrib import admin

from Users.models import Course, Instructor, Register, Student

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Register)
