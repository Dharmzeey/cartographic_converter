from pyproj import Proj
import math

def UTM_to_latlon(zone, easting, northing):
  zone = float(zone)
  easting = float(easting)
  northing = float(northing)

  # Define the UTM zone
  # zone = math.floor ((lon + 180.0) / 6) + 1

  # Create a Proj object for the UTM zone
  p = Proj(proj='utm', zone=zone, ellps='WGS84')

  # Define the easting and northing coordinates

  # Convert the easting and northing coordinates to longitude and latitude
  longitude, latitude = p(easting, northing, inverse=True)
  ret_val = "Latitude: %.7f" % latitude , "Longitude: %.7f" % longitude
  return ret_val


def UTM_to_DMS(zone, easting, northing):

  zone = float(zone)
  easting = float(easting)
  northing = float(northing)


  # Define the UTM zone
  # zone = 31
  # zone = math.floor ((lon + 180.0) / 6) + 1


  # Create a Proj object for the UTM zone
  p = Proj(proj='utm', zone=zone, ellps='WGS84')

  # Define the easting and northing coordinates

  # Convert the easting and northing coordinates to longitude and latitude
  longitude, latitude = p(easting, northing, inverse=True)

  # Convert latitude to degrees
  latitude_degrees = int(latitude)

  # Convert longitude to degrees
  longitude_degrees = int(longitude)

  # Convert the remaining decimal part of latitude to minutes
  latitude_minutes_decimal = abs(latitude - latitude_degrees)
  latitude_minutes = latitude_minutes_decimal * 60

  # Convert the remaining decimal part of longitude to minutes
  longitude_minutes_decimal = abs(longitude - longitude_degrees)
  longitude_minutes = longitude_minutes_decimal * 60

  # Convert the remaining decimal part of minutes to seconds
  latitude_seconds_decimal = latitude_minutes % 1
  latitude_seconds = latitude_seconds_decimal * 60

  longitude_seconds_decimal = longitude_minutes % 1
  longitude_seconds = longitude_seconds_decimal * 60
  
  # THIS IS TO ASSIGN THE HEMISPHERE BASED ON THE SIGN OF THR DEGREE
  x_axis = "E" if longitude_degrees > 1 else "W"
  y_axis = "N" if latitude_degrees > 1 else "S"

  # convert degrees into +ve incase of west and south
  latitude_degrees = abs(latitude_degrees)
  longitude_degrees = abs(longitude_degrees)
  
  # convert the minutes to integer
  latitude_minutes = int(latitude_minutes_decimal * 60)
  longitude_minutes = int(longitude_minutes_decimal * 60)
  
  # Round the seconds to the nearest integer
  latitude_seconds = round(latitude_seconds)
  longitude_seconds = round(longitude_seconds)
  ret_val = f"Latitude {latitude_degrees}°{latitude_minutes}'{latitude_seconds} {y_axis}", f"Longitude {longitude_degrees}°{longitude_minutes}'{longitude_seconds} {x_axis}"
  return ret_val


