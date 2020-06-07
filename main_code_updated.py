import webbrowser
import os
import pandas as pd
import folium
import math
from firebase import firebase 
import os.path
import tkinter as tk

authentication = firebase.FirebaseAuthentication('tl9sQ6cK6MsDjscyRtVTfOmSeeKDJsfILXjgHYsc', 'nidhu.kulkarni@gmail.com', extra={'id': 'fbaf0fed-762d-4e02-a62d-302db69636fb'})
fireapp = firebase.FirebaseApplication('https://apptest-cad89.firebaseio.com/',  authentication=authentication)
root= tk.Tk()
homedir = os.path.expanduser("~") #creating a home dir to store the export.html file
canvas1 = tk.Canvas(root, width = 700, height = 600, bg = 'black')
canvas1.pack()
label1 = tk.Label(root, text='PANDEMIC ALERT SYSTEM')
label1.config(font=('helvetica', 30), bg = 'black', fg = 'white')
canvas1.create_window(350, 35, window=label1)

label3 = tk.Label(root, text='Enter the UID:')
label3.config(font=('helvetica', 15), bg = 'black', fg = 'white')
canvas1.create_window(350, 120, window=label3)

entry1 = tk.Entry (root) 
canvas1.create_window(350, 140, window=entry1)
contact_persons_uid = []
#root.geometry("120*60")

label4 = tk.Label(root, text='Contact Persons:')
label4.config(font=('helvetica', 15), bg = 'black', fg = 'white')
canvas1.create_window(350, 250, window=label4)


def get_data(uid):
    list1 = []
    list2 = []
    
    
    listbox = tk.Listbox(root)
    canvas1.create_window(350, 350, window=listbox)
    

    firebase1 = firebase.FirebaseApplication("https://apptest-cad89.firebaseio.com/",None)
    
    label_path_lat = "Data/{}/lat".format(uid)
    label_path_long = "Data/{}/long".format(uid)
    result = firebase1.get(label_path_lat,'')
    result= result.replace('"','')#added to remove extra " added while uploading from app
    for i in result.split(","):
        x = float(i)
        list1.append(x)
    result = firebase1.get(label_path_long,'')
    result= result.replace('"','')#added to remove extra " added while uploading from app
    for i in result.split(","):
        x = float(i)
        list2.append(x)
        
    return list1, list2
    
def call_map():
    uid = entry1.get()
    try:
        latitude, longitude = get_data(uid)
        latitude = [i for i in latitude if i != 0]
        longitude = [i for i in longitude if i != 0]
        get_map(latitude, longitude, uid)
    except Exception:
        label3['text'] = "Please check the UID"

        
def get_map(latitude, longitude,userid):

# Make an empty map
    data = pd.DataFrame({
    'lat': latitude,
    'lon': longitude,
   
    })
    
    m = folium.Map(location=[52.515707, 13.379387], tiles='OpenStreetMap', zoom_start=13)
# Add marker one by one on the map
    for i in range(0,len(data)):
        folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=userid).add_to(m)
# Save it as html
    m.save('markers_on_folium_map.html')
    webbrowser.open(homedir+"/markers_on_folium_map.html")
    
    
    
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


def get_contact_person():
    list_uids=[]
    firebase1 = firebase.FirebaseApplication("https://apptest-cad89.firebaseio.com/",None)
    label_path = "Data/{}".format("uids")
    result = firebase1.get(label_path,'')
    result= result.replace('"','')#added to remove extra " added while uploading from app
    for i in result.split(","):
        list_uids.append(i)
    
    uid = entry1.get()
    lat1, long1 = get_data(uid)
    lat1 = [i for i in lat1 if i != 0]
    long1 = [i for i in long1 if i != 0]
    data1 = pd.DataFrame({
    'lat': lat1,
    'lon': long1,

    })
    print(list_uids)
    list_uids.remove(uid)
    print(list_uids)
    for item in list_uids:
        
        print(item)
        lat2,long2 = get_data(item)
        lat2 = [i for i in lat2 if i != 0]
        long2 = [i for i in long2 if i != 0]
        data2 = pd.DataFrame({
        'lat': lat2,
        'lon': long2,
        })
        
        for i in range(0,len(data1)): 
            for j in range(0,len(data2)): 
                dist= havers(data1.iloc[i]['lat'],data2.iloc[j]['lat'],data1.iloc[i]['lon'],data2.iloc[j]['lon'])
                print(dist)
                if dist < 30:
                    if item not in contact_persons_uid:
                        print("Contact detected")
                        contact_persons_uid.append(item)
        
    listbox = tk.Listbox(root)
    canvas1.create_window(350, 350, window=listbox)        
    for item in contact_persons_uid:
        listbox.insert(tk.END,item)
    
def send_alert():
    for i in contact_persons_uid:
        firebase1 = firebase.FirebaseApplication("https://apptest-cad89.firebaseio.com/",None)
        label_path = "Data/{}".format(i)
        firebase1.put(label_path,'notification','alert')    
    
def main():
    
    display_map_button = tk.Button(root, text = "Show Map with markers", command = call_map, bg = 'cyan', fg = 'black')

    canvas1.create_window(350, 180, window=display_map_button)
    
    button = tk.Button(root, text = "Get contact persons", command = get_contact_person, bg = 'cyan', fg = 'black')
    canvas1.create_window(350, 210, window=button)
    listbox = tk.Listbox(root)
    canvas1.create_window(350, 350, window=listbox)
    button1 = tk.Button(root, text = "Send Alert", command = send_alert, bg = 'cyan', fg = 'black')
    canvas1.create_window(350, 460, window=button1)
    label2 = tk.Label(root, text='Designed by, \n Akash Apturkar, Arush Oli, Aqsa Firdaus Khan, Nidhi Krishna Kulkarni\n Under the guidance of Sreeganesh Thottempudi \n SRH Berlin University  ')
    label2.config(font=('helvetica', 10), bg = 'black', fg = 'white')
    canvas1.create_window(350, 560, window=label2)
    root.mainloop()

main()
