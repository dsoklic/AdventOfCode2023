import unittest
import solutions.day13_part1 as part1
import solutions.day13_part2 as part2

class Testing(unittest.TestCase):
    def test_vertical(self):
        input = [
            '#.##..##.',
            '..#.##.#.',
            '##......#',
            '##......#',
            '..#.##.#.',
            '..##..##.',
            '#.#.##.#.'
        ]

        is_horizontal, line = part1.getMirrorLine(input)

        self.assertFalse(is_horizontal)
        self.assertEqual(line, 5)

    def test_horizontal(self):
        input = [
            '#...##..#',
            '#....#..#',
            '..##..###',
            '#####.##.',
            '#####.##.',
            '..##..###',
            '#....#..#'
        ]

        is_horizontal, line = part1.getMirrorLine(input)

        self.assertTrue(is_horizontal)
        self.assertEqual(line, 4)

    def test_differences(self):
        self.assertAlmostEqual(part2.countLineDifferences('#....#..#','#.##.#..#'), 2)
        self.assertAlmostEqual(part2.countLineDifferences('#.##.#..#','#.##.#..#'), 0)

if __name__ == '__main__':
    unittest.main()
