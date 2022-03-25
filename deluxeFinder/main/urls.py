from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
  path('', views.route, name="route"),
  path('locations/', views.locations, name="locations"),
  path('newpoint/', views.waypointForm, name="newpoint"),
  path('map/', views.map, name="map"),
]