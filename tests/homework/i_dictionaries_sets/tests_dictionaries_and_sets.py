#
import unittest
from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog2_not_prog_1, get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog1_or_prog2, prog1Set, prog2Set

class Test_Config(unittest.TestCase):

    def test_studentsWhoTookBoth(self):
        self.assertSetEqual({'Student3'}, get_students_who_took_prog1_and_prog2(prog1Set, prog2Set))
        
    def test_StudentsWhoTookEither(self):
        self.assertSetEqual({'Student1', 'Student2', 'Student3', 'Student4', 'Student5'}, get_students_who_took_prog1_or_prog2(prog1Set, prog2Set))

    def test_StudentsWhoTookProg1Only(self):
        self.assertSetEqual({'Student1', 'Student2'}, get_students_who_took_prog1_not_prog_2(prog1Set, prog2Set))

    def test_studentsWhoTookProg2Only(self):
        self.assertSetEqual({'Student4', 'Student5'}, get_students_who_took_prog2_not_prog_1(prog1Set, prog2Set))
