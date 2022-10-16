from unittest import TestCase
from .sonars import solve_sonars, solve_file, get_scanner_positions_from_file, find_intersection


class Test(TestCase):
    def test_solve_sonars(self):
        scanners = get_scanner_positions_from_file("19 - sonars/test_input_3")
        intersections, got_intersection = find_intersection(set(scanners[0]), scanners[1], (0, 1, 2), (-1, 1, -1), 12)
        self.assertTrue(got_intersection)
        print(intersections)
        self.assertEqual(38, len(intersections))

