from unittest import TestCase

from models.note import Note
from models.notesEnum import NotesEnum
from models.valuesEnum import ValuesEnum


class TestNote(TestCase):

    def test_NoneParamAdd(self):
        note = Note(None, 4, None)
        self.assertEqual(note.value, ValuesEnum.whole)

    def test_transpose_up(self):

        note = Note(ValuesEnum.half, 4, NotesEnum.c)
        note.transposeUp(5)
        note1 = Note(ValuesEnum.half, 4, NotesEnum.f)
        self.assertEqual(note.octave, note1.octave)
        self.assertEqual(note.name, note1.name)

        note = Note(ValuesEnum.half, 4, NotesEnum.b)
        note.transposeUp(5)
        note1 = Note(ValuesEnum.half, 5, NotesEnum.e)
        self.assertEqual(note.octave, note1.octave)
        self.assertEqual(note.name, note1.name)

        with self.assertRaises(Exception) as context:
            note = Note(ValuesEnum.half, 5, NotesEnum.f)
            note.transposeUp(5)
        self.assertTrue('Данную ноту можно транспонировать максимум на 0 полутонов вверх!' in str(context.exception))

    def test_findMaxCountOfSemitonesToTransposeUp(self):
        note = Note(ValuesEnum.half, 5, NotesEnum.f)
        self.assertEqual(note.findMaxCountOfSemitonesToTransposeUp(), 0)

        note = Note(ValuesEnum.half, 3, NotesEnum.b)
        self.assertEqual(note.findMaxCountOfSemitonesToTransposeUp(), 18)

        note = Note(ValuesEnum.half, 3, NotesEnum.e)
        self.assertEqual(note.findMaxCountOfSemitonesToTransposeUp(), 25)
