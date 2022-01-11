from element import Element
from valuesEnum import ValuesEnum
import copy


class Bar:
    def __init__(self, countOfBeats: int, valueOfBeats: int):
        self.elements = []
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
                raise Exception("Навозможно добавить к такту элемент заданной длительности!")
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
