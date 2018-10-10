from dev.Frame import Frame
import unittest


class TestFrame(unittest.TestCase):

    def testNoThrows(self):
        f = Frame()
        self.assertEqual(0, f.getScore())
        self.assertEqual(None, f.getResult())
        self.assertEqual(0, f.getThrows())

    def testOneThrow(self):
        f = Frame()
        f.add(5)
        self.assertEqual(5, f.getScore())
        self.assertEqual(None, f.getResult())
        self.assertEqual(1, f.getThrows())

    def testOpenStatus(self):
        f = Frame()
        f.add(5)
        f.add(4)
        self.assertEqual(9, f.getScore())
        self.assertEqual("open", f.getResult())
        self.assertEqual(2, f.getThrows())

    def testSpareStatus(self):
        f = Frame()
        f.add(5)
        f.add(5)
        self.assertEqual(10, f.getScore())
        self.assertEqual("spare", f.getResult())
        self.assertEqual(2, f.getThrows())

    def testStrikeStatus(self):
        f = Frame()
        f.add(10)
        self.assertEqual(10, f.getScore())
        self.assertEqual("strike", f.getResult())
        self.assertEqual(1, f.getThrows())
