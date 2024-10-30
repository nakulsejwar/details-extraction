from django.contrib import admin
from .models import Aadhar

@admin.register(Aadhar)
class AadharAdmin(admin.ModelAdmin):
    list_display = ('aadhar_number',)  # Display only Aadhar number in admin
    search_fields = ('aadhar_number',)  # Enable search by Aadhar number
