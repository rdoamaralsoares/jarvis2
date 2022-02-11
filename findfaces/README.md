# Findfaces
Code that read images via RTSP from Meraki Cameras and perform a face identifier of users based on a local data base with know users. There is the capacity to export that data via API in a Json format.

# Objective
Objective of that code is perform a face search in a data base in real time, capturing images data from Meraki's Cameras via RTSP and share that via API integration.

# Install
Copy files and run the "requirements.txt"

```
pip install -r requirements.txt
```


# Running
At folder faces you will find some examples of faces. You need to follow that steps:
1) Take a picture of your face at the same format of example of faces founded at "faces" folder.
2) Save your picture at "faces" folder.
3) Run "encode.py" to extract your face encoding.
4) You will generate the file "faces.json" that should contain all faces encoded. Identify your face code by the name of your face file at key "filename".
5) Add manualy your user data at database_temp.json following the same keys and templates in "database_temp.json"
6) Att field "face" you should copy your encoded face from "faces.json" file.
--> Atention: You should remove "" character from the array that represents your face. The "face" key should contain a list type not a string.
7) At "main.py" file you should enter with your camera IP Adrress. 
--> Make sure that you enable the RTSP streaming at Meraki dashboard.
--> Your computer and camera should be at the same local network.
8) Run "main.py" and wait some seconds to load the screen showing the captured images.
9) Show the terminal outputs to see the logs that the system will generates when identify you.

# API
There is an object created at the code that could export the data of user identified via API interaction. If you whould like to export the data via API you could study that structure located at "api_interaction.py" file and configure with you API data.

To enable the API interaction after your configuration, at "main.py" file you should enable the API at its creation in the line 11. Change the active parameter to True - api = Api(active=True).

When the system identify an user, it will send via API the data at Json format. To read about the json format, see at the console output the tag "=> people" when the syste recognize you.

The systes was written to notify if a unknow user is stoped in front of camera. If a unknow user stay stoped in front of camera and the system not found at the database after ten subsequent attempts, they will notify an unknow user if the API is enabled.

# Contact
Created by: Ricardo Soares

Personal e-mail: soares.ricardo@gmail.com

Corporate e-mail: ricardo.a.soares@global.ntt
