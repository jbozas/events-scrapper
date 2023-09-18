from django.contrib import admin
from .models import Cinema


admin.site.register(Cinema,  admin.ModelAdmin)