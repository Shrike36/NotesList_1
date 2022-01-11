# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeroQTuGg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import copy

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from notesList import NotesList


class Ui_CreateNewNotesListWindow(object):
    def setupUi(self, CreateNewNotesListWindow):
        if not CreateNewNotesListWindow.objectName():
            CreateNewNotesListWindow.setObjectName(u"CreateNewNotesListWindow")
        CreateNewNotesListWindow.setFixedSize(800, 600)
        CreateNewNotesListWindow.setWindowFlags(Qt.Window)
        self.centralwidget = QWidget(CreateNewNotesListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.countOfBeatsComboBox = QComboBox(self.centralwidget)
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.addItem("")
        self.countOfBeatsComboBox.setObjectName(u"countOfBeatsComboBox")
        self.countOfBeatsComboBox.setGeometry(QRect(2*220, 2*20, 2*71, 2*22))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.countOfBeatsComboBox.setFont(font)
        self.vlaueOfBeatsComboBox = QComboBox(self.centralwidget)
        self.vlaueOfBeatsComboBox.addItem("")
        self.vlaueOfBeatsComboBox.addItem("")
        self.vlaueOfBeatsComboBox.addItem("")
        self.vlaueOfBeatsComboBox.addItem("")
        self.vlaueOfBeatsComboBox.setObjectName(u"vlaueOfBeatsComboBox")
        self.vlaueOfBeatsComboBox.setGeometry(QRect(2*220,2*50, 2*71, 2*22))
        self.vlaueOfBeatsComboBox.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(2*20, 2*20, 2*181, 2*21))
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(2*20, 2*50, 2*171, 2*21))
        self.label_2.setFont(font)

        self.createPshButton = QPushButton(self.centralwidget)
        self.createPshButton.setObjectName(u"createPshButton")
        self.createPshButton.setGeometry(QRect(2*20, 2*90, 2*75, 2*23))
        self.createPshButton.setFont(font)
        self.createPshButton.clicked.connect(self.createPshButtonClicked)

        self.retranslateUi(CreateNewNotesListWindow)

        QMetaObject.connectSlotsByName(CreateNewNotesListWindow)
    # setupUi

    def createPshButtonClicked(self):

        self.parent().__setattr__("prevNotesList", copy.deepcopy(self.parent().__getattribute__("notesList")))
        self.parent().__setattr__("countOfBeats", self.countOfBeatsComboBox.currentData())
        self.parent().__setattr__("valueOfBeats", self.vlaueOfBeatsComboBox.currentData())
        self.parent().__setattr__("notesList", NotesList(
            self.countOfBeatsComboBox.currentData(),
            self.vlaueOfBeatsComboBox.currentData()))


        self.parent().__setattr__("countOfBeats", self.countOfBeatsComboBox.currentData())
        self.parent().__setattr__("valueOfBeats", self.vlaueOfBeatsComboBox.currentData())

        self.parent().__getattribute__("countOfBeastLlabel").setText(str(self.countOfBeatsComboBox.currentData()))
        self.parent().__getattribute__("valueOfBeatLlabel").setText(str(self.vlaueOfBeatsComboBox.currentData()))


        if (self.parent().__getattribute__("notesListWindow") == None):
            self.parent().openNotesListWindow()
        self.parent().__getattribute__("notesListWindow").redraw(self.parent().__getattribute__("notesList"))

        self.hide()

    def retranslateUi(self, CreateNewNotesListWindow):
        CreateNewNotesListWindow.setWindowTitle(QCoreApplication.translate("CreateNewNotesListWindow", u"CreateNewNotesListWindow", None))
        self.countOfBeatsComboBox.setItemText(0, QCoreApplication.translate("CreateNewNotesListWindow", u"1", None))
        self.countOfBeatsComboBox.setItemText(1, QCoreApplication.translate("CreateNewNotesListWindow", u"2", None))
        self.countOfBeatsComboBox.setItemText(2, QCoreApplication.translate("CreateNewNotesListWindow", u"3", None))
        self.countOfBeatsComboBox.setItemText(3, QCoreApplication.translate("CreateNewNotesListWindow", u"4", None))
        self.countOfBeatsComboBox.setItemText(4, QCoreApplication.translate("CreateNewNotesListWindow", u"5", None))
        self.countOfBeatsComboBox.setItemText(5, QCoreApplication.translate("CreateNewNotesListWindow", u"6", None))
        self.countOfBeatsComboBox.setItemText(6, QCoreApplication.translate("CreateNewNotesListWindow", u"7", None))
        self.countOfBeatsComboBox.setItemText(7, QCoreApplication.translate("CreateNewNotesListWindow", u"8", None))
        self.countOfBeatsComboBox.setItemText(8, QCoreApplication.translate("CreateNewNotesListWindow", u"9", None))
        self.countOfBeatsComboBox.setItemText(9, QCoreApplication.translate("CreateNewNotesListWindow", u"10", None))
        self.countOfBeatsComboBox.setItemText(10, QCoreApplication.translate("CreateNewNotesListWindow", u"11", None))
        self.countOfBeatsComboBox.setItemText(11, QCoreApplication.translate("CreateNewNotesListWindow", u"12", None))
        self.countOfBeatsComboBox.setItemText(12, QCoreApplication.translate("CreateNewNotesListWindow", u"13", None))
        self.countOfBeatsComboBox.setItemText(13, QCoreApplication.translate("CreateNewNotesListWindow", u"14", None))
        self.countOfBeatsComboBox.setItemText(14, QCoreApplication.translate("CreateNewNotesListWindow", u"15", None))
        self.countOfBeatsComboBox.setItemData(0, 1)
        self.countOfBeatsComboBox.setItemData(1, 2)
        self.countOfBeatsComboBox.setItemData(2, 3)
        self.countOfBeatsComboBox.setItemData(3, 4)
        self.countOfBeatsComboBox.setItemData(4, 5)
        self.countOfBeatsComboBox.setItemData(5, 6)
        self.countOfBeatsComboBox.setItemData(6, 7)
        self.countOfBeatsComboBox.setItemData(7, 8)
        self.countOfBeatsComboBox.setItemData(8, 9)
        self.countOfBeatsComboBox.setItemData(9, 10)
        self.countOfBeatsComboBox.setItemData(10, 11)
        self.countOfBeatsComboBox.setItemData(11, 12)
        self.countOfBeatsComboBox.setItemData(12, 13)
        self.countOfBeatsComboBox.setItemData(13, 14)
        self.countOfBeatsComboBox.setItemData(14, 15)


        self.vlaueOfBeatsComboBox.setItemText(0, QCoreApplication.translate("CreateNewNotesListWindow", u"1", None))
        self.vlaueOfBeatsComboBox.setItemText(1, QCoreApplication.translate("CreateNewNotesListWindow", u"1/2", None))
        self.vlaueOfBeatsComboBox.setItemText(2, QCoreApplication.translate("CreateNewNotesListWindow", u"1/4", None))
        self.vlaueOfBeatsComboBox.setItemText(3, QCoreApplication.translate("CreateNewNotesListWindow", u"1/8", None))
        self.vlaueOfBeatsComboBox.setItemData(0, 1)
        self.vlaueOfBeatsComboBox.setItemData(1, 2)
        self.vlaueOfBeatsComboBox.setItemData(2, 4)
        self.vlaueOfBeatsComboBox.setItemData(3, 8)

        self.label.setText(QCoreApplication.translate("CreateNewNotesListWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043e\u043b\u0435\u0439 \u0432 \u0442\u0430\u043a\u0442\u0435", None))
        self.label_2.setText(QCoreApplication.translate("CreateNewNotesListWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0430\u043a\u0442\u043e\u0432\u043e\u0439 \u0434\u043e\u043b\u0438", None))
        self.createPshButton.setText(QCoreApplication.translate("CreateNewNotesListWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

