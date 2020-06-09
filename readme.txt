----CITIZEN TRACKING AND ALERT SYSTEM FOR FUTURE PANDEMIC RESPONSE----
**************************************************************************************************
@ authors :
Akash Apturkar
Arush Oli
Nidhi Kulkarni
Aqsa Fridaus Khan

-----------------------
Steps for installing :-
-----------------------
For executing the code, run the main_code_updated.py. For that the prerequisites need to be completed:

Firebase credentials of the database need to be supplied in the  main_code_updated.py and also the android app (download and open 
the .aia file in MIT appinventor for that)

The following modules need to be installed using pip in the command prompt before running the main code:

pip install folium

pip install pandas

pip install requests


pip install python-firebase

note:- Edit line no 11,12 in main code to add your Firebase credentials

----------------------------------------------
----If firebase is having problem in import----
----------------------------------------------


then go to your file where firebase is saved then

1)rename .async into .async_
2)open _ini_file and change .async into .async_
3)open firebase.py and change .async into .async_

because of .async is the keyword now is current version in python

For Android app :
-----------------
For editing:
Download Big_data.aia file, open MIT app inventor website -> login -> in my projects select "import .aia from computer"
view and edit the project in MIT app inventor

For testing:
Download Big_data.aia file in smartphone
install
open ->select register new user -> enter name and set password
login
tracking begins

