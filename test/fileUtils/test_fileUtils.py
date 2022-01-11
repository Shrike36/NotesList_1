from unittest import TestCase

from models.note import Note
from models.notesEnum import NotesEnum
from models.notesList import NotesList
from models.rest import Rest
from models.valuesEnum import ValuesEnum
from utils.fileUtils import FileUtils


class TestFileUtils(TestCase):
    def test_save_file(self):
        notesList = NotesList(4,4,64)
        rest = Rest(ValuesEnum.whole)
        note = Note(ValuesEnum.whole, 4, NotesEnum.c)
        notesList.addElementToTail(rest, False)
        notesList.addElementToTail(note, False)

        FileUtils.saveFile("D:/4_year/тест/NotesList_1/1.ns", notesList)

        f = open("D:/4_year/тест/NotesList_1/1.ns", 'r')
        str1 = f.read()
        str2 = notesList.toString()
        f.close()

        self.assertEqual(str1, str2)

    def test_open_from_file(self):
        notesList = NotesList(4,4,64)
        rest = Rest(ValuesEnum.whole)
        note = Note(ValuesEnum.whole, 4, NotesEnum.c)
        notesList.addElementToTail(rest, False)
        notesList.addElementToTail(note, False)
        FileUtils.saveFile("D:/4_year/тест/NotesList_1/1.ns", notesList)

        notesList1 = FileUtils.openFromFile("D:/4_year/тест/NotesList_1/1.ns")

        self.assertEqual(len(notesList.getNotesList()), len(notesList1.getNotesList()))
