from firebase import firebase
import os.path
import tkinter as tk
import webbrowser

authentication = firebase.FirebaseAuthentication('<your_api _key_here>', '<your_email_id>', extra={'id': '<your_firebase_uid>'})
fireapp = firebase.FirebaseApplication('<your_firebase_url>',  authentication=authentication)

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

def get_data(uid):
    list1 = []
    list2 = []
    contact_persons_uid = ['001', '002','003']
    
    listbox = tk.Listbox(root)
    
    for item in contact_persons_uid:
        listbox.insert(tk.END,item)
    
    firebase1 = firebase.FirebaseApplication("<your_firebase_url>",None)
    
    label_path_lat = "/Data/{}/lat".format(uid)
    label_path_long = "/Data/{}/long".format(uid)
    result = firebase1.get(label_path_lat,'')
    
    for i in result.split(","):
        x = float(i)
        list1.append(x)
    result = firebase1.get(label_path_long,'')
    
    for i in result.split(","):
        x = float(i)
        list2.append(x)
        
    return list1, list2
    
def call_map():
    uid = entry1.get()
    try:
        latitude, longitude = get_data(uid)
        get_map(latitude, longitude)
    except Exception:
        label3['text'] = "Please check the UID"
    
def main():
    display_map = tk.Button(root, text = "Show Map with markers", command = call_map)
    canvas1.create_window(350, 180, window=display_map)
    listbox = tk.Listbox(root)
    canvas1.create_window(350, 350, window=listbox)
    label2 = tk.Label(root, text='Designed by \n ')
    label2.config(font=('helvetica', 10))
    label2.pack()
    root.mainloop()

main()
