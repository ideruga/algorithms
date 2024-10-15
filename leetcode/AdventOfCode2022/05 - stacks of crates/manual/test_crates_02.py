from collections import deque
from unittest import TestCase
from crates_02 import CratesMaster


class TestCratesMaster(TestCase):
    def setUp(self):
        self.master = CratesMaster()

    def test_move_crates(self):
        input_lines = [line for line in open("test_data_01.txt")]
        self.master.arrange_crates(input_lines)
        self.assertEquals(self.master.crates[0:3], [deque(['M']), deque(['C']), deque(['P', 'Z', 'N', 'D'])])
        self.assertEquals(self.master.get_top_crates(), "MCD")
