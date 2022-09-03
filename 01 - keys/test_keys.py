from unittest import TestCase
from .keys import count_depth_window_increase, count_depth_increase

depths = [199,
          200,
          208,
          210,
          200,
          207,
          240,
          269,
          260,
          263,
          ]


class Test(TestCase):

    def test_count_depth_increase(self):
        self.assertEqual(7, count_depth_increase(depths))

    def test_count_depth_window_increase(self):
        self.assertEqual(5, count_depth_window_increase(depths))
