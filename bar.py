from element import Element

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

    def getFreeSpace(self):
        size = self.countOfBeats / self.valuesOfBeats
        for element in self.elements:
            size -= 1/element.getValue().value
        return size