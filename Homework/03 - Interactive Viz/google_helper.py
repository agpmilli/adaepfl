"""
Helper functions to transform our list of universities to a list of Swiss Canton ids.
We use the Google Maps API with a dummy Google account to retrieve the latters.
"""
import googlemaps
import credentials
import json

######## string operations to clean university names ########
def extract_uni_name(arr):
    return [split_dash(s) for s in arr]


def split_dash(s):
    return s.split('-')[0].strip()


##################### google geocoding ######################
def university_to_id(uni, maps):
    result = maps.geocode(uni)
    if len(result) == 0:
        return uni, places_near(uni, maps)
    else:
        return uni, extract_json(result)

def canton_ids(universities):
    maps = googlemaps.Client(key=credentials.API_KEY)
    ids = [university_to_id(uni, maps) for uni in extract_uni_name(universities)]
    return ids

def extract_json(js):
    area = [x['short_name'] for x in js[0]['address_components'] if 'administrative_area_level_1' in x['types']]
    if(len(area) == 0):
        return None
    return area[0]

def places_near(uni, maps):
    geocode_result = maps.places(uni)
    if(len(geocode_result) == 0):
        return None
    results = geocode_result['results']
    if(len(results) == 0):
        return None
    lat_lng = results[0]['geometry']['location']
    return extract_json(maps.reverse_geocode(lat_lng))
