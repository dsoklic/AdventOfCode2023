import unittest
from solutions.day04 import *

class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dummy_input = [
          'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
          'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
          'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
          'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
          'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
          'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
        ]

    def test_card_info(self):
        id, winners, actual = getCardInfo('Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19')

        self.assertEqual(id, 2)
        self.assertCountEqual(winners, [13, 32, 20, 16, 61])
        self.assertCountEqual(actual, [61, 30, 68, 82, 17, 32, 24, 19])

    def test_score(self):
        _, winners, actual = getCardInfo('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
        self.assertEqual(getScore(winners, actual), 8)

    def test_winning_numbers(self):
        _, winners, actual = getCardInfo('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
        matches = getWinningNumbers(winners, actual)
    
        self.assertCountEqual(matches, [48, 83, 86, 17])

    def test_part2(self):
        res = calculatePart2(self.dummy_input)
        self.assertEqual(res, 30)

if __name__ == '__main__':
    unittest.main()
