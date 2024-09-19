import unittest
from challenge_function import f

class TestCountElements(unittest.TestCase):

    def test_string(self):
        return self.assertEqual(f("sstty"), {"s":  2, "t": 2, "y": 1})
    
    def test_numbers(self):
        return self.assertEqual(f("21242"), {"2":  3, "4": 1, "1": 1})
    
    def test_single_character(self):
        return self.assertEqual(f("a"), {"a": 1})

    def test_duplicate_characters(self):
        return self.assertEqual(f("aaaaa"), {"a": 5})

    def test_empty_string(self):
        return self.assertEqual(f(""), {})

    def test_special_characters(self):
        return self.assertEqual(f("@#$!@"), {"@":  2,  "#": 1, "!": 1, "$": 1})

    def test_string_list(self):
        return self.assertEqual(f(['s', 's', 'y', 't', 't']), {"s":  2, "t": 2, "y": 1})        

    def test_numbers_list(self):
        return self.assertEqual(f([2, 1, 2, 4, 2]), {2:  3, 4: 1, 1: 1})

    def test_string_set_with_duplicates(self):
        return self.assertEqual(f({'s', 's', 'y', 't', 't'}), {"s":  1, "t": 1, "y": 1})

if __name__ == '__main__':
    unittest.main()