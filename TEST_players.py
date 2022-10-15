import unittest
from main import players


class MyTestCase(unittest.TestCase):

    def test_addToAmbo(self):
        self.player1 = players()
        self.player1.addToAmbo(0)
        self.player1.addToAmbo(5)
        self.player1.addToAmbo(0)
        self.player1.addToAmbo(5)
        self.assertEqual(self.player1.ambo, [6+2,6,6,6,6,6+2])  # add assertion here

    def test_moveFromAmbo(self):
        self.player1 = players()
        self.player1.moveFromAmbo(0)
        self.player1.moveFromAmbo(5)
        self.assertEqual(self.player1.ambo, [6-1,6,6,6,6,6-1])  # add assertion here

        self.player1.moveFromAmbo(0)
        self.player1.moveFromAmbo(5)
        self.assertEqual(self.player1.ambo, [6-2,6,6,6,6,6-2])  # add assertion here

    def test_addToKalaha(self):
        self.player1 = players()
        self.player1.addToKalaha()
        self.assertEqual(self.player1.kalaha, 1)  # add assertion here

if __name__ == '__main__':
  unittest.main()
