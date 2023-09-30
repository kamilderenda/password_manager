import sys
from PySide6.QtWidgets import QApplication
# from UI.GUI_login import MainWindow
from src.GUI_data import Window

app = QApplication(sys.argv)
window = Window(1)
window.show()
app.exec()
