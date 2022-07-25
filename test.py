import unittest
from unittest import mock
import main
import random


class TestStringManipulation(unittest.TestCase):

    def test_leave_only_consonants(self):
        self.assertEqual(main.leave_only_consonants('abbey road'), 'bbyrd', "Should be bbyrd")
        self.assertEqual(main.leave_only_consonants('abbey road!!!'), 'bbyrd', "Should be bbyrd")
        self.assertEqual(main.leave_only_consonants('a hard day\'s night'), 'hrddysnght', "Should be hrddysnght")

    def test_insert_spaces(self):
        #check there are no double (or more) spaces
        self.assertNotIn("  ", main.insert_spaces("hrddysnght"), "should not contain multiple spaces in a row")

        #TODO: how else can we test this (and create_questions_from_answers), given the randomness? 
        # Some of these tests may pass sometimes and fail others, based on the random placement of the spaces
        # Need to add mocking for random numbers

    # def test_create_questions_from_answers():
    #     pass

if __name__ == '__main__':
    unittest.main()