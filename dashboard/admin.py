from django.contrib import admin

# Register your models here.
from .models import info

class infoAdmin(admin.ModelAdmin):
    field = ['arrival_time', 'departure_time', 'harness_length','gross_weight', 'atmospheric_pressure',
                 'room_temperature', 'fuel_capacity_on_left_wing','fuel_quantity_on_left_wing',
                 'fuel_capacity_on_right_wing', 'fuel_quantity_on_right_wing', 'flight_no']
    list_display = ('msn_number', 'carrier_name','model','arrival_time','departure_time','source',
                    'destination','harness_length','gross_weight', 'atmospheric_pressure','room_temperature',
                    'fuel_capacity_on_left_wing','fuel_quantity_on_left_wing','fuel_capacity_on_right_wing',
                    'fuel_quantity_on_right_wing', 'flight_no', 'Country')
    list_filter = ('model', 'carrier_name', 'Country', 'departure_time', 'arrival_time', 'flight_no', 'msn_number', )

admin.site.register(info, infoAdmin)