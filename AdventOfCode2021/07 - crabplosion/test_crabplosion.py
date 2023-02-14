from unittest import TestCase
from .crabplosion import solve_file, solve_crabplosion2, solve_crabplosion


class Test(TestCase):
    def test_solve_crabplosion(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        result = solve_crabplosion(data)
        self.assertEqual(37, result)

    def test_solve_crabplosion2(self):
        data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        result = solve_crabplosion2(data)
        self.assertEqual(168, result)

    def test_solve_crabplosion2_real_input(self):
        result = solve_file("07 - crabplosion/input", solve_crabplosion)
        self.assertEqual(343468, result)

    def test_solve_crabplosion2_real_input2(self):
        result = solve_file("07 - crabplosion/input", solve_crabplosion2)
        self.assertEqual(96086265, result)
