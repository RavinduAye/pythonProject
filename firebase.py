import pyrebase

global med_details
global userData

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

with open('selectedMedicine') as s:
    medic = s.read().splitlines()
    # print(medic)

    if medic == ['hello']:
        medi = 'hello'
    elif medic == ['panadol']:
        medi = 'panadol'
    elif medic == ['siddhalepa']:
        medi = 'siddhalepa'
    elif medic == ['painkiller'] or medic == ['painkillers']:
        medi = 'painkiller'


def to_int(x):
    try:
        return int(x)
    except ValueError:
        return x


with open('UserID') as f:
    medicines = f.read().splitlines()

new_a = [to_int(x) for x in medicines]


users = db.child("Customers").get()
medPrice = db.child("MedicinePrice").get()

for user in users.each():
    print(user.val().get('accountNumber'))

    if new_a == [user.val().get('accountNumber')]:
        userKey = user.key()
        userName = user.val().get('name')
        userAcc = user.val().get('accountNumber')
        userAmount = user.val().get('amount')
        userDate = user.val().get('restrictDate')
        userData = [userKey, userName, userAcc, userAmount, userDate]
        print(userData)
        # print(userAcc)

for medprice in medPrice.each():
    # print(medprice.val())

    if medi == medprice.val().get('Mname'):
        med_key = medprice.key()
        med_name = medprice.val().get('Mname')
        med1_price = medprice.val().get('Price')
        med_quantity = medprice.val().get('Quantity')
        med_details = [med_key, med_name, med1_price, med_quantity]
        print(med_quantity)

from payment import pay

pay.med(med_details, userData)
