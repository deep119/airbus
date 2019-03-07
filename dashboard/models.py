from django.db import models

# Create your models here.


class info(models.Model):
    msn_number = models.CharField(max_length=100, db_index=True)
    carrier_name = models.CharField(max_length=100, null=True, blank=True, db_index=True,
                                    choices=(('Indigo', 'Indigo'), ('JetAirways', 'JetAirways'),
                                             ('AirAsia', 'AirAsia'), ('SpiceJet', 'SpiceJet'),
                                             ('GoAir', 'GoAir')),
                                    default="India")
    model = models.CharField(max_length=100, db_index=True)
    arrival_time = models.DateTimeField(db_index=True)
    departure_time = models.DateTimeField(db_index=True)
    source = models.CharField(max_length=200, verbose_name=('Source Airport'))
    destination = models.CharField(max_length=200, verbose_name=('Destination Airport'))
    harness_length = models.IntegerField(default=0)
    gross_weight = models.FloatField(max_length=200)
    atmospheric_pressure = models.FloatField(max_length=200)
    room_temperature = models.CharField(max_length=200)
    fuel_capacity_on_left_wing = models.FloatField(max_length=200)
    fuel_quantity_on_left_wing = models.FloatField(max_length=200)
    fuel_capacity_on_right_wing = models.FloatField(max_length=200)
    fuel_quantity_on_right_wing = models.FloatField(max_length=200)
    flight_no = models.CharField(max_length=200)
    Country = models.CharField(max_length=100, null=True, blank=True, db_index=True,
                                    choices=(('India', 'India'), ('USA', 'USA')),
                                    default="India")
