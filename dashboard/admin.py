from django.contrib import admin

# Register your models here.
from .models import info

class infoAdmin(admin.ModelAdmin):
    fields = ['source_arrival_time', 'departure_time']

admin.site.register(info, infoAdmin)