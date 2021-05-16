import calendar
import datetime
import subprocess
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

import pyrebase

today_1 = datetime.date.today()
todayS = str(today_1)

days = calendar.monthrange(today_1.year, today_1.month)[1]

sdate = today_1 + datetime.timedelta(days=days)
dateS = str(sdate)


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

users = db.child("Customers").get()
medicine = db.child("MedicinePrice").get()
message = db.child("MedicineNotification").get()


class pay:

    @staticmethod
    def med(med, user):
        if med[1] == 'panadol' or med[1] == 'siddhalepa':
            res_med = 0
            # print(user)
        elif med[1] == 'painkiller' or med[1] == 'painkillers':
            userDate = user[4]

            if userDate == '':
                res_med = 1
                print("res_med = 1")

            elif userDate != '':
                date_time_obj = datetime.datetime.strptime(userDate, '%Y-%m-%d')
                date = date_time_obj.date()

                if today_1 >= date:
                    res_med = 2
                    # print("res_med = 2")

                elif today_1 <= date:
                    res_med = 3
                    # print("res_med = 3")

            else:
                print("incorrect")


        for user1 in users.each():
            # print(user1.key())

            if user1.key() == user[0]:
                UserId = user1.key()

        for medicineName in medicine.each():
            if medicineName.key() == med[0]:
                medId = medicineName.key()
                # print(medId)


        class payment(QMainWindow):

            def __init__(self):

                super().__init__()

                loadUi('interfaces/paymentDetails.ui', self)
                self.loadClicked()

            def loadClicked(self):
                self.textBrowser.setText(user[1])
                self.textBrowser_2.setText(str(user[2]))
                self.textBrowser_3.setText(str(user[3]))
                self.textBrowser_5.setText(med[1])
                self.textBrowser_4.setText(str(med[2]))

            def keyPressEvent(self, event):

                if event.key() == Qt.Key_1:

                    if user[3] > med[2] and user[3] != 0:
                        if res_med == 0:
                            newAmount = user[3] - med[2]
                            db.child("Customers").child(UserId).update({"amount": newAmount})
                            print(newAmount)

                            self.load()

                            # subprocess.check_call((sys.executable, 'voiceRecog.py'))
                        elif res_med == 1:
                            newAmount = user[3] - med[2]
                            db.child("Customers").child(UserId).update({"amount": newAmount})
                            db.child("Customers").child(UserId).update({"restrictDate": dateS})

                            self.load()
                            # print("true restricted 1")

                        elif res_med == 2:
                            newAmount = user[3] - med[2]
                            db.child("Customers").child(UserId).update({"amount": newAmount})
                            db.child("Customers").child(UserId).update({"restrictDate": dateS})
                            self.load()
                            # print("true restricted 2")

                        elif res_med == 3:
                            subprocess.check_call((sys.executable, 'NotEligible_RestrictMedicine.py'))
                            # print("true restricted 3")


                        else:
                            print("A")

                    else:
                        self.close()
                        subprocess.check_call((sys.executable, 'insufficientBalance.py'))


                elif event.key() == Qt.Key_2:
                    self.close()
                    subprocess.check_call((sys.executable, 'interface2.py'))

            def load(self):


                medQuantity = med[3] - 1

                if medQuantity == -1:
                    # Account eke balance eka thibila beheth ganna beri unoth aaye account balance eka thibba ganama wenna oone
                    # restrict Date ekath add wenna be beheth ganna beri unoth
                    newAmount = user[3]
                    db.child("Customers").child(UserId).update({"amount": newAmount})
                    db.child("Customers").child(UserId).update({"restrictDate": ''})

                    data = {"date": "{}".format(todayS), "Notification": "Medicine over = {}".format(med[1])}
                    db.child("MedicineNotification").push(data)

                    self.close()

                    subprocess.check_call((sys.executable, 'medicineOver.py'))

                elif medQuantity >= 0:
                    db.child("MedicinePrice").child(medId).update({"Quantity": medQuantity})
                    # print(medQuantity)

                    if 3 > medQuantity:
                        text = med[1]
                        # print(text)
                        data = {"date": "{}".format(todayS), "Notification": "Medicine Refill Needed {}".format(text)}
                        db.child("MedicineNotification").push(data)


        app = QApplication(sys.argv)

        window = payment()
        window.show()
        sys.exit(app.exec_())
