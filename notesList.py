from bar import Bar
from element import Element

class NotesList:

    def __init__(self, countOfBeats: int, valueOfBeats: int):
        self.notes_list = []
        self.countOfBeats = countOfBeats
        self.valuesOfBeats = valueOfBeats

    def getNotesList(self):
        return self.notes_list

    def addElementToTail(self, element: Element, autoFillFlag: bool):
        if(len(self.notes_list) == 0 or not self.notes_list[len(self.notes_list)-1].getFreeSpace()):
            if(len(self.notes_list) <= 64):
                self.notes_list.append(Bar(self.countOfBeats, self.valuesOfBeats))
            else:
                raise Exception("Невозможно создать больше 64 тактов!")
        elementNumber = len(self.notes_list[len(self.notes_list)-1].getElements())
        (self.notes_list[len(self.notes_list)-1]).addElement(element, elementNumber, autoFillFlag)
        if (len(self.notes_list[len(self.notes_list)-1].getElements()) == 0):
            self.notes_list.pop(len(self.notes_list)-1)

    def addElementToPosition(self, element: Element, barNumber: int, elementNumber: int, autoFillFlag: bool):
        if(barNumber >= len(self.notes_list) or barNumber < 0):
            raise Exception("Такта с заданным номером не существует!")
        (self.notes_list[barNumber]).addElement(element, elementNumber, autoFillFlag)

    def deleteLastElement(self, autoFillFlag: bool):
        if(not len(self.notes_list)):
            raise Exception("Элементы отсутствуют!")
        elementIndex = len(self.notes_list[len(self.notes_list)-1].getElements())-1
        self.notes_list[len(self.notes_list)-1].deleteElement\
            (elementIndex, autoFillFlag)
        if(not len(self.notes_list[len(self.notes_list)-1].getElements())):
            self.notes_list.pop(len(self.notes_list)-1)

    def deleteElementAtPosition(self, barNumber: int, elementNumber: int, autoFillFlag: bool):
        if(barNumber >= len(self.notes_list) or barNumber < 0):
            raise Exception("Такта с заданным номером не существует!")
        self.notes_list[barNumber].deleteElement(elementNumber, autoFillFlag)
        if(not len(self.notes_list[barNumber].getElements())):
            self.notes_list.pop(barNumber)

    def editElementOnPosition(self, element: Element, barNumber: int, elementNumber: int, autoFillFlag: bool):
        if(barNumber >= len(self.notes_list) or barNumber < 0):
            raise Exception("Такта с заданным номером не существует!")
        self.notes_list[barNumber].editElement(element, elementNumber, autoFillFlag)

    def addBar(self, bar: Bar):
        self.notes_list.append(bar)

    def toString(self):
        string = str(self.countOfBeats)
        string+="\n"
        string+=str(self.valuesOfBeats)
        string+="\n"
        for bar in self.notes_list:
            string+=bar.toString()
        return string
