from django.contrib import admin
from Communication.models import Announcement, Message, Reply

admin.site.register(Announcement)
admin.site.register(Reply)
admin.site.register(Message)