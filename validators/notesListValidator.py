from models.notesList import NotesList


class NotesListValidator:

    countOfBeats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    valuesOfBeats = [1, 2, 4, 8, 16]

    @staticmethod
    def isNotesListValid(notesList: NotesList):
        return notesList.__getattribute__("countOfBeats") in NotesListValidator.countOfBeats \
               and notesList.__getattribute__("valueOfBeats") in NotesListValidator.valueOfBeats \
               and notesList.__getattribute__("maxBarcount")>0


