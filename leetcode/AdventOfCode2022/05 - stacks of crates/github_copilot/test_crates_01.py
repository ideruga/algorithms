from unittest import TestCase
from crates_01 import get_top_crates

class Test(TestCase):

    def test_get_top_crates(self):
        input_lines = [line for line in open("test_data_01.txt")]
        self.assertEqual("CMZ", get_top_crates(input_lines))

    def test_get_top_crates_real_data(self):
        input_lines = [line for line in open("data.txt")]
        self.assertEqual("FWNSHLDNZ", get_top_crates(input_lines))

