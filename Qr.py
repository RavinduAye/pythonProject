import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sys
import subprocess

camera_port = 0
cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()

    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')

        if myData in myDataList:
            text3 = myData
            UI = open('UserID', 'w')
            UI.write(text3)
            UI.close()

            cv2.imshow('Result', img)
            cv2.waitKey(1)
            cap.release()
            cv2.destroyWindow('Result')

            import interface2

        myOutput = 'Un-Authorized'
        myColor = (0, 0, 255)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(img, myOutput + "- press n for exit", (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

    cv2.imshow('Result', img)
    k = cv2.waitKey(1)

    if k == ord('n'):
        cap.release()
        cv2.destroyWindow('Result')
        subprocess.check_call((sys.executable, 'home.py'))
