from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','last_name']