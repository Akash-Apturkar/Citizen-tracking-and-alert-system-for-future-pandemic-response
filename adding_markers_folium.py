# import libraries for folium
import folium
import pandas as pd
import webbrowser 
import os
 
#define test values input to which is taken from firebase
latitude = [52.515707,52.522,52.5334,52.5666]
longitude = [13.379387, 13.3790, 13.3547, 13.3444]
userid = "test"


homedir = os.path.expanduser("~") #creating a home dir to store the export.html file

# Make a data frame with dots to show on the map
def get_map(latitude, longitude,userid):

# Make an empty map
    data = pd.DataFrame({
    'lat': latitude,
    'lon': longitude,
   
    })
    data
    m = folium.Map(location=[52.515707, 13.379387], tiles='OpenStreetMap', zoom_start=13)
# Add marker one by one on the map
    for i in range(0,len(data)):
        folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=userid).add_to(m)
# Save it as html
    m.save('markers_on_folium_map.html')
    webbrowser.open(homedir+"/markers_on_folium_map.html")
    

#calling the fucntion
get_map(latitude,longitude,userid)
