import math

EARTH_RADIUS_KM = 6378.137

def distance_in_meters(lat1, lon1, lat2, lon2):
    d_lat = (lat2 * math.pi) / 180 - (lat1 * math.pi) / 180
    d_lon = (lon2 * math.pi) / 180 - (lon1 * math.pi) / 180
    a = math.sin(d_lat / 2) * math.sin(d_lat / 2) +\
        math.cos((lat1 * math.pi) / 180) * math.cos((lat2 * math.pi) / 180) *\
        math.sin(d_lon / 2) * math.sin(d_lon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = 1000. * EARTH_RADIUS_KM * c
    return d
