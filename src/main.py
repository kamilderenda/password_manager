from GUI_data import Window, QApplication


if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec()