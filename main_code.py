from firebase import firebase
import os.path
import tkinter as tk
import gmaps
from ipywidgets.embed import embed_minimal_html
import webbrowser


authentication = firebase.FirebaseAuthentication('<Your API Key here>', '<Your mail id here>', extra={'id': '<Your Firebase id here>'})
fireapp = firebase.FirebaseApplication('https://apptest-cad89.firebaseio.com/',  authentication=authentication)

gmaps.configure(api_key='AIzaSyBReFmkZK6DbZomh2X9ztXRfO84HVabF3Y')

root= tk.Tk()
homedir = os.path.expanduser("~") #creating a home dir to store the export.html file
canvas1 = tk.Canvas(root, width = 700, height = 600)
canvas1.pack()
label1 = tk.Label(root, text='PANDEMIC ALERT SYSTEM')
label1.config(font=('helvetica', 10))
canvas1.create_window(350, 25, window=label1)

label3 = tk.Label(root, text='Enter the UID:')
label3.config(font=('helvetica', 9))
canvas1.create_window(350, 120, window=label3)

entry1 = tk.Entry (root) 
canvas1.create_window(350, 140, window=entry1)

#root.geometry("120*60")

def get_data():
    list1 = []
    list2 = []
    contact_persons_uid = ['001', '002','003']
    
    for item in contact_persons_uid:
        listbox.insert(END, item)
    
    firebase1 = firebase.FirebaseApplication("https://apptest-cad89.firebaseio.com/",None)
    user_input = entry1.get()
    label_path_lat = "/Data/{}/lat".format(user_input)
    label_path_long = "/Data/{}/long".format(user_input)
    result = firebase1.get(label_path_lat,'')
    
    for i in result.split(","):
        x = float(i)
        list1.append(x)
    result = firebase1.get(label_path_long,'')
    for i in result.split(","):
        x = float(i)
        list2.append(x)
        
    locations = list(zip(list1,list2))
    marker_locations= locations

    fig=gmaps.figure()
    markers=gmaps.marker_layer(marker_locations)
    fig.add_layer(markers)
    embed_minimal_html('export.html', views=[fig])
    webbrowser.open(homedir+"/Downloads/export.html")

def open():
    x1 = entry1.get()
    try:
        get_data()
    except Exception:
        label3['text'] = "Please check the UID"
    

button = tk.Button (root, text = "Show Map with markers", command = open)
canvas1.create_window(350, 180, window=button)
listbox = tk.Listbox(root)
canvas1.create_window(350, 350, window=listbox)
label2 = tk.Label(root, text='Designed by \n ')
label2.config(font=('helvetica', 10))
label2.pack()
root.mainloop()


