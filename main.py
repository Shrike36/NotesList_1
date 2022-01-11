import sys
from PyQt5 import QtWidgets

from windows.MainWindow import Ui_MainWindow


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if(not 15):
    print("hui1")

if(15):
    print("hui15")

if(0):
    print("hui0")

app = QtWidgets.QApplication([])
app.setStyle('Fusion')
application = mywindow()
application.show()

sys.exit(app.exec())

# class GridLayout_Example(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.build_widgets()
#         self.build_layout()
#
#         self.resize(640, 480)
#
#     def build_widgets(self):
#         self.btn_country_63 = QPushButton(
#             text="Country", styleSheet="background-color:red;color:white"
#         )
#         self.btn_country_63.setFixedSize(100, 25)
#
#         self.btn_state_63 = QPushButton(
#             text="State", styleSheet="background-color:red;color:white"
#         )
#         self.btn_state_63.setFixedSize(100, 25)
#
#         self.btn_district_63 = QPushButton(
#             text="District", styleSheet="background-color:red;color:white"
#         )
#         self.btn_district_63.setFixedSize(100, 25)
#
#         self.btn_town_63 = QPushButton(
#             text="Town", styleSheet="background-color:red;color:white"
#         )
#         self.btn_town_63.setFixedSize(60, 75)
#
#         self.btn_town_64 = QPushButton(
#             text="Town", styleSheet="background-color:red;color:white"
#         )
#         self.btn_town_64.setFixedSize(60, 75)
#
#
#         self.btn_town_65 = QPushButton(
#             text="Town", styleSheet="background-color:red;color:white"
#         )
#         self.btn_town_65.setFixedSize(60, 75)
#
#         self.btn_bank_63 = QPushButton(
#             text="Bank", styleSheet="background-color:red;color:white"
#         )
#         self.btn_bank_63.setFixedSize(100, 25)
#
#         self.btn_zip_63 = QPushButton(
#             text="Zip Code", styleSheet="background-color:red;color:white"
#         )
#         self.btn_zip_63.setFixedSize(100, 25)
#
#     def build_layout(self):
#         self.container = QFrame()
#         self.container.setStyleSheet("background-color: lightgreen")
#
#         grid_layout = QGridLayout(self.container)
#         grid_layout.addWidget(self.btn_country_63, 0, 0, 1, 1)
#         grid_layout.addWidget(self.btn_state_63, 1, 0, 1, 1)
#         grid_layout.addWidget(self.btn_district_63, 0, 1, 1, 1)
#         grid_layout.addWidget(self.btn_town_63, 0, 2, 3, 1)
#         grid_layout.addWidget(self.btn_bank_63, 1, 3, 1, 1)
#         grid_layout.addWidget(self.btn_zip_63, 2, 4, 1, 1)
#         grid_layout.addWidget(self.btn_town_64, 0, 5, 3, 1)
#         grid_layout.addWidget(self.btn_town_65, 0, 6, 3, 1)
#         grid_layout.setColumnStretch(7, 1)
#         grid_layout.setSpacing(0)
#         grid_layout.setContentsMargins(0, 0, 0, 0)
#
#         lay = QVBoxLayout(self)
#         lay.addWidget(self.container)
#         self.container.setFixedHeight(self.container.sizeHint().height())
#
#
# def main():
#     app = QApplication(sys.argv)
#     print("default-style: ", app.style().metaObject().className())
#     app.setStyle("fusion")
#     mainwindow = GridLayout_Example()
#     mainwindow.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     main()


# from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
#                              QHBoxLayout, QVBoxLayout, QMainWindow)
# from PyQt5.QtCore import Qt, QSize
# from PyQt5 import QtWidgets
# import sys
#
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
#         self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
#         self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
#
#         for i in range(1,50):
#             object = QLabel("TextLabel")
#             self.vbox.addWidget(object)
#
#         self.widget.setLayout(self.vbox)
#
#         #Scroll Area Properties
#         self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
#         self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.scroll.setWidgetResizable(True)
#         self.scroll.setWidget(self.widget)
#
#         self.setCentralWidget(self.scroll)
#
#         self.setGeometry(600, 100, 1000, 900)
#         self.setWindowTitle('Scroll Area Demonstration')
#         self.show()
#
#         return
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()