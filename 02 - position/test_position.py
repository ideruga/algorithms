from unittest import TestCase
from .position import find_position, find_position2

data = ["forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"]


class Test(TestCase):
    def test_find_position(self):
        self.assertEqual((15, 10), find_position(data))

    def test_find_position2(self):
        self.assertEqual((15, 60, 10), find_position2(data))
