from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(School)
admin.site.register(School_Class)
admin.site.register(Class_Section)