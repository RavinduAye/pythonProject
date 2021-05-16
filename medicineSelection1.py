import sys
import subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.Qt import Qt


class medicineSelection1(QMainWindow):

    def __init__(self):

        super().__init__()

        from voiceRecog import text1
        self.text1 = text1


        loadUi('interfaces/VoiceRecognition/voice.ui', self)
        self.loadClicked()

    def loadClicked(self):

        self.textBrowser.setText("Do you want {}".format(self.text1) + " ?")

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_1:

            selectedMed = open('selectedMedicine', 'w')
            selectedMed.write(self.text1)
            selectedMed.close()
            self.close()
            subprocess.check_call((sys.executable, 'firebase.py'))


        elif event.key() == Qt.Key_2:
            self.close()
            subprocess.check_call((sys.executable, 'interface2.py'))

        self.close()


app = QApplication(sys.argv)
window = medicineSelection1()
window.show()
sys.exit(app.exec_())
