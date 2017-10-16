"""vistara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from . import views

urlpatterns = [
   url(r'^',include('django.contrib.auth.urls')),
   url(r'^accounts/profile/$',views.profile,name="profile"),
   ##security/my and security/all and all/all
   url(r'^MessageDetail/create/$', views.MessageCreateView.as_view(), name='create-message-detail'),

	url(r'^msg/(?P<dept>[-\w+]+)/(?P<type>[-\w+]+)$',views.UserProfileListView.as_view(),name="msg-list"),   
]
