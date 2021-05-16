import time
import sys
import runpy
import subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.Qt import Qt
import cv2


class medicineSelection3(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi('interfaces/VoiceRecognition/voicedoesntmatch.ui', self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_2:
            self.close()
            subprocess.check_call((sys.executable, 'interface2.py'))


app = QApplication(sys.argv)

window = medicineSelection3()
window.show()

sys.exit(app.exec_())
