from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from main.forms import LocationForm

from deluxeFinder.mixins import Directions

# Create your views here.
def locationForm(request):
  form = LocationForm
  if request.method == 'POST':
    form = LocationForm(request.POST)
    if form.is_valid():
      post = form.save(commit = True)
      post.save()
      form = LocationForm()
  else:
    form = LocationForm()
  return render(request, 'main/newRoute.html', {'form': form})

def route(request):
  context = {
    "google_api_key": settings.GOOGLE_API_KEY,
    "base_country": "US"
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