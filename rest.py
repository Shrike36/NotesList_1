from element import Element
from valuesEnum import ValuesEnum


class Rest(Element):

    def __init__(self, value: ValuesEnum):
        super().__init__(value)

    def getPic(self):
        return "D:/4_year/тест/pic/pause/alto/"+ \
               str(self.value.value)+".png"