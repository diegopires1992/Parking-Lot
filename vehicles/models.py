from django.db import models
from levels.models import Level

class Space(models.Model):
    variety = models.CharField(max_length=255)
    level_name = models.CharField(max_length=255)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)

class Vehicles(models.Model):
    license_plate = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255)
    arrived_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField('date_published', null=True)
    amount_paid = models.CharField(max_length=255, null=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)