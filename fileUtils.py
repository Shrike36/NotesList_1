from bar import Bar
from note import Note
from notesEnum import NotesEnum
from notesList import NotesList
from rest import Rest
from valuesEnum import ValuesEnum


class FileUtils:

    @staticmethod
    def saveFile(path: str, notesList: NotesList):
        f = open(path, 'w')
        str = notesList.toString()
        f.write(str)
        f.close()

    @staticmethod
    def openFromFile(path: str):
        f = open(path, 'r')
        return FileUtils.parseNoteListFromString(f.readlines())

    @staticmethod
    def parseNoteListFromString(string:str):
        countOfBeats = int(string[0])
        valueOfBeats = int(string[1])
        notesList = NotesList(countOfBeats, valueOfBeats)

        for i in range(0, len(string)):
            # if not i.isspace():
            if(i>=len(string)):
                break
            string[i] = str(string[i]).replace('\n', '')
            if(str(string[i]) == ''):
                string.pop(i)
                i-=1

        for i in range(2, len(string)):
            if(string[i][0] == "["):
                pair = FileUtils.parseBarFromString(string, i+1, len(string), countOfBeats, valueOfBeats)
                bar = pair[0]
                i = pair[1]
                notesList.addBar(bar)
                i+=1

        return notesList

    @staticmethod
    def parseBarFromString(string:str, index: int, endIndex: int, countOfBeats: int, valueOfBeats: int):
        bar = Bar(countOfBeats, valueOfBeats)
        for i in range(index, endIndex):
            if (string[i] == "rest"):
                pair = FileUtils.parseRestFromString(string, i+1, endIndex)
                rest = pair[0]
                i = pair[1]
                bar.addElement(rest,len(bar.getElements()),False)
                i += 1
            elif (string[i] == "note"):
                pair = FileUtils.parseNoteFromString(string, i+1, endIndex)
                note = pair[0]
                i = pair[1]
                bar.addElement(note,len(bar.getElements()),False)
                i += 1
            elif (string[i] == "]"):
                return [bar, i]
        raise Exception("Невозможно считать данные из файла")

    @staticmethod
    def parseRestFromString(string:str, index: int, endIndex: int):
        value = None
        for i in range(index, endIndex):
            if (string[i] == "{"):
                i+=1
                value = ValuesEnum(int(string[i]))
            elif (string[i] == "}"):
                if (value != None):
                    return [Rest(value), i]
                else:
                    raise Exception("Невозможно считать данные из файла")
        raise Exception("Невозможно считать данные из файла")

    @staticmethod
    def parseNoteFromString(string:str, index: int, endIndex: int):
        value = None
        octave = None
        name = None

        for i in range(index, endIndex):
            if (string[i] == "{"):
                i+=1
                value = ValuesEnum(int(string[i]))
                i+=1
                octave = int(string[i])
                i+=1
                name = NotesEnum(int(string[i]))
            elif (string[i] == "}"):
                if (value != None and octave != None and name != None):
                    return [Note(value, octave, name), i]
                else:
                    raise Exception("Невозможно считать данные из файла")
        raise Exception("Невозможно считать данные из файла")