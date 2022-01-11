from models.element import Element
from models.valuesEnum import ValuesEnum


class Rest(Element):

    def __init__(self, value: ValuesEnum):
        super().__init__(value)

    def getPic(self):
        return "D:/4_year/тест/pic/pause/alto/"+ \
               str(self.value.value)+".png"

    def toString(self):
        string = "rest"+"\n{\n"+str(self.value.value)+"\n}\n"
        return string