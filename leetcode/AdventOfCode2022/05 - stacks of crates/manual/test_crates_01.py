from collections import deque
from unittest import TestCase
from crates_01 import CratesMaster


class TestCratesMaster(TestCase):
    def setUp(self):
        self.master = CratesMaster()

    def test_move_crates(self):
        input_lines = [line for line in open("test_data_01.txt")]
        self.master.arrange_crates(input_lines)
        self.assertEquals(self.master.crates[0:3], [deque(['C']), deque(['M']), deque(['P', 'D', 'N', 'Z'])])
        self.assertEquals(self.master.get_top_crates(), "CMZ")
