from pathlib import Path
from PySide6.QtGui import Qt, QIcon, QFont, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QListWidgetItem, QListWidget, QPushButton
from UI.Data import Ui_Form
from UI.Manager import Ui_MainWindow
from UI.DialogInfo import Ui_Form as DialogInfo
from src.db import DBControl


class Data(QWidget, Ui_Form):
    """
    Widget which is stored in ListWidgets, contains USERNAME, PASSWORD, SITENAME, and 3 buttons:
    DELETE_BUTTON, OVERRIDE_BUTTON, HIDE_PASSWORD_BUTTON
    """

    def __init__(self, main, user_id, db: DBControl):
        super().__init__()
        self.user_id = user_id
        self.db = db
        self.setupUi(self)
        self.main = main     # injecting main window, just to have connection between self.
        self.item = QListWidgetItem()
        self._password = None
        self.label_password.setText("---SECURED---")

        self.bt_hide.setCheckable(True)

        self.bt_del.pressed.connect(self.delete)
        self.bt_hide.pressed.connect(self.hide)
        self.bt_change.pressed.connect(self.change)


    def hide(self):
        if not self.bt_hide.isChecked():
            self.label_password.setText(self._password)
        else:
            self.label_password.setText("---SECURED---")

    def change(self):
        dialog = InputDialog(self.main.user_id)
        if dialog.password or dialog.name or dialog.site:
            old_name = self.label_site.text()
            self.label_password.setText(dialog.password)
            self.label_mail.setText(dialog.name)
            self.label_site.setText(dialog.site)
            self.db.modify_password(self.user_id, old_name, self.label_site.text(), dialog.name, dialog.password)
            self.db.save()

    def delete(self):
        self.main.l_widget.takeItem(self.main.l_widget.row(self.item))
        self.db.delete_password(self.user_id, self.label_site.text())
        self.db.save()


class InputDialog(QDialog, DialogInfo):

    def __init__(self, index):
        super().__init__()
        self.setupUi(self)
        self.name = None
        self.password = None
        self.site = None
        self.to_add = False

        self.le_site.setStyleSheet("background-color: white;")
        self.le_password.setStyleSheet("background-color: white;")
        self.le_user.setStyleSheet("background-color: white;")

        self.bt_save.pressed.connect(self.accept)
        self.bt_cancel.pressed.connect(self.close)
        self.exec()

    def accept(self):
        if self.le_site.text() or self.le_user.text() or self.le_password.text():
            self.to_add = True
            self.site = self.le_site.text()
            self.name = self.le_user.text()
            self.password = self.le_password.text()
            self.close()


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id: int):
        super().__init__()
        self.user_id = user_id
        self.db = DBControl(Path(__file__).parent.parent / 'db.json')
        self.setupUi(self)
        self.bt_add.pressed.connect(self.add_item)
        self.container = []
        self.dynamic_load()
        self.setWindowTitle("Your Password Database")
        self.setup_header()

    def add_item(self):
        dialog = InputDialog(self.user_id)
        if dialog.to_add:
            self.db.add_password(self.user_id, dialog.name, dialog.password, dialog.site)
            self.db.save()
            self._new_item(dialog.site, dialog.name, dialog.password)

    def _new_item(self, site, mail, password):
        data = Data(self, self.user_id, self.db)
        data.label_mail.setText(mail)
        data.label_site.setText(site)
        data._password = password
        self.l_widget.addItem(data.item)
        data.item.setSizeHint(data.sizeHint())
        self.l_widget.setItemWidget(data.item, data)
        self.update()

    def dynamic_load(self):
        items = self.db.retrieve_passwords(self.user_id)
        self.container.extend(items)
        print(self.container)
        for i in self.container:
            _pass = i['password']
            _site = i['website']
            _name = i['login']
            print(_pass)
            self._new_item(_site, _name, _pass)

    def setup_header(self):
        image = f"../assets/{self.user_id}.jpg"
        username = self.db.data[str(self.user_id)]['username']
        self.label_2.setText(username)
        self.label.setPixmap(QPixmap(image))
        self.label.setScaledContents(True)
