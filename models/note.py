from models.element import Element
from models.notesEnum import NotesEnum
from models.valuesEnum import ValuesEnum
# from validators.noteValidator import NoteValidator


class Note(Element):

    def __init__(self, value: ValuesEnum, octave: int, name: NotesEnum):
        super().__init__(value)
        self.octave = octave
        self.name = name

    def getName(self):
        return self.name

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

    def toString(self):
        string = "note"+"\n{\n"+\
              str(self.value.value)+"\n"+ \
              str(self.octave)+"\n"+ \
              str(self.name.value)+ \
              "\n}\n"
        return string

    def tramsposeUp(self, countOfSemitones):
        max = self.findMaxCountOfSemitonesToTransposeUp()
        max = max if max < 11 else 11
        if(max < countOfSemitones or countOfSemitones < 0 ):
            raise Exception("Данную ноту можно транспонировать максимум на "+str(max)+" полутонов вверх!")

        if (self.name.value + countOfSemitones > 12):
            self.octave+=1
            countOfSemitones = self.name.value + countOfSemitones - 12
            self.name = NotesEnum(countOfSemitones)
        else:
            self.name = NotesEnum(self.name.value + countOfSemitones)

    def findMaxCountOfSemitonesToTransposeUp(self):
        return (5*12+6) - (self.octave*12+self.name.value)