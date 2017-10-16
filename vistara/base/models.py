from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from datetime import datetime

class Departments(models.Model):
	department_name=models.CharField(max_length=500,default='')
	overall_dept_head=models.OneToOneField(User)
	def __str__(self):
		return str(self.department_name)


class Airport(models.Model):
	airport_name=models.CharField(max_length=500,default='')
	overall_airport_head=models.OneToOneField(User)
		
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	first_name=models.CharField(max_length=100,default='')
	last_name=models.CharField(max_length=100,default='')

	airport=models.ForeignKey(Airport,on_delete=models.SET_NULL,null=True)
	department=models.ForeignKey(Departments,on_delete=models.SET_NULL,null=True)
	USER_DES_CHOICES=(('CXO','Chief X officer'),('HOD','Overall Head of Department'),('HODA','Airport Head of Department'),('StaffHO','Staff Head Office'),('StaffA','Staff Airport'))
	designation=models.CharField(max_length=500,default='',choices=USER_DES_CHOICES)


	def __str__(self):
		return str(self.user.username)
	

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class Message(models.Model):
	message=models.TextField()
	sender=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='sender')
	to=models.ManyToManyField(User,null=True,related_name='reciever')
	date=models.DateField(default=datetime.now,blank=True)
	ifactor=models.IntegerField(default=0)
	def __str__(self):
		return str(self.sender)



