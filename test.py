import unittest
import main

class TestStringManipulation(unittest.TestCase):

    def test_leave_only_consonants(self):
        self.assertEqual(main.leave_only_consonants('abbey road'), 'bbyrd', "Should be bbyrd")
        self.assertEqual(main.leave_only_consonants('abbey road!!!'), 'bbyrd', "Should be bbyrd")
        self.assertEqual(main.leave_only_consonants('a hard day\'s night'), 'hrddysnght', "Should be hrddysnght")

    def test_insert_spaces(self):
        #check input and output are not the same
        self.assertNotEqual(main.insert_spaces('bbyrd'), 'bbyrd', "string should always be modified")
        #check the output contains spaces
        self.assertIn(" ", main.insert_spaces("hrddysnght"), "should contain at least one space")
        #TODO: how else can we test this, given the randomness?

if __name__ == '__main__':
    unittest.main()