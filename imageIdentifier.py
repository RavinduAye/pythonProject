import cv2
import sys
import os
import subprocess


path = 'Resources'

orb = cv2.ORB_create(nfeatures=1000)

images = []
classNames = []
myList = os.listdir(path)
print('Total Classes Detected', len(myList))

for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findDes(Images):

    descriptorList = []

    for img in Images:
        kp, des = orb.detectAndCompute(img, None)
        descriptorList.append(des)
    return descriptorList


def findID(img, descriptorList, thresher=15):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()
    matchList = []
    finalVal = -1
    try:
        for des in descriptorList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchList.append(len(good))

    except:
        pass

    if len(matchList) != 0:
        if max(matchList) > thresher:
            finalVal = matchList.index(max(matchList))
    return finalVal


desList = findDes(images)
print(len(desList))

camera_port = 0
cap = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)

while True:

    success, img2 = cap.read()

    if img2 is None:
        break
    imgOriginal = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    id = findID(img2, desList)
    if id != -1:

        text = classNames[id]
        cv2.putText(imgOriginal,  "Do you want "+classNames[id]+"(Y/N)", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('img2', imgOriginal)
        k = cv2.waitKey(1)

        if k == ord('y'):
            cap.release()
            cv2.destroyWindow('img2')
            selectedMed = open('selectedMedicine', 'w')
            selectedMed.write(text)
            selectedMed.close()
            subprocess.check_call((sys.executable, 'firebase.py'))

        elif k == ord('n'):
            cap.release()
            cv2.destroyWindow('img2')
            subprocess.check_call((sys.executable, 'interface2.py'))

    else:
        cv2.putText(imgOriginal, "Doesn't match. Press 'n' for exit", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('img2', imgOriginal)
        k = cv2.waitKey(1)

        if k == ord('n'):
            cap.release()
            cv2.destroyWindow('img2')
            subprocess.check_call((sys.executable, 'interface2.py'))
