from unittest import TestCase
from crates_02 import get_top_crates

class Test(TestCase):

    def test_get_top_crates(self):
        input_lines = [line for line in open("test_data_01.txt")]
        self.assertEqual("MCD", get_top_crates(input_lines))

    def test_get_top_crates_real_data(self):
        input_lines = [line for line in open("data.txt")]
        self.assertEqual("RNRGDNFQG", get_top_crates(input_lines))

