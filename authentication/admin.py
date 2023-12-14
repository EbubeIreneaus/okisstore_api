from django.contrib import admin
from .models import Profile

# Register your models here.


class pAdmin(admin.ModelAdmin):
        list_display = ['name', 'email', '_date']



admin.site.register(Profile, pAdmin)