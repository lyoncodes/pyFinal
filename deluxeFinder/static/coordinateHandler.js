$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places,geometry") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete())

})

const loc_coordinates = [
  {
      "name": 'qa',
      "lat": 47.6234577,
      "long": -122.356369,
      "address": "500 Queen Anne Ave N, Seattle, WA 98109"
  },
  {
      "name": 'wall',
      "lat": 47.6610617,
      "long": -122.329966,
      "address": "111 NE 45th St, Seattle, WA 98105"
  },
  {
      "name": 'caphill',
      "lat": 47.619400,
      "long": -122.321274,
      "address": "115 Broadway E, Seattle, WA 98102"
  },
  {
      "name": 'hol',
      "lat": 47.69639255276665,
      "long": -122.37167349092192,
      "address": "9208 Holman Road NW, Seattle, WA 98117"
  },
  {
      "name": 'kent',
      "lat": 47.384308,
      "long": -122.2985485,
      "address": "24220 Pacific Hwy S, Kent, WA 98032"
  },
  {
      "name": 'lake',
      "lat": 47.7182053,
      "long": -122.2990875,
      "address": "12325 30th Ave NE, Seattle, WA 98125"
  },
  {
      "name": 'ed',
      "lat": 47.8011279,
      "long": -122.3339186,
      "address": "21910 HWY 99, Edmonds, WA 98026"
  },
  {
      "name": 'cr',
      "lat": 47.6173975,
      "long": -122.1339078,
      "address": "15600 NE 8th St Suite O-1, Bellevue, WA 98008"
  }

]

const auto_fields = ['a', 'b']
// points = document.getElementsByClassName('point-waypoint')
// for (point of points) {
//   point.addEventListener('click', () => {
//     onPlaceChanged('waypoint')
//   })
// }


function initAutocomplete() {
  for (i = 0; i < auto_fields.length; i++) {
    var field = auto_fields[i]
    window['autocomplete_'+field] = new google.maps.places.Autocomplete(
      document.getElementById('point-' + field),
    {
       types: ['address'],
       componentRestrictions: {'country': [base_country.toLowerCase()]},
    })
  }

  // add event listeners
  autocomplete_a.addListener('place_changed', function(){
    onPlaceChanged('a')
  });
}

function onPlaceChanged(token){  
    var auto = window['autocomplete_'+token]
    var el_id = 'point-' + token
    var lat_id = 'id-lat-' + token
    var long_id = 'id-long-' + token
    var address = document.getElementById(el_id).value // collect values from route form input
    callGeoCode(address, lat_id, long_id, token)
}

function callGeoCode(address, lat_id, long_id, token){
  const geocoder = new google.maps.Geocoder() // instantiate new Geocoder

  geocoder.geocode( { 'address': address}, function(results, status) {

    if (status == google.maps.GeocoderStatus.OK) {
        // get lat/long values from response results
        var latitude = results[0].geometry.location.lat();
        var longitude = results[0].geometry.location.lng();

        closest_location_from_point = findClosest(results[0].geometry.location)

        // assign values to hidden inputs
        $('#' + lat_id).val(latitude) 
        $('#' + long_id).val(longitude) 
        console.log($('#' + lat_id).val(latitude) )

        // call calculate
        calcRoute(closest_location_from_point, token)
    } 
  }); 
}

function validateForm() {
    var valid = true;
    $('.geo').each(function () {
        if ($(this).val() === '') {
            valid = false;
            return false;
        }
    });
    return valid
}

function findClosest(point){
  let closest = []
  for (let i = 0; i < loc_coordinates.length; i++) {

    // get location
    let loc = { 'lat': loc_coordinates[i].lat, 'lng': loc_coordinates[i].long }
    
    // find closest
    loc_coordinates[i].distance = google.maps.geometry.spherical.computeDistanceBetween(point, loc)
    console.log(loc_coordinates[i].distance)

    closest.push(loc_coordinates[i])
  }
  //return closest
  closest.sort((a, b) => {
    return a.distance - b.distance;
  });

  return closest[0]
}

function calcRoute(closest_location, addy){
    // if ( validateForm() == true){
      const params = {
        lat_a: $('#id-lat-' + addy).val(),
        long_a: $('#id-long-' + addy).val(),
        lat_b: closest_location.lat,
        long_b: closest_location.long,
      };
      // format URL
      let esc = encodeURIComponent;
      let query = Object.keys(params)
          .map(k => esc(k) + '=' + esc(params[k]))
          .join('&');

      url = '/map?' + query
      window.location.assign(url)
    // }

}