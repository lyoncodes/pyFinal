from django.conf import settings
import requests
from humanfriendly import format_timespan

def Directions(*args, **kwargs):
  '''
  Direction engine
  '''
  
  '''
  get and assign params
  '''
  lat_a = kwargs.get("lat_a")
  long_a = kwargs.get("long_a")

  lat_b = kwargs.get("lat_b")
  long_b = kwargs.get("long_b")
  
  origin = f'{lat_a}, {long_a}'
  destination = f'{lat_b},{long_b}'

  '''
  req/res handling
  '''
  result = requests.get(
    'https://maps.googleapis.com/maps/api/directions/json?',
    params = {
      'origin': origin,
      'destination': destination,
      'key': settings.GOOGLE_API_KEY
    }
  )

  directions = result.json()
  # print(directions)
  if directions["status"] == "OK":
    routes = directions["routes"][0]["legs"]

    distance = 0
    duration = 0
    route_list = [] # list for storing directions
    # print(routes)
    for route in range(len(routes)):
      # print(routes[route])
      distance += int(routes[route]["distance"]["value"])
      duration += int(routes[route]["duration"]["value"])

      '''
      populate route list
      '''

      route_step = {
        'origin': routes[route]["start_address"],
        'destination': routes[route]["end_address"],
        'distance': routes[route]["distance"]["text"],
        'duration': routes[route]["duration"]["text"], 

        'steps': [
          [
            s["distance"]["text"],
            s["duration"]["text"],
            s["html_instructions"],
          ]
          for s in routes[route]["steps"]
        ]
      }
      route_list.append(route_step)

  return {
    "origin": origin,
    "destination": destination,
    "distance": f"{round(distance/1000, 2)} Km",
    "duration": format_timespan(duration),
    "route": route_list
  }