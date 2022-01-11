from unittest import TestCase

from models.note import Note
from models.notesEnum import NotesEnum
from models.notesList import NotesList
from models.rest import Rest
from models.valuesEnum import ValuesEnum


class TestNotesList(TestCase):

    def test_NoneParamAdd(self):
        notesList = NotesList(None, 8, 64)
        self.assertEqual(notesList.__getattribute__("countOfBeats"), 4)
        self.assertEqual(notesList.__getattribute__("valuesOfBeats"), 4)

    def test_add_element_to_tail_over_bounds(self):
        notesList = NotesList(4, 4, 64)
        for i in range(0, 64):
            notesList.addElementToTail(Rest(ValuesEnum.whole), False)
        with self.assertRaises(Exception) as context:
            notesList.addElementToTail(Rest(ValuesEnum.whole), False)
        self.assertTrue('Невозможно создать больше 64 тактов!' in str(context.exception))

    def test_add_element_to_tail_incorrect_element_value(self):
        notesList = NotesList(3, 4, 64)
        with self.assertRaises(Exception) as context:
            notesList.addElementToTail(Rest(ValuesEnum.whole), False)
        self.assertTrue('Невозможно добавить к такту элемент заданной длительности!' in str(context.exception))

    def test_add_element_to_tail_one_auto_another_not(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), True)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)

        self.assertEqual(len(notesList.getNotesList()), 2)
        self.assertTrue(notesList.getNotesList()[1].getFreeSpace())

    def test_find_max_count_of_semitones_to_transpose_up(self):
        notesList = NotesList(4, 4, 64)
        notesList.addElementToTail(Note(ValuesEnum.half, 3, NotesEnum.b),False)
        notesList.addElementToTail(Note(ValuesEnum.half, 4, NotesEnum.b),False)
        notesList.addElementToTail(Note(ValuesEnum.whole, 5, NotesEnum.dsh),False)
        self.assertEqual(2, notesList.findMaxCountOfSemitonesToTransposeUp())

    def test_transpose_up_over_bound(self):
        notesList = NotesList(4, 4, 64)
        notesList.addElementToTail(Note(ValuesEnum.half, 3, NotesEnum.b),False)
        notesList.addElementToTail(Note(ValuesEnum.half, 4, NotesEnum.b),False)
        notesList.addElementToTail(Note(ValuesEnum.whole, 5, NotesEnum.dsh),False)
        with self.assertRaises(Exception) as context:
            notesList.transposeUp(10)
        self.assertTrue('Данный список нот можно транспонировать максимум на 2 полутонов вверх!' in str(context.exception))

    def test_add_bar_over_bounds(self):
        notesList = NotesList(4, 4, 64)
        for i in range(0, 64):
            notesList.addElementToTail(Rest(ValuesEnum.whole), False)
        with self.assertRaises(Exception) as context:
            notesList.addElementToTail(Rest(ValuesEnum.whole), False)
        self.assertTrue('Невозможно создать больше 64 тактов!' in str(context.exception))

    def test_add_element_to_position_incorrect_position(self):
        notesList = NotesList(3, 4, 64)
        with self.assertRaises(Exception) as context:
            notesList.addElementToPosition(Rest(ValuesEnum.whole), 3, 3, False)
        self.assertTrue('Такта с заданным номером не существует!' in str(context.exception))

    def test_add_element_to_position_incorrect_value(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.half), False)
        with self.assertRaises(Exception) as context:
            notesList.addElementToPosition(Rest(ValuesEnum.whole), 0, 0, False)
        self.assertTrue('Невозможно добавить к такту элемент заданной длительности!' in str(context.exception))

    def test_add_element_to_position_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.addElementToPosition(Rest(ValuesEnum.sixteenth), 0, 0, True)
        self.assertEqual(notesList.getNotesList()[0].getElements()[0].getValue(), ValuesEnum.half)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getValue(), ValuesEnum.quarter)

    def test_delete_last_element_no_elements(self):
        notesList = NotesList(3, 4, 64)
        with self.assertRaises(Exception) as context:
            notesList.deleteLastElement(False)
        self.assertTrue('Элементы отсутствуют!' in str(context.exception))

    def test_delete_last_element_without_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.addElementToTail(Rest(ValuesEnum.half), False)
        notesList.deleteLastElement(False)
        self.assertEqual(len(notesList.getNotesList()[0].getElements()), 1)
        self.assertEqual(notesList.getNotesList()[0].getFreeSpace(), 3/4-1/4)

    def test_delete_last_element_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.addElementToTail(Rest(ValuesEnum.half), False)
        notesList.deleteLastElement(True)
        self.assertEqual(len(notesList.getNotesList()[0].getElements()), 2)
        self.assertEqual(notesList.getNotesList()[0].getFreeSpace(), 0)

    def test_edit_element_on_position_incorrect_position(self):
        notesList = NotesList(3, 4, 64)
        with self.assertRaises(Exception) as context:
            notesList.editElementOnPosition(Rest(ValuesEnum.quarter), 1, 0, False)
        self.assertTrue('Такта с заданным номером не существует!' in str(context.exception))

    def test_edit_element_without_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.addElementToTail(Rest(ValuesEnum.sixteenth), False)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.editElementOnPosition(Note(ValuesEnum.eighth, 4, NotesEnum.c), 0, 1, False)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getValue(), ValuesEnum.eighth)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getName(), NotesEnum.c)

    def test_edit_element_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.sixteenth), False)
        notesList.addElementToTail(Rest(ValuesEnum.eighth), False)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.editElementOnPosition(Note(ValuesEnum.eighth, 4, NotesEnum.c), 0, 0, True)
        self.assertEqual(notesList.getNotesList()[0].getElements()[0].getValue(), ValuesEnum.quarter)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getValue(), ValuesEnum.eighth)
        self.assertEqual(notesList.getNotesList()[0].getElements()[0].getName(), NotesEnum.c)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getName(), NotesEnum.c)

    def test_delete_element_at_position_incorrect_position(self):
        notesList = NotesList(3, 4, 64)
        with self.assertRaises(Exception) as context:
            notesList.deleteElementAtPosition(1, 0, False)
        self.assertTrue('Такта с заданным номером не существует!' in str(context.exception))

    def test_delete_element_at_position_without_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.sixteenth), False)
        notesList.addElementToTail(Rest(ValuesEnum.eighth), False)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.deleteElementAtPosition(0, 0, False)
        self.assertEqual(len(notesList.getNotesList()[0].getElements()), 2)
        self.assertEqual(notesList.getNotesList()[0].getElements()[0].getValue(), ValuesEnum.eighth)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getValue(), ValuesEnum.quarter)

    def test_delete_element_at_position_without_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.sixteenth), False)
        notesList.addElementToTail(Rest(ValuesEnum.eighth), False)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.deleteElementAtPosition(0, 0, False)
        self.assertEqual(len(notesList.getNotesList()[0].getElements()), 2)
        self.assertEqual(notesList.getNotesList()[0].getElements()[0].getValue(), ValuesEnum.eighth)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getValue(), ValuesEnum.quarter)

    def test_delete_element_at_position_auto_fill(self):
        notesList = NotesList(3, 4, 64)
        notesList.addElementToTail(Rest(ValuesEnum.sixteenth), False)
        notesList.addElementToTail(Rest(ValuesEnum.eighth), False)
        notesList.addElementToTail(Rest(ValuesEnum.quarter), False)
        notesList.deleteElementAtPosition(0, 0, True)
        self.assertEqual(len(notesList.getNotesList()[0].getElements()), 4)
        self.assertEqual(notesList.getNotesList()[0].getElements()[0].getValue(), ValuesEnum.quarter)
        self.assertEqual(notesList.getNotesList()[0].getElements()[1].getValue(), ValuesEnum.eighth)



