import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.Qt import Qt
import subprocess


class logging(QMainWindow):

    def __init__(self):
        super().__init__()

        loadUi('interfaces/restrictMedicine.ui', self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_2:
            self.close()
            subprocess.check_call((sys.executable, 'interface2.py'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = logging()
    window.show()
    sys.exit(app.exec_())
