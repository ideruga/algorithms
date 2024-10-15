from unittest import TestCase

from leetcode.daily.daily_2024_10_15 import Solution


class TestSolution(TestCase):
    def test_minimum_steps_100(self):
        self.assertEqual(2, Solution().minimumSteps("100"))

    def test_minimum_steps_101(self):
        self.assertEqual(1, Solution().minimumSteps("101"))

    def test_minimum_steps_0111(self):
        self.assertEqual(0, Solution().minimumSteps("0111"))
