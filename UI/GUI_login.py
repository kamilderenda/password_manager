from uuid import uuid4
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PySide6.QtCore import QTimer
from UI.Pform import Ui_Form
from src.GUI_data import Window as AppWindow
#from src.face_recognition import predict, create_model, get_image
from src.db import DBControl


class MainWindow(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = DBControl(Path(__file__).parent.parent / 'db.json')
        #self.model = create_model()
        self.pushButton.pressed.connect(self.start_progress)
        self.progressBar.setValue(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0

    def start_progress(self):
        self.stackedWidget.setCurrentIndex(0)
        self.progress_value = 0
        self.timer.start(100)
        #res = predict(get_image(), self.model)
        wd = AppWindow(1)
        wd.show()


    def update_progress(self):
        self.progress_value += (100/ 10000) * 100
        self.progressBar.setValue(int(self.progress_value))
        if self.progress_value >= 100:
            self.timer.stop()


app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec()
