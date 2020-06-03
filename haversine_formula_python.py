import math

#Haversine function to find the distance between 2 points on a sphere by using the latitude and longitude
def havers(lat1, lat2, lon1, lon2):

    R = 6373.0
    #radius of the Earth

    #convert the latitude longitude details to radians
    latitude1 = math.radians(lat1)
    longitude1 = math.radians(lon1)
    latitude2 = math.radians(lat2)
    longitude2 = math.radians(lon2)

    #determine the change in coordinates
    dlon = longitude2 - longitude1
    dlat = latitude2 - latitude1

    #formula to find the distance
    a = math.sin(dlat / 2)**2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = ( R * c ) * 1000

    return(distance)

lat1 = 52.467362
lat2 = 52.466336
lon1 = 13.320594
lon2 = 13.328108
result = havers(lat1, lat2, lon1, lon2)
print(result)
