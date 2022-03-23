from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Location

class LocationForm(ModelForm):
  class Meta:
    model = Location
    fields = '__all__'