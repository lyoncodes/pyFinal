from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Location, Waypoint

class LocationForm(ModelForm):
  class Meta:
    model = Location
    fields = '__all__'

class WaypointForm(ModelForm):
  class Meta:
    model = Waypoint
    fields = '__all__'