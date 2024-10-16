from unittest import TestCase

from leetcode.daily.daily_2024_10_16 import Solution


class TestSolution(TestCase):
    def test_minimum_steps_100(self):
        self.assertEqual("ccaccbcc", Solution().longestDiverseString(1, 1, 7))

    def test_minimum_steps_101(self):
        self.assertEqual("aabaa", Solution().longestDiverseString(7, 1, 0))
