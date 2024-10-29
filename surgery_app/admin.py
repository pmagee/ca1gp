from django.contrib import admin
from .models import Surgery, Patient, Doctor

# Register your models here.
admin.site.register(Surgery)
admin.site.register(Patient)
admin.site.register(Doctor)
