from django.contrib import admin
from .models import dj_srk

# Register your models here.
@admin.register(dj_srk)
class admin(admin.ModelAdmin):
    display_list = ['name', 'age']