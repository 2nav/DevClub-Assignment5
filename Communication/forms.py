from email import message
from django import forms
from .models import Message, Reply


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['txt']


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ['txt']