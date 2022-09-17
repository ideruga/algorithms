from unittest import TestCase
from .lanternfish import solve_lanternfish, solve_file


class Test(TestCase):
    def test_solve_lanterfish_single_fish(self):
        data = [0]

        result = solve_lanternfish(data, 80)
        self.assertEqual(1421, result)

    def test_solve_lanterfish_five_fishes(self):
        data = [3, 4, 3, 1, 2]
        result = solve_lanternfish(data, 80)
        self.assertEqual(5934, result)

    def test_solve_lanterfish_five_fishes_256(self):
        data = [3, 4, 3, 1, 2]
        result = solve_lanternfish(data, 256)
        self.assertEqual(26984457539, result)

    def test_solve_lanterfish_final_input_80_steps(self):
        result = solve_file("06 - lanternfish/input", 80)
        self.assertEqual(372300, result)

    def test_solve_lanterfish_final_input_256_steps(self):
        result = solve_file("06 - lanternfish/input", 256)
        self.assertEqual(1675781200288, result)


