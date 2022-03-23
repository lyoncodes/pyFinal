from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
  town = models.CharField(verbose_name="Town/City", max_length=100, null=True, blank=True)
  county = models.CharField(verbose_name="County", max_length=100, null=True, blank=True)
  post_code = models.CharField(verbose_name="Post Code", max_length=8, null=True, blank=True)
  country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)
  longitude = models.CharField(verbose_name="Longitude", max_length=50, null=True, blank=True)
  latitude = models.CharField(verbose_name="Latitude", max_length=50, null=True, blank=True)

  def __str__(self):
    return self.name
  
  class Meta:
    db_table = 'locations'