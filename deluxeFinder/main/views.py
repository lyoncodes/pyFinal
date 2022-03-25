from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.conf import settings
from main.forms import LocationForm, Location, WaypointForm, Waypoint
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from deluxeFinder.mixins import Directions

# Create your views here.
# @login_required
# def locationForm(request):
#   locations = Location.objects.all()
#   form = LocationForm
#   if request.method == 'POST':
#     form = LocationForm(request.POST)
#     if form.is_valid():
#       post = form.save(commit = True)
#       post.save()
#       form = LocationForm()
#   else:
#     form = LocationForm()
#   return render(request, 'main/locations.html', {'form': form, 'locations': locations})

@login_required
def waypointForm(request):
  form = WaypointForm
  if request.method == 'POST':
    form = WaypointForm(request.POST)
    if form.is_valid():
      post = form.save(commit = True)
      post.save()
      form = WaypointForm()
  else:
    form = WaypointForm()
  return render(request, 'main/newpoint.html', {'form': form})

@login_required
def locations(request):
  locations = Location.objects.all()
  return render(request, 'main/locations.html', {'locations': locations})

def route(request):
  waypoints = Waypoint.objects.filter(userId = request.user.id)
  context = {
    "google_api_key": settings.GOOGLE_API_KEY,
    "base_country": "US",
    "waypoints": waypoints
  }
  return render(request, 'main/route.html', context)

def map(request):
  lat_a = request.GET.get("lat_a", None)
  long_a = request.GET.get("long_a", None)
  lat_b = request.GET.get("lat_b", None)
  long_b = request.GET.get("long_b", None)

  if lat_a and lat_b:
    directions = Directions(
      lat_a = lat_a,
			long_a =long_a,
			lat_b = lat_b,
			long_b = long_b
    )
  else:
    return redirect(reverse('main:route'))
  
  context = {
	"google_api_key": settings.GOOGLE_API_KEY,
	"base_country": settings.BASE_COUNTRY,
	"lat_a": lat_a,
	"long_a": long_a,
	"lat_b": lat_b,
	"long_b": long_b,
	"origin": f'{lat_a}, {long_a}',
	"destination": f'{lat_b}, {long_b}',
	"directions": directions,
  }
  return render(request, 'main/map.html', context)