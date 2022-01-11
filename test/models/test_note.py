from unittest import TestCase

from models.note import Note
from models.notesEnum import NotesEnum
from models.valuesEnum import ValuesEnum


class TestNote(TestCase):

    def test_NoneParamAdd(self):
        note = Note(None, 4, None)
        self.assertEqual(note.value, ValuesEnum.whole)

    def test_transpose_up_without_octave_changed(self):
        note = Note(ValuesEnum.half, 4, NotesEnum.c)
        note.transposeUp(5)
        note1 = Note(ValuesEnum.half, 4, NotesEnum.f)
        self.assertEqual(note.octave, note1.octave)
        self.assertEqual(note.name, note1.name)

    def test_transpose_up_octave_changed(self):
        note = Note(ValuesEnum.half, 4, NotesEnum.b)
        note.transposeUp(5)
        note1 = Note(ValuesEnum.half, 5, NotesEnum.e)
        self.assertEqual(note.octave, note1.octave)
        self.assertEqual(note.name, note1.name)

    def test_transpose_up_semitones_over_bound(self):
        with self.assertRaises(Exception) as context:
            note = Note(ValuesEnum.half, 5, NotesEnum.f)
            note.transposeUp(5)
        self.assertTrue('Данную ноту можно транспонировать максимум на 0 полутонов вверх!' in str(context.exception))

    def test_findMaxCountOfSemitonesToTransposeUp_1(self):
        note = Note(ValuesEnum.half, 5, NotesEnum.f)
        self.assertEqual(note.findMaxCountOfSemitonesToTransposeUp(), 0)

    def test_findMaxCountOfSemitonesToTransposeUp_2(self):
        note = Note(ValuesEnum.half, 3, NotesEnum.b)
        self.assertEqual(note.findMaxCountOfSemitonesToTransposeUp(), 18)

    def test_findMaxCountOfSemitonesToTransposeUp_3(self):
        note = Note(ValuesEnum.half, 3, NotesEnum.e)
        self.assertEqual(note.findMaxCountOfSemitonesToTransposeUp(), 25)
