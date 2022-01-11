from unittest import TestCase

from models.bar import Bar
from models.note import Note
from models.notesEnum import NotesEnum
from models.rest import Rest
from models.valuesEnum import ValuesEnum


class TestBar(TestCase):

    def test_NoneParamAdd(self):
        bar = Bar(None, 8)
        self.assertEqual(bar.__getattribute__("countOfBeats"), 4)
        self.assertEqual(bar.__getattribute__("valuesOfBeats"), 4)

    def test_add_element_incorrect_position(self):
        bar = Bar(3, 4)

        with self.assertRaises(Exception) as context:
            bar.addElement(Rest(ValuesEnum.whole), 3, False)
        self.assertTrue('Невозможно добавить элемент на заданную позицию!' in str(context.exception))

    def test_add_element_incorrect_value(self):
        bar = Bar(3, 4)
        with self.assertRaises(Exception) as context:
            bar.addElement(Rest(ValuesEnum.whole), 0, False)
        self.assertTrue('Невозможно добавить к такту элемент заданной длительности!' in str(context.exception))

    def test_add_element_auto_fill(self):
        bar = Bar(3, 4)
        bar.addElement(Rest(ValuesEnum.whole),0,True)
        self.assertEqual(bar.getElements()[0].getValue(), ValuesEnum.half)
        self.assertEqual(bar.getElements()[1].getValue(), ValuesEnum.quarter)


    def test_delete_element_incorrect_position(self):
        bar = Bar(3, 4)
        with self.assertRaises(Exception) as context:
            bar.deleteElement(3, False)
        self.assertTrue('Элемента с заданным номером в заданном такте не существует!' in str(context.exception))

    def test_delete_element_without_auto_fill(self):
        bar = Bar(3, 4)
        bar.addElement(Rest(ValuesEnum.whole),0,True)
        bar.deleteElement(0,False)
        self.assertEqual(bar.getElements()[0].getValue(), ValuesEnum.quarter)

    def test_delete_element_auto_fill(self):
        bar = Bar(3, 4)
        bar.addElement(Rest(ValuesEnum.whole),0,True)
        bar.deleteElement(0,False)
        bar.deleteElement(0,True)
        self.assertEqual(bar.getElements()[0].getValue(), ValuesEnum.half)
        self.assertEqual(bar.getElements()[1].getValue(), ValuesEnum.quarter)

    def test_edit_element_incorrect_position(self):
        bar = Bar(3, 4)
        with self.assertRaises(Exception) as context:
            bar.deleteElement(3, False)
        self.assertTrue('Элемента с заданным номером в заданном такте не существует!' in str(context.exception))

    def test_edit_element_without_auto_fill(self):
        bar = Bar(3, 4)
        bar.addElement(Rest(ValuesEnum.whole),0,True)
        element = Note(ValuesEnum.eighth, 4, NotesEnum.a)
        bar.editElement(element,1,False)
        self.assertEqual(bar.getElements()[1].getName(), NotesEnum.a)

    def test_edit_element_auto_fill(self):
        bar = Bar(3, 4)
        bar.addElement(Rest(ValuesEnum.whole),0,True)
        element = Note(ValuesEnum.eighth, 4, NotesEnum.a)
        bar.editElement(element,1,True)
        self.assertEqual(bar.getElements()[1].getValue(), ValuesEnum.quarter)

    def test_get_free_space(self):
        bar = Bar(10, 4)
        bar.addElement(Rest(ValuesEnum.whole),0,False)
        bar.addElement(Rest(ValuesEnum.quarter),1,False)
        bar.addElement(Note(ValuesEnum.half, 5, NotesEnum.c),2,False)
        self.assertEqual(bar.getFreeSpace(), 10/4-1-1/4-1/2)

    def test_auto_fill(self):
        bar = Bar(10, 4)
        bar.addElement(Rest(ValuesEnum.whole),0,False)
        bar.addElement(Rest(ValuesEnum.quarter),1,False)
        bar.addElement(Note(ValuesEnum.half, 5, NotesEnum.c),2,False)
        bar.addElement(Note(ValuesEnum.eighth, 5, NotesEnum.c),3,False)

        bar.autoFill(Note(ValuesEnum.eighth, 3, NotesEnum.f),3)

        self.assertEqual(bar.getElements()[3].getValue(), ValuesEnum.half)
        self.assertEqual(bar.getElements()[4].getValue(), ValuesEnum.eighth)

        self.assertEqual(bar.getElements()[3].getName(), NotesEnum.f)
        self.assertEqual(bar.getElements()[4].getName(), NotesEnum.f)


    def test_transpose_up(self):
        bar = Bar(4, 4)
        bar.addElement(Note(ValuesEnum.quarter, 4, NotesEnum.b),0,False)
        bar.addElement(Note(ValuesEnum.quarter, 4, NotesEnum.a),1,False)
        bar.addElement(Note(ValuesEnum.quarter, 3, NotesEnum.c),2,False)
        bar.transposeUp(1)

        self.assertEqual(bar.getElements()[0].getOctave(), 5)
        self.assertEqual(bar.getElements()[1].getOctave(), 4)

        self.assertEqual(bar.getElements()[0].getName(), NotesEnum.c)
        self.assertEqual(bar.getElements()[1].getName(), NotesEnum.ash)

    def test_transpose_up_semitones_over_bound(self):
        bar = Bar(4, 4)
        bar.addElement(Note(ValuesEnum.quarter, 4, NotesEnum.b),0,False)
        bar.addElement(Note(ValuesEnum.quarter, 4, NotesEnum.a),1,False)
        bar.addElement(Note(ValuesEnum.quarter, 3, NotesEnum.c),2,False)
        with self.assertRaises(Exception) as context:
            bar.transposeUp(10)
        self.assertTrue('Данный список нот можно транспонировать максимум на 6 полутонов вверх!' in str(context.exception))

    def test_find_max_count_of_semitones_to_transpose_up(self):
        bar = Bar(4, 4)
        bar.addElement(Note(ValuesEnum.quarter, 5, NotesEnum.c),0,False)
        bar.addElement(Note(ValuesEnum.quarter, 4, NotesEnum.a),1,False)
        bar.addElement(Note(ValuesEnum.quarter, 4, NotesEnum.c),2,False)
        bar.addElement(Rest(ValuesEnum.quarter),3,False)
        self.assertEqual(bar.findMaxCountOfSemitonesToTransposeUp(), 5)



