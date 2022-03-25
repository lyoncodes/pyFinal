from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
  latitude = models.FloatField(verbose_name="Latitude", null=True, blank=True)
  longitude = models.FloatField(verbose_name="Longitude", null=True, blank=True)

  def __str__(self):
    return self.name
  
  class Meta:
    db_table = 'location'

class Waypoint(models.Model):
  name = models.CharField(max_length=255)
  userId = models.ForeignKey(User, on_delete= models.CASCADE)
  address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
  
  def __str__(self):
    return self.name
  
  class Meta:
    db_table = 'waypoint'