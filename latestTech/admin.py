from django.contrib import admin

# Register your models here.

from .models import School, information
admin.site.register(School)
admin.site.register(information)


