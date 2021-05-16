import pyrebase
global med1_price, userData

firebaseConfig = {"apiKey": "AIzaSyABh5NA4kJSWoPS_3Q8vwX-fqDoy63HjYg",
                  "authDomain": "medicineatm-7d374.firebaseapp.com",
                  "databaseURL": "https://medicineatm-7d374-default-rtdb.firebaseio.com/",
                  "projectId": "medicineatm-7d374",
                  "storageBucket": "medicineatm-7d374.appspot.com",
                  "messagingSenderId": "961671499065",
                  "appId": "1:961671499065:web:c6080afb602762b8a06ce8",
                  "measurementId": "G-SL89Z8HNWX"
                  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


data = {"accountNumber": 777777, "amount": 1160, "name": "A.D Wijayarathne", "restrictDate": ''}
db.child("Customers").push(data)

# data = {"Notification": " "}
# db.child("MedicineNotification").push(data)
