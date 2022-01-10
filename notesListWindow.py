# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerwnBFSh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from bar import Bar
from element import Element
from note import Note
from notesEnum import NotesEnum
from notesList import NotesList
from valuesEnum import ValuesEnum


class Ui_NotesListWindow(object):
    def setupUi(self, notesListWindow):
        if not notesListWindow.objectName():
            notesListWindow.setObjectName(u"notesListWindow")
        notesListWindow.setFixedSize(324/5*19, ((512+594)/5+50)*3)
        notesListWindow.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(Qt.Window)
        self.centralwidget = QWidget(notesListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 324/5*19, ((512+594)/5+50)*3))

        self.layoutForScrollArea = QHBoxLayout(self.centralwidget)
        # self.layoutForScrollArea.setGeometry(QRect(0, 0, 324/5*19, ((512+594)/5+50)*64))

        self.gridLayoutWidget = QScrollArea()
        self.gridLayoutWidget.setWidgetResizable(True)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 324/5*19, ((512+594)/5+50)*64))

        self.scrollAreaWidgetContents = QWidget()

        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayoutWidget.setWidget(self.scrollAreaWidgetContents)
        self.layoutForScrollArea.addWidget(self.gridLayoutWidget)


        # # notesListWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(notesListWindow)
        # self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 800, 22))
        # # notesListWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(notesListWindow)
        # self.statusbar.setObjectName(u"statusbar")
        # # notesListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(notesListWindow)

        # self.redraw()
        # self.clearLayout()
        # self.redraw()

        QMetaObject.connectSlotsByName(notesListWindow)
    # setupUi

    def clearLayout(self):
        for i in reversed(range(self.gridLayout.count())):
            self.gridLayout.itemAt(i).widget().setParent(None)

    def redraw(self, notesList: NotesList):

        self.clearLayout()

        row = 0
        col = 0
        for bar_1 in notesList.getNotesList():
            row, col = self.drawBar(bar_1, row, col)

        self.gridLayout.setRowStretch(row+3, 1)
        self.gridLayout.setColumnStretch(19, 1)

    def drawBar(self, bar: Bar, row: int, col: int):
        elements = bar.getElements()
        for element in elements:
            if(col > 17):
                col = 0
                row += 3

            if(col == 0):
                self.drawPic("D:/4_year/тест/pic/sign/alto_key.png", row, col, 594/5)
                self.drawPic("D:/4_year/тест/pic/sign/bass_key.png", row+1, col, 512/5)
                col+=1

            self.drawPic("D:/4_year/тест/pic/sign/alto_stan.png", row, col, 594/5)
            self.drawPic("D:/4_year/тест/pic/sign/bass_stan.png", row+1, col, 512/5)
            if(element.__class__.__name__ == "Note"):
                if(element.getOctave() < 4):
                    self.drawElement(element, row+1, col)
                else:
                    self.drawElement(element, row, col)
            else:
                self.drawElement(element, row, col)

            self.drawPic("", row+2, col, 512/5)

            col+=1

        if(bar.getFreeSpace() > 0):
            self.drawPic("", row, col, 594/5)
            self.drawPic("", row+1, col, 512/5)
            col+=1

        self.drawPic("D:/4_year/тест/pic/sign/alto_end.png", row, col, 594/5)
        self.drawPic("D:/4_year/тест/pic/sign/bass_end.png", row+1, col, 512/5)

        return [row, col + 1]

    def drawElement(self, element: Element, row: int, col: int):
        self.drawPic(element.getPic(), row, col, element.getPicScale())

    def drawPic(self, path, row: int, col: int, h_scale):
        pic = QLabel(self.gridLayoutWidget)
        pic.setPixmap(QPixmap(path).scaled(324/5, h_scale))
        self.gridLayout.addWidget(pic,row,col)

    def retranslateUi(self, notesListWindow):
        notesListWindow.setWindowTitle(QCoreApplication.translate("notesListWindow", u"notesListWindow", None))
    # retranslateUi

