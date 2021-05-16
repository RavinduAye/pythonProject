import sys
import subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.Qt import Qt


class usingKeypad(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi('interfaces/mainwindow.ui', self)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_1:
            loadUi('interfaces/medicines.ui', self)

        elif event.key() == Qt.Key_2:
            self.close()
            subprocess.check_call((sys.executable, 'medicineSelection.py'))

        elif event.key() == Qt.Key_3:
            self.close()
            subprocess.check_call((sys.executable, 'imageIdentifier.py'))

        elif event.key() == Qt.Key_4:
            self.close()


app = QApplication(sys.argv)
window = usingKeypad()
window.show()
sys.exit(app.exec_())
