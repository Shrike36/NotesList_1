from bar import Bar
from element import Element


class NotesList:

    def __init__(self, countOfBeats: int, valueOfBeats: int):
        self.notes_list = []
        self.countOfBeats = countOfBeats
        self.valuesOfBeats = valueOfBeats

    def getNotesList(self):
        return self.notes_list

    def addElement(self, element: Element):
        if(len(self.notes_list) == 0 or not self.notes_list[len(self.notes_list)-1].getFreeSpace()):
            self.notes_list.append(Bar(self.countOfBeats, self.valuesOfBeats))
        (self.notes_list[len(self.notes_list)-1]).addElement(element)


    def addBar(self, bar: Bar):
        self.notes_list.append(bar)