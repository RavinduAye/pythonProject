from pyrebase import pyrebase
import numpy as np

firebaseConfig = {"apiKey": "AIzaSyABh5NA4kJSWoPS_3Q8vwX-fqDoy63HjYg",
                  "authDomain": "medicineatm-7d374.firebaseapp.com",
                  "databaseURL": "https://medicineatm-7d374-default-rtdb.firebaseio.com/",
                  "projectId": "medicineatm-7d374",
                  "storageBucket": "medicineatm-7d374.appspot.com",
                  "messagingSenderId": "961671499065",
                  "appId": "1:961671499065:web:c6080afb602762b8a06ce8",
                  "measurementId": "G-SL89Z8HNWX"
                  }

global array

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

users = db.child("Customers").get()

for user in users.each():
    b = user.val().get('accountNumber')
    a = str(b)
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()



