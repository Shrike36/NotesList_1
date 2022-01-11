from models.bar import Bar
from models.element import Element

class NotesList:

    def __init__(self, countOfBeats: int, valueOfBeats: int, maxBarCount: int):
        self.notes_list = []
        if(countOfBeats == None or valueOfBeats == None or maxBarCount == None):
            self.countOfBeats = 4
            self.valuesOfBeats = 4
            self.maxBarcount = 64
        else:
            self.countOfBeats = countOfBeats
            self.valuesOfBeats = valueOfBeats
            self.maxBarcount = maxBarCount

    def getNotesList(self):
        return self.notes_list

    def addElementToTail(self, element: Element, autoFillFlag: bool):
        if(len(self.notes_list) == 0 or not self.notes_list[len(self.notes_list)-1].getFreeSpace()):
            if(len(self.notes_list) < self.maxBarcount):
                self.notes_list.append(Bar(self.countOfBeats, self.valuesOfBeats))
            else:
                raise Exception("Невозможно создать больше "+str(self.maxBarcount)+" тактов!")
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
        if(len(self.notes_list) >= self.maxBarcount):
            raise Exception("Невозможно создать больше "+str(self.maxBarcount)+" тактов!")
        self.notes_list.append(bar)

    def toString(self):
        string = str(self.countOfBeats)
        string+="\n"
        string+=str(self.valuesOfBeats)
        string+="\n"
        for bar in self.notes_list:
            string+=bar.toString()
        return string

    def transposeUp(self, countOfSemitones: int):
        max = self.findMaxCountOfSemitonesToTransposeUp()
        max = max if max < 11 else 11
        if(max < countOfSemitones or countOfSemitones < 0):
            raise Exception("Данный список нот можно транспонировать максимум на "+str(max)+" полутонов вверх!")
        for bar in self.notes_list:
            bar.transposeUp(countOfSemitones)

    def findMaxCountOfSemitonesToTransposeUp(self):
        min = 1000
        for bar in self.notes_list:
            barMin = bar.findMaxCountOfSemitonesToTransposeUp()
            if(barMin <= min):
                min = barMin
        return min

    def transposeDown(self, countOfSemitones: int):
        max = self.findMaxCountOfSemitonesToTransposeDown()
        max = max if max < 11 else 11
        if(max < countOfSemitones or countOfSemitones < 0):
            raise Exception("Данный список нот можно транспонировать максимум на "+str(max)+" полутонов dybp!")
        for bar in self.notes_list:
            bar.transposeDown(countOfSemitones)

    def findMaxCountOfSemitonesToTransposeDown(self):
        min = 1000
        for bar in self.notes_list:
            barMin = bar.findMaxCountOfSemitonesToTransposeDown()
            if(barMin <= min):
                min = barMin
        return min
