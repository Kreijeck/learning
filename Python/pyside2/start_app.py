from PySide2 import QtWidgets
import sys

from Python.pyside2.main import Ui_Form

class MainWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Learning")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    start = MainWidget()
    start.show()

    sys.exit(app.exec_())
