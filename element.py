from valuesEnum import ValuesEnum

class Element:

    def __init__(self, value: ValuesEnum):
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value:ValuesEnum):
        self.value = value

    def getPic(self):
        pass

    def getPicScale(self):
        return 594/5

    def toString(self):
        pass

