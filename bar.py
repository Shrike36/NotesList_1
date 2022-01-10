from element import Element
from valuesEnum import ValuesEnum


class Bar:

    def __init__(self, countOfBeats: int, valueOfBeats: int):
        self.elements = []
        self.countOfBeats = countOfBeats
        self.valuesOfBeats = valueOfBeats

    def getElements(self):
        return self.elements

    def addElement(self, element: Element):
        if(self.getFreeSpace() >= 1/element.getValue().value):
            self.elements.append(element)
        else:
            raise Exception("Навозможно добавить к такту элемент заданной длительности!")

    def deleteElement(self, elementNumber: int, autoFillFlag: bool):
        if(elementNumber >= len(self.elements) or elementNumber < 0):
            raise Exception("Элемента с заданным номером в заданном такте не существует!")
        if(not autoFillFlag):
            self.elements.pop(elementNumber)
        else:
            self.elements.pop(elementNumber)
            if(len(self.elements) > 0):
                if(elementNumber == len(self.elements)):
                    elementNumber-=1
                self.autoFill(elementNumber)

    def getFreeSpace(self):
        size = self.countOfBeats / self.valuesOfBeats
        for element in self.elements:
            size -= 1/element.getValue().value
        return size

    def autoFill(self, elementNumber):
        self.elements[elementNumber].setValue(
            ValuesEnum(
                self.elements[elementNumber].getValue().value/2))