from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
from itertools import chain
from Communication.models import Message
from .forms import MessageForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    context = {'users': User.objects.all()}
    return render(request, 'Communication/home.html', context)


def MessageDetailView(request, id):
    p1 = User.objects.filter(id=id)
    p2 = request.user
    message_1 = Message.objects.filter(reciever__in=p1, sender=p2)
    message_2 = Message.objects.filter(reciever=p2, sender__in=p1)
    messages = sorted(list(chain(message_1, message_2)),
                      key=lambda instance: instance.date_added)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.instance.sender = request.user
            form.instance.reciever = User.objects.get(id=id)
            form.save()
            return HttpResponseRedirect(reverse('message-detail', args=[id]))

    context = {"messages": messages, "form": form}
    return render(request, "Communication/message_detail.html", context)
