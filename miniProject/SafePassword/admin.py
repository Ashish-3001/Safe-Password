from django.contrib import admin
from .models import Application
from .models import  Password

# Register your models here.
admin.site.register(Application)
admin.site.register(Password)