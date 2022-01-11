from models.element import Element
from models.note import Note

class NoteValidator:

    notesInterval = [2*12+6, 5*12+6]

    @staticmethod
    def validateNote(note : Note):
        noteHigh = note.getOctave()*12+note.getName().value
        return noteHigh > NoteValidator.notesInterval[0] and noteHigh < NoteValidator.notesInterval[1]