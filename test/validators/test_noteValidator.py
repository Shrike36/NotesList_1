from unittest import TestCase

from models.note import Note
from models.notesEnum import NotesEnum
from models.valuesEnum import ValuesEnum
from validators.noteValidator import NoteValidator


class TestNoteValidator(TestCase):
    def test_validate_note(self):
        note = Note(ValuesEnum.half, 2, NotesEnum.a)
        self.assertTrue(NoteValidator.validateNote(note))

    def test_validate_note_1(self):
        note = Note(ValuesEnum.half, 1, NotesEnum.a)
        self.assertFalse(NoteValidator.validateNote(note))

    def test_validate_note_2(self):
        note = Note(ValuesEnum.half, 5, NotesEnum.b)
        self.assertFalse(NoteValidator.validateNote(note))
