from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Departments)
admin.site.register(Airport)
admin.site.register(Message)

# Register your models here.
