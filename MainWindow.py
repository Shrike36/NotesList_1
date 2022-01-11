################################################################################
## Form generated from reading UI file 'untitledJLbDdW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from bar import Bar
from createNewNotesListWindow import Ui_CreateNewNotesListWindow
from element import Element
from fileUtils import FileUtils
from note import Note
from notesEnum import NotesEnum
from notesList import NotesList
from rest import Rest
from valuesEnum import ValuesEnum
import copy
from notesListWindow import Ui_NotesListWindow

class NotesListW(QWidget, Ui_NotesListWindow):                          # +++
    def __init__(self, parent=None):
        super(NotesListW, self).__init__(parent)
        self.setupUi(self)

class CreateNewNotesListW(QWidget, Ui_CreateNewNotesListWindow):                          # +++
    def __init__(self, parent=None):
        super(CreateNewNotesListW, self).__init__(parent)
        self.setupUi(self)

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(2*658, 2*245)

        self.create = QAction(MainWindow)
        self.create.setObjectName(u"create")
        self.save = QAction(MainWindow)
        self.save.setObjectName(u"save")
        self.undo = QAction(MainWindow)
        self.undo.setObjectName(u"undo")
        self.open = QAction(MainWindow)
        self.open.setObjectName(u"open")

        self.create.triggered.connect(self.createNewNotesListWindow)
        self.save.triggered.connect(self.saveFile)
        self.open.triggered.connect(self.openFromFile)
        self.undo.triggered.connect(self.undoPressed)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(2*10, 2*20, 2*191, 2*16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(2*10, 2*40, 2*211, 2*16))
        self.label_2.setFont(font)
        self.valueOfBeatLlabel = QLabel(self.centralwidget)
        self.valueOfBeatLlabel.setObjectName(u"valueOfBeatLlabel")
        self.valueOfBeatLlabel.setGeometry(QRect(2*230, 2*40, 2*21, 2*16))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.valueOfBeatLlabel.setFont(font1)
        self.countOfBeastLlabel = QLabel(self.centralwidget)
        self.countOfBeastLlabel.setObjectName(u"countOfBeastLlabel")
        self.countOfBeastLlabel.setGeometry(QRect(2*230, 2*20, 2*21, 2*16))
        self.countOfBeastLlabel.setFont(font1)
        self.addRadioButton = QRadioButton(self.centralwidget)
        self.addRadioButton.setObjectName(u"addRadioButton")
        self.addRadioButton.setGeometry(QRect(2*10, 2*90, 2*101, 2*18))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.addRadioButton.setFont(font2)
        self.editRadioButton = QRadioButton(self.centralwidget)
        self.editRadioButton.setObjectName(u"editRadioButton")
        self.editRadioButton.setGeometry(QRect(2*10, 2*110, 2*141, 2*18))
        self.editRadioButton.setFont(font2)
        self.deleteRadioButton = QRadioButton(self.centralwidget)
        self.deleteRadioButton.setObjectName(u"deleteRadioButton")
        self.deleteRadioButton.setGeometry(QRect(2*10, 2*130, 2*101, 2*18))
        self.deleteRadioButton.setFont(font2)
        self.valueComboBox = QComboBox(self.centralwidget)
        self.valueComboBox.addItem("")
        self.valueComboBox.addItem("")
        self.valueComboBox.addItem("")
        self.valueComboBox.addItem("")
        self.valueComboBox.addItem("")
        self.valueComboBox.setObjectName(u"valueComboBox")
        self.valueComboBox.setGeometry(QRect(2*360, 2*20, 2*81, 2*20))
        font3 = QFont()
        font3.setPointSize(8)
        self.valueComboBox.setFont(font3)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(2*270, 2*20, 2*91, 2*20))
        self.label_5.setFont(font2)

        self.savePushButton = QPushButton(self.centralwidget)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(2*270, 2*170, 2*81, 2*23))
        self.savePushButton.setFont(font2)
        self.savePushButton.clicked.connect(self.savePushButtonClicked)

        self.barNumberLineEdit = QLineEdit(self.centralwidget)
        self.barNumberLineEdit.setObjectName(u"barNumberLineEdit")
        self.barNumberLineEdit.setGeometry(QRect(2*580, 2*20, 2*71, 2*20))
        self.barNumberLineEdit.setValidator(QIntValidator(1, 64, self))

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(2*480, 2*20, 2*81, 2*20))
        self.label_6.setFont(font2)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(2*280, 2*120, 2*91, 2*20))
        self.label_7.setFont(font2)
        self.octaveComboBox = QComboBox(self.centralwidget)
        self.octaveComboBox.addItem("")
        self.octaveComboBox.addItem("")
        self.octaveComboBox.addItem("")
        self.octaveComboBox.addItem("")
        self.octaveComboBox.setObjectName(u"octaveComboBox")
        self.octaveComboBox.setGeometry(QRect(2*360, 2*120, 2*81, 2*20))
        self.octaveComboBox.setFont(font3)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(2*280, 2*90, 2*91, 2*20))
        self.label_8.setFont(font2)
        self.noteComboBox = QComboBox(self.centralwidget)
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.addItem("")
        self.noteComboBox.setObjectName(u"noteComboBox")
        self.noteComboBox.setGeometry(QRect(2*360, 2*90, 2*81, 2*20))
        self.noteComboBox.setFont(font3)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(2*480, 2*50, 2*121, 2*20))
        self.label_9.setFont(font2)

        self.elementNumberLineEdit = QLineEdit(self.centralwidget)
        self.elementNumberLineEdit.setObjectName(u"elementNumberLineEdit")
        self.elementNumberLineEdit.setGeometry(QRect(2*580, 2*50, 2*71, 2*20))
        self.elementNumberLineEdit.setValidator(QIntValidator(1, 90, self))

        self.deletePushButton = QPushButton(self.centralwidget)
        self.deletePushButton.setObjectName(u"deletePushButton")
        self.deletePushButton.setGeometry(QRect(2*360, 2*170, 2*81, 2*23))
        self.deletePushButton.setFont(font2)
        self.deletePushButton.clicked.connect(self.deletePushButtonClicked)

        self.autoFillCheckBox = QCheckBox(self.centralwidget)
        self.autoFillCheckBox.setObjectName(u"autoFillCheckBox")
        self.autoFillCheckBox.setGeometry(QRect(2*10, 2*170, 2*211, 2*16))
        self.autoFillCheckBox.setFont(font2)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 2*70, 2*671, 2*20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 2*150, 2*671, 2*20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(2*250, 2*0, 2*20, 2*221))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(2*450, 2*0, 2*20, 2*221))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.countOfSemitonesLineEdit = QLineEdit(self.centralwidget)
        self.countOfSemitonesLineEdit.setObjectName(u"countOfSemitonesLineEdit")
        self.countOfSemitonesLineEdit.setGeometry(QRect(2*580, 2*90, 2*71, 2*20))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(2*480, 2*90, 2*81, 2*20))
        self.label_12.setFont(font2)
        self.transposeUpPushButton = QPushButton(self.centralwidget)
        self.transposeUpPushButton.setObjectName(u"transposeUpPushButton")
        self.transposeUpPushButton.setGeometry(QRect(2*480, 2*120, 2*81, 2*23))
        self.transposeUpPushButton.setFont(font2)
        self.transposeDownPushButton = QPushButton(self.centralwidget)
        self.transposeDownPushButton.setObjectName(u"transposeDownPushButton")
        self.transposeDownPushButton.setGeometry(QRect(2*570, 2*120, 2*81, 2*23))
        self.transposeDownPushButton.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(2*0, 2*0, 2*658, 2*22))
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        self.fixMenu = QMenu(self.menubar)
        self.fixMenu.setObjectName(u"fixMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.fixMenu.menuAction())
        self.fileMenu.addAction(self.create)
        self.fileMenu.addAction(self.save)
        self.fileMenu.addAction(self.open)
        self.fixMenu.addAction(self.undo)

        self.retranslateUi(MainWindow)

        self.countOfBeats = 4
        self.valueOfBeats = 4

        self.notesList = NotesList(self.countOfBeats, self.valueOfBeats)
        self.prevNotesList = NotesList(self.countOfBeats, self.valueOfBeats)

        self.notesListWindow = NotesListW(self)
        self.notesListWindow.show()

        self.createNewNotesListWindow = None

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def openFromFile(self):
        self.prevNotesList = copy.deepcopy(self.notesList)

        try:
            filename, filetype = QFileDialog.getOpenFileName(self,
                                                             "Выбрать файл",
                                                             ".",
                                                             "(*.ns)")
            notesList = FileUtils.openFromFile(filename)
            if(notesList != None):
                self.notesList = notesList
                self.countOfBeats = self.notesList.__getattribute__("countOfBeats")
                self.valueOfBeats = self.notesList.__getattribute__("valuesOfBeats")
                self.countOfBeastLlabel.setText(str(self.countOfBeats))
                self.valueOfBeatLlabel.setText(str(self.valueOfBeats))

        except Exception as ex:
            QMessageBox.critical(self, "Ошибка ", "Невозможно считать данные из файла", QMessageBox.Ok)

        if (self.notesListWindow == None):
            self.openNotesListWindow()
        self.notesListWindow.redraw(self.notesList)

    def saveFile(self):
        try:
            filename, ok = QFileDialog.getSaveFileName(self,
                                                       "Сохранить файл",
                                                       ".",
                                                       "(*.ns)")
            FileUtils.saveFile(filename, self.notesList)
        except Exception as ex:
            QMessageBox.critical(self, "Ошибка ", "Невозможно сохранить в файл", QMessageBox.Ok)

    def createNewNotesListWindow(self):
        self.createNewNotesListWindow = CreateNewNotesListW(self)
        self.createNewNotesListWindow.show()


    def undoPressed(self):
        tmp = copy.deepcopy(self.prevNotesList)
        self.prevNotesList = copy.deepcopy(self.notesList)
        self.notesList = tmp
        self.countOfBeats = self.notesList.__getattribute__("countOfBeats")
        self.valueOfBeats = self.notesList.__getattribute__("valuesOfBeats")
        self.countOfBeastLlabel.setText(str(self.countOfBeats))
        self.valueOfBeatLlabel.setText(str(self.valueOfBeats))
        if (self.notesListWindow == None):
            self.openNotesListWindow()
        self.notesListWindow.redraw(self.notesList)

    def openNotesListWindow(self):
        self.notesListWindow = NotesListW(self)
        self.notesListWindow.show()

    def deletePushButtonClicked(self):
        if(self.deleteRadioButton.isChecked()):
            self.prevNotesList = copy.deepcopy(self.notesList)
            autoFillFlag = self.autoFillCheckBox.isChecked()
            if(self.barNumberLineEdit.text() and self.elementNumberLineEdit.text()):
                barNumber = int(self.barNumberLineEdit.text())
                elementNumber = int(self.elementNumberLineEdit.text())
                try:
                    self.notesList.deleteElementAtPosition(barNumber - 1, elementNumber - 1, autoFillFlag)
                except Exception as ex:
                    QMessageBox.critical(self, "Ошибка ", str(ex), QMessageBox.Ok)
            else:
                try:
                    self.notesList.deleteLastElement(autoFillFlag)
                except Exception as ex:
                    QMessageBox.critical(self, "Ошибка ", str(ex), QMessageBox.Ok)

            if (self.notesListWindow == None):
                self.openNotesListWindow()
            self.notesListWindow.redraw(self.notesList)

    def savePushButtonClicked(self):
        # sender = self.sender()
        # bar = Bar()
        self.prevNotesList = copy.deepcopy(self.notesList)

        note = self.noteComboBox.currentData()
        autoFillFlag = self.autoFillCheckBox.isChecked()
        if(note > 0):
            value = ValuesEnum(self.valueComboBox.currentData())
            octave = int(self.octaveComboBox.currentText())
            note_name = NotesEnum(note)
            element = Note(value, octave, note_name)
        else:
            value = ValuesEnum(self.valueComboBox.currentData())
            element = Rest(value)

        if(self.addRadioButton.isChecked()):

            if(self.barNumberLineEdit.text() and self.elementNumberLineEdit.text()):
                barNumber = int(self.barNumberLineEdit.text())-1
                elementNumber = int(self.elementNumberLineEdit.text())-1
                try:
                    self.notesList.addElementToPosition(element, barNumber, elementNumber, autoFillFlag)
                except Exception as ex:
                    QMessageBox.critical(self, "Ошибка ", str(ex), QMessageBox.Ok)
            else:
                try:
                    self.notesList.addElementToTail(element, autoFillFlag)
                except Exception as ex:
                    QMessageBox.critical(self, "Ошибка ", str(ex), QMessageBox.Ok)

        elif (self.editRadioButton.isChecked()):
            if(self.barNumberLineEdit.text() and self.elementNumberLineEdit.text()):
                barNumber = int(self.barNumberLineEdit.text())-1
                elementNumber = int(self.elementNumberLineEdit.text())-1
                try:
                    self.notesList.editElementOnPosition(element, barNumber, elementNumber, autoFillFlag)
                except Exception as ex:
                    QMessageBox.critical(self, "Ошибка ", str(ex), QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Ошибка ", "Не указан элемент для редактирования!", QMessageBox.Ok)

        if (self.notesListWindow == None):
            self.openNotesListWindow()
        self.notesListWindow.redraw(self.notesList)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.create.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.undo.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043e\u043b\u0435\u0439 \u0432 \u0442\u0430\u043a\u0442\u0435:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0442\u0430\u043a\u0442\u043e\u0432\u043e\u0439 \u0434\u043e\u043b\u0438:", None))
        self.valueOfBeatLlabel.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.countOfBeastLlabel.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.addRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.addRadioButton.setChecked(True)
        self.editRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.deleteRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.valueComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043b\u0430\u044f", u"1"))
        self.valueComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0432\u0438\u043d\u0430", u"2"))
        self.valueComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0442\u0430\u044f", u"4"))
        self.valueComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u044c\u043c\u0430\u044f", u"8"))
        self.valueComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0428\u0435\u0441\u0442\u043d\u0430\u0434\u0446\u0430\u0442\u0430\u044f", u"16"))
        self.valueComboBox.setItemData(0, 1)
        self.valueComboBox.setItemData(1, 2)
        self.valueComboBox.setItemData(2, 4)
        self.valueComboBox.setItemData(3, 8)
        self.valueComboBox.setItemData(4, 16)

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0430\u043a\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0442\u0430\u0432\u0430", None))
        self.octaveComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.octaveComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.octaveComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.octaveComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"5", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0442\u0430", None))
        self.noteComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0443\u0437\u0430", None))
        self.noteComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u043e", None))
        self.noteComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0414\u043e \u0434\u0438\u0435\u0437", None))
        self.noteComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0420\u0435", None))
        self.noteComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0420\u0435 \u0434\u0438\u0435\u0437", None))
        self.noteComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041c\u0438", None))
        self.noteComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0424\u0430", None))
        self.noteComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0424\u0430 \u0434\u0438\u0435\u0437", None))
        self.noteComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043b\u044c", None))
        self.noteComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043b\u044c \u0434\u0438\u0435\u0437", None))
        self.noteComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041b\u044f", None))
        self.noteComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041b\u044f \u0434\u0438\u0435\u0437", None))
        self.noteComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"\u0421\u0438", None))
        self.noteComboBox.setItemData(0, 0)
        self.noteComboBox.setItemData(1, 1)
        self.noteComboBox.setItemData(2, 2)
        self.noteComboBox.setItemData(3, 3)
        self.noteComboBox.setItemData(4, 4)
        self.noteComboBox.setItemData(5, 5)
        self.noteComboBox.setItemData(6, 6)
        self.noteComboBox.setItemData(7, 7)
        self.noteComboBox.setItemData(8, 8)
        self.noteComboBox.setItemData(9, 9)
        self.noteComboBox.setItemData(10, 10)
        self.noteComboBox.setItemData(11, 11)
        self.noteComboBox.setItemData(12, 12)


        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430", None))
        self.deletePushButton.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.autoFillCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0442\u043e\u043d\u044b", None))
        self.transposeUpPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.transposeDownPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.fixMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

