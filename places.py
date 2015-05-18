import sys, os, re
import requests, httplib
from geopy.geocoders import Nominatim
from math import *
import numpy as np 
import matplotlib.pyplot as plt

places_api_key = "tonal-unity-94913"

def GooglePlacesAPIHttpRequest(**kwargs):
	start_string = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
	for i, key in enumerate(kwargs):
		if i == 0:
			start_string = "%s%s=%s"%(start_string, key, kwargs[key])
		else:
			start_string = "%s&%s=%s"%%(start_string, key, kwargs[key])

geocoder = Nominatim()
def get_latlong(city_name):
	loc = geolocator.geocode(city_name)
	return loc.latitude, loc.longitude


def get_places_near_city(city_name, nplaces=10):
	lat, lon = get_latlong(city_name)

