from dev.Game import Game
import unittest


class TestGame(unittest.TestCase):

    def testNoThrows(self):
        g = Game()
        self.assertEqual(0, g.getScore())

    def testOneThrow(self):
        g = Game()
        g.add(5)
        self.assertEqual(5, g.getScore())

    def testTwoThrows(self):
        g = Game()
        g.add(5)
        g.add(4)
        self.assertEqual(9, g.getScore())

    def testSpareOneThrow(self):
        g = Game()
        g.add(7)
        g.add(3)
        g.add(4)
        self.assertEqual(18, g.getScore())

    def testSpareTwoThrows(self):
        g = Game()
        g.add(7)
        g.add(3)
        g.add(4)
        g.add(2)
        self.assertEqual(20, g.getScore())

    def testStrikeOneThrow(self):
        g = Game()
        g.add(10)
        g.add(4)
        self.assertEqual(18, g.getScore())

    def testStrikeTwoThrows(self):
        g = Game()
        g.add(10)
        g.add(4)
        g.add(3)
        self.assertEqual(24, g.getScore())

    def testSpareAndStrike(self):
        g = Game()
        g.add(4)
        g.add(6)
        g.add(10)
        self.assertEqual(30, g.getScore())

    def testOneThrowAfterSpareAndStrike(self):
        g = Game()
        g.add(4)
        g.add(6)
        g.add(10)
        g.add(6)
        self.assertEqual(42, g.getScore())

    def testTwoThrowsAfterSpareAndStrike(self):
        g = Game()
        g.add(4)
        g.add(6)
        g.add(10)
        g.add(6)
        g.add(2)
        self.assertEqual(46, g.getScore())

    def testTenthFrameSpareStatus(self):
        g = Game()
        points = [
            1, 2,
            3, 4,
            5, 2,
            4, 3,
            4, 4,
            1, 6,
            7, 2,
            5, 4,
            3, 3,
            4, 6
        ]
        for p in points:
            g.add(p)
        self.assertEqual(None, g.frames[9].getResult())

    def testTenthFrameTwoThrows(self):
        g = Game()
        points = [
            1, 2,
            3, 4,
            5, 2,
            4, 3,
            4, 4,
            1, 6,
            7, 2,
            5, 4,
            3, 3,
            4, 3
        ]
        for p in points:
            g.add(p)
        self.assertEqual(70, g.getScore())

    def testTenthFrameSpare(self):
        g = Game()
        points = [
            1, 2,
            3, 4,
            5, 2,
            4, 3,
            4, 4,
            1, 6,
            7, 2,
            5, 4,
            3, 3,
            4, 6, 3
        ]
        for p in points:
            g.add(p)
        self.assertEqual(76, g.getScore())

    def testTenthFrameStrikeTwoThrows(self):
        g = Game()
        points = [
            1, 2,
            3, 4,
            5, 2,
            4, 3,
            4, 4,
            1, 6,
            7, 2,
            5, 4,
            3, 3,
            10, 6, 3
        ]
        for p in points:
            g.add(p)
        self.assertEqual(82, g.getScore())

    def testTenthFrameTwoStrikesOneThrow(self):
        g = Game()
        points = [
            1, 2,
            3, 4,
            5, 2,
            4, 3,
            4, 4,
            1, 6,
            7, 2,
            5, 4,
            3, 3,
            10, 10, 3
        ]
        for p in points:
            g.add(p)
        self.assertEqual(86, g.getScore())

    def testFullGame(self):
        g = Game()
        points = [
            1, 4,
            4, 5,
            6, 4,
            5, 5,
            10,
            0, 1,
            7, 3,
            6, 4,
            10,
            2, 8, 6
        ]
        for p in points:
            g.add(p)
        self.assertEqual(133, g.getScore())
