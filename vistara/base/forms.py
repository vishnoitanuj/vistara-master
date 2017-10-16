from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

from django.db.models import Q

class MessageForm(forms.ModelForm):
	class Meta:
		model=Message
		title="Message"
		fields=['message','to']
		


