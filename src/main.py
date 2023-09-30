from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PySide6.QtCore import QTimer
from UI.Pform import Ui_Form
import sys


class MainWindow(QWidget, Ui_Form):
    def __init__(self):

        super().__init__()
        self.setupUi(self)



        self.pushButton.pressed.connect(self.start_progress)
        self.progressBar.setValue(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
    def start_progress(self):
        self.stackedWidget.setCurrentIndex(0)
        self.progress_value = 0
        self.timer.start(100)

    def update_progress(self):
        self.progress_value += (100/ 30000) * 100
        self.progressBar.setValue(int(self.progress_value))
        if self.progress_value >= 100:
            self.timer.stop()  # Stop the timer when the progress reaches 100




app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec()