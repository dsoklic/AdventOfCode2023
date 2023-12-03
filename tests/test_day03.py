import unittest
from solutions.day03 import *

class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dummy_input = [
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..'
        ]

    def test_all_numbers(self):
        self.assertEqual(len(getAllNumbers(self.dummy_input)), 10)

    def test_only_parts(self):
        parts = getPartNumbers(self.dummy_input)
        self.assertEqual(len(parts), 8)
        self.assertCountEqual(parts, (467, 35, 633, 617, 592, 755, 664, 598))

    def test_gears(self):
        gears = getAllGears(self.dummy_input)
        self.assertCountEqual(gears, ((3, 1), (3, 4), (5, 8)))

    def test_gear_pairs(self):
        gears = getAllGears(self.dummy_input)
        numbers  = getAllNumbers(self.dummy_input)

        pairs = getPairsNextToGears(numbers, gears)
        self.assertEqual(len(pairs), 2)

if __name__ == '__main__':
    unittest.main()
