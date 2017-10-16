from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import *
from django import forms
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Count
from datetime import datetime
import uclassify


# Create your views here.


@login_required
def profile(request):
	msg_list=Message.objects.filter(to=request.user)
	sent_msg_list=Message.objects.filter(sender=request.user)
	context={'msg_list':msg_list,'sent_msg_list':sent_msg_list }
	return render(request,'registration/profile.html',context)


class MessageCreateView(LoginRequiredMixin,generic.CreateView):
	model=Message
	form_class= MessageForm
	template_name='base/detailcreate_form.html'
	def form_valid(self,form,**kwargs):
		message=form.save(commit=False)
		message.sender=User.objects.get(username=self.request.user)
		message_content=(message.message)
		a = uclassify()
		a.setWriteApiKey('WIPVAtuJ5Gq3')
		a.setReadApiKey('JiP2L5HBORVM')
		#a.create("GorB") #Creates Classifier named "ManorWoman"
		#a.addClass(["g","b"],"gorb") #Adds two class named "man" and "woman" to the classifier "ManorWoman"
		a.train(["Bomb Bad","Late Urgent","Delay Dead"],"b","GorB")
		a.train(["Good Happy"],"g","GorB")        
		d = a.classify([message_content],"GorB")
		ls=d[0][2]
		i=ls[0][1]
		message.ifactor=float(i)*10
		message.save()
		return redirect('/')

class UserProfileListView(generic.ListView):
	model=UserProfile
	def get_queryset(self,**kwargs):
		queryset=UserProfile.objects.all()
		if self.kwargs['dept'] == 'cxo':
			queryset=UserProfile.objects.filter(designation__exact=self.kwargs['dept'])
		elif self.kwargs['dept'] == "all":
			queryset=UserProfile.objects.all()
		elif self.kwargs['type'] == "all":
			queryset=UserProfile.objects.filter(designation__exact=self.kwargs['dept'])
		elif self.kwargs['type'] == "my":
			queryset=UserProfile.objects.filter(designation__exact=self.kwargs['dept'] , airport__exact=self.airport)
		return queryset



		

	'''
	# def get_context_data(self, **kwargs):
	# 	context = super(MessageListView, self).get_context_data(**kwargs)
	# 	context['kwrg']=self.kwargs
	# 	ls=list(self.kwargs)
	# 	context['kwls']=ls
	# 	return context'''

