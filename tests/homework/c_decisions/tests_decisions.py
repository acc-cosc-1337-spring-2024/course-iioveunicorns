#
import unittest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating


class test_config(unittest.TestCase):
    
    def test_get_options_ratio_1(self):
        self.assertEqual(get_options_ratio(5, 20), 0.25)
    
    def test_get_options_ratio_2(self):
        self.assertEqual(get_options_ratio(10, 20), 0.5)

    def test_get_faculty_rating_1(self):
        self.assertEqual(get_faculty_rating(0.91), 'Excellent')

    def test_get_faculty_rating_2(self):
        self.assertEqual(get_faculty_rating(0.85), 'Very Good')

    def test_get_faculty_rating_3(self):
        self.assertEqual(get_faculty_rating(0.71), 'Good')

    def test_get_faculty_rating_4(self):
        self.assertEqual(get_faculty_rating(0.66), 'Needs Improvement')

    def test_get_faculty_rating_5(self):
        self.assertEqual(get_faculty_rating(0.45), 'Unacceptable')