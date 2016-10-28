"""
Helper functions to transform our list of universities to a list of Swiss Canton ids.
We use the Google Maps API with a dummy Google account to retrieve the latters.
"""
import googlemaps
import credentials
import json


def extract_uni_name(arr):
    """
    Extract the universities' name and return an array of it
    Parameters:
      arr - the array of university name where each element is of the form (name - some_text).
    """
    return [s.split('-')[0].strip() for s in arr]


def university_to_id(uni, maps):
    """
    Return the mapping between the university name and its canton (or None if not found)
    Parameters:
      uni - the array of university names
      maps - the googlemaps instance
    """
    result = maps.geocode(uni)
    if len(result) == 0:
        return uni, places_near(uni, maps)
    else:
        return uni, extract_json(result)

def canton_ids(universities):
    """
    Return the mapping between the university name and its canton (or None if not found). 
    This is what the caller should use
    Parameters:
      universities - the array of university name where each element is of the form (name - some_text).
    """
    maps = googlemaps.Client(key=credentials.API_KEY)
    ids = [university_to_id(uni, maps) for uni in extract_uni_name(universities)]
    return ids

def extract_json(js):
    """
    Return the canton for a specific university name or None if not found 
    Parameters:
      js - the JSON response returned by the Google Maps API
    """
    area = [x['short_name'] for x in js[0]['address_components'] if 'administrative_area_level_1' in x['types']]
    if(len(area) == 0):
        return None
    return area[0]

def places_near(uni, maps):
    """
    Return the mapping between the university name and its canton (or None if not found)
    Parameters:
      uni - the array of university names
      maps - the googlemaps instance
    """
    geocode_result = maps.places(uni)
    if(len(geocode_result) == 0):
        return None
    results = geocode_result['results']
    if(len(results) == 0):
        return None
    lat_lng = results[0]['geometry']['location']
    return extract_json(maps.reverse_geocode(lat_lng))
