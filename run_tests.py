import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_decisions
has the test functions
'''
from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)

#from tests.homework.c_decisions import tests_decisions

unittest.TextTestRunner(verbosity=2).run(suite)
