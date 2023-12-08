import unittest
from solutions.day07 import *

class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dummy_input = [
            '32T3K 765',
            'T55J5 684',
            'KK677 28',
            'KTJJT 220',
            'QQQJA 483'
        ]

    def test_parseInput(self):
        expected = [
            ('32T3K', 765),
            ('T55J5', 684),
            ('KK677', 28),
            ('KTJJT', 220),
            ('QQQJA', 483)
        ]

        self.assertCountEqual(parseInput(self.dummy_input), expected)

    def test_hasPair(self):
        hand = '32T3K'
        self.assertTrue(hasPair(hand))

    def test_hasTwoPairs(self):
        hand = '3AA31'
        self.assertTrue(hasTwoPairs(hand))
        

    def test_hasThreeOfAKind(self):
        hand = 'AT3TT'
        self.assertTrue(hasThreeOfAKind(hand))
        

    def test_hasFullHouse(self):
        hand = 'A33A3'
        self.assertTrue(hasFullHouse(hand))
        

    def test_hasFourOfAKind(self):
        hand = '33233'
        self.assertTrue(hasFourOfAKind(hand))
        

    def test_hasFiveOfAKind(self):
        hand = '55555'
        self.assertTrue(hasFiveOfAKind(hand))
        
    def test_compareHands(self):
        self.assertGreater(compareHands('AAAAA', '392TA'), 0)
        self.assertEqual(compareHands('AAAAA', 'AAAAA'), 0)
        self.assertGreater(compareHands('77888', '77788'), 0)

    def test_sorted(self):
        expected = [
            '32T3K',
            'KTJJT',
            'KK677',
            'T55J5',
            'QQQJA'
        ]

        sorted = sortLines(parseInput(self.dummy_input))
        actual = [a for a,_ in sorted]

        self.assertListEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
