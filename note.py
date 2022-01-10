from element import Element
from notesEnum import NotesEnum
from valuesEnum import ValuesEnum


class Note(Element):

    def __init__(self, value: ValuesEnum, octave: int, name: NotesEnum):
        super().__init__(value)
        self.octave = octave
        self.name = name

    def getPic(self):
        return "D:/4_year/тест/pic/note/"+\
               str(self.octave)+"/"+\
               str(self.value.value)+"/"+\
               (str(NotesEnum(self.name).name))[0]+".png"

    def getPicScale(self):
        if(self.octave < 4):
            return 512/5
        return 594/5

    def getOctave(self):
        return self.octave