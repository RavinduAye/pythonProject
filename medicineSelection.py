import sys
import subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.Qt import Qt


class medicineSelection(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi('interfaces/VoiceRecognition/voice2.ui', self)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_A:
            subprocess.check_call((sys.executable, 'voiceRecog.py'))


        elif event.key() == Qt.Key_2:
            subprocess.check_call((sys.executable, 'interface2.py'))

        self.close()


app = QApplication(sys.argv)

window = medicineSelection()
window.show()
sys.exit(app.exec_())
