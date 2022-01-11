from unittest import TestCase

from models.notesList import NotesList
from validators.notesListValidator import NotesListValidator


class TestNotesListValidator(TestCase):
    def test_is_notes_list_valid_1(self):
        notesList = NotesList(4, 4, 64)
        self.assertTrue(NotesListValidator.isNotesListValid(notesList))

    def test_is_notes_list_valid_2(self):
        notesList = NotesList(-1, 4, 64)
        self.assertFalse(NotesListValidator.isNotesListValid(notesList))

    def test_is_notes_list_valid_3(self):
        notesList = NotesList(4, 4, -64)
        self.assertFalse(NotesListValidator.isNotesListValid(notesList))

    def test_is_notes_list_valid_4(self):
        notesList = NotesList("f", 4, 64)
        self.assertFalse(NotesListValidator.isNotesListValid(notesList))

    def test_is_notes_list_valid_5(self):
        notesList = NotesList(4, 5, 64)
        self.assertFalse(NotesListValidator.isNotesListValid(notesList))

