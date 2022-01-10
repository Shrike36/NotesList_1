from bar import Bar
from element import Element


class NotesList:

    def __init__(self, countOfBeats: int, valueOfBeats: int):
        self.notes_list = []
        self.countOfBeats = countOfBeats
        self.valuesOfBeats = valueOfBeats

    def getNotesList(self):
        return self.notes_list

    def addElement(self, element: Element):
        if(len(self.notes_list) == 0 or not self.notes_list[len(self.notes_list)-1].getFreeSpace()):
            if(len(self.notes_list) <= 64):
                self.notes_list.append(Bar(self.countOfBeats, self.valuesOfBeats))
            else:
                raise Exception("Невозможно создать больше 64 тактов!")
        (self.notes_list[len(self.notes_list)-1]).addElement(element)

    def deleteElement(self, barNumber: int, elementNumber: int, autoFillFlag: bool):
        if(barNumber >= len(self.notes_list)):
            raise Exception("Такта с заданным номером не существует!")
        self.notes_list[barNumber].deleteElement(elementNumber, autoFillFlag)
        if(not len(self.notes_list[barNumber].getElements())):
            self.notes_list.pop(barNumber)

    def addBar(self, bar: Bar):
        self.notes_list.append(bar)