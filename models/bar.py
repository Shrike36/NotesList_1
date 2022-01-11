from models.element import Element
from models.valuesEnum import ValuesEnum
import copy

class Bar:
    def __init__(self, countOfBeats: int, valueOfBeats: int):
        self.elements = []
        if(countOfBeats == None or valueOfBeats == None):
            self.countOfBeats = 4
            self.valuesOfBeats = 4
        else:
            self.countOfBeats = countOfBeats
            self.valuesOfBeats = valueOfBeats

    def getElements(self):
        return self.elements

    def addElement(self, element: Element, elementNumber: int, autoFillFlag: bool):
        if(elementNumber >= len(self.elements)+1 or elementNumber < 0):
            raise Exception("Невозможно добавить элемент на заданную позицию!")
        if(not autoFillFlag):
            if(self.getFreeSpace() >= 1/element.getValue().value):
                self.elements.insert(elementNumber, element)
            else:
                raise Exception("Невозможно добавить к такту элемент заданной длительности!")
        else:
            self.autoFill(element, elementNumber)

    def deleteElement(self, elementNumber: int, autoFillFlag: bool):
        if(elementNumber >= len(self.elements) or elementNumber < 0):
            raise Exception("Элемента с заданным номером в заданном такте не существует!")
        elementToFill = self.elements.pop(elementNumber)
        if(autoFillFlag):
            self.autoFill(elementToFill, elementNumber)

    def editElement(self, element: Element, elementNumber: int, autoFillFlag: bool):
        if(elementNumber >= len(self.elements) or elementNumber < 0):
            raise Exception("Элемента с заданным номером в заданном такте не существует!")
        self.elements.pop(elementNumber)
        if(not autoFillFlag):
            self.addElement(element, elementNumber, False)
        else:
            self.autoFill(element, elementNumber)

    def getFreeSpace(self):
        size = self.countOfBeats / self.valuesOfBeats
        for element in self.elements:
            size -= 1/element.getValue().value
        return size

    def autoFill(self, elementToFill: Element, elementNumber: int):
        freeSpace = self.getFreeSpace()

        while(freeSpace != 0):
            for value in ValuesEnum:
                if(freeSpace - 1/value.value >= 0):
                    elementToFill.setValue(value)
                    newElement = copy.deepcopy(elementToFill)
                    self.elements.insert(elementNumber, newElement)
                    elementNumber+=1
                    freeSpace -= 1/value.value
                    break

    def toString(self):
        str = "[\n"
        for element in self.elements:
            str+=element.toString()
        str+="]\n"
        return str

    def transposeUp(self, countOfSemitones: int):
        max = self.findMaxCountOfSemitonesToTransposeUp()
        max = max if max < 11 else 11
        if(max < countOfSemitones or countOfSemitones < 0 ):
            raise Exception("Данный список нот можно транспонировать максимум на "+str(max)+" полутонов вверх!")
        for element in self.elements:
            if(element.__class__.__name__ == "Note"):
                element.transposeUp(countOfSemitones)

    def findMaxCountOfSemitonesToTransposeUp(self):
        min = 1000
        for element in self.elements:
            barMin = 10000
            if(element.__class__.__name__ == "Note"):
                barMin = element.findMaxCountOfSemitonesToTransposeUp()
            if(barMin <= min):
                min = barMin
        return min

    def transposeDown(self, countOfSemitones: int):
        max = self.findMaxCountOfSemitonesToTransposeDown()
        max = max if max < 11 else 11
        if(max < countOfSemitones or countOfSemitones < 0 ):
            raise Exception("Данный список нот можно транспонировать максимум на "+str(max)+" полутонов вниз!")
        for element in self.elements:
            if(element.__class__.__name__ == "Note"):
                element.transposeDown(countOfSemitones)

    def findMaxCountOfSemitonesToTransposeDown(self):
        min = 1000
        for element in self.elements:
            barMin = 10000
            if(element.__class__.__name__ == "Note"):
                barMin = element.findMaxCountOfSemitonesToTransposeDown()
            if(barMin <= min):
                min = barMin
        return min