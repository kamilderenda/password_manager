from uuid import uuid4
import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PySide6.QtCore import QTimer
from UI.Pform import Ui_Form
from src.GUI_data import Window as AppWindow
from src.face_recognition import predict, create_model, get_image
from src.db import DBControl


class MainWindow(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = DBControl(Path(__file__).parent.parent / 'db.json')
        self.model = create_model()
        self.pushButton.pressed.connect(self.start_progress)
        self.progressBar.setValue(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0

    def start_progress(self):
        self.stackedWidget.setCurrentIndex(0)
        self.progress_value = 0
        self.timer.start(100)
        image = get_image()
        # mozna do innego watku!
        # res = predict(image, self.model)
        res = 1
        print(res)
        if res:
            # trzeba przeslac dane(id do okna)
            # self.destroy()
            wd = AppWindow(res)
            wd.show()
        else:
            user_id = self.db.add_user(str(uuid4()))
            new_path = Path(__file__).parent.parent / 'assets' / f'{user_id}.jpg'
            image.save(str(new_path))
            # dodac zwracanie
            # self.destroy()
            wd = AppWindow(user_id)
            wd.show()

    def update_progress(self):
        self.progress_value += (100 / 10000) * 100
        self.progressBar.setValue(int(self.progress_value))
        if self.progress_value >= 100:
            self.timer.stop()


app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec()
