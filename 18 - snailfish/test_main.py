from unittest import TestCase, main

from parameterized import parameterized

from data import sum_test_data_1
from main import _add, split, add_to_left_number, explode, _sum, magnitude


class Test(TestCase):

    @parameterized.expand([
        ["[[9,1],[1,9]]", 129],
        ["[[1,2],[[3,4],5]]", 143],
        ["[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384],
        ["[[[[1,1],[2,2]],[3,3]],[4,4]]", 445],
        ["[[[[3,0],[5,3]],[4,4]],[5,5]]", 791],
        ["[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137],
        ["[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488],
    ])
    def test_magnitude(self, number, expected_result):
        result = magnitude(number)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"],
        # ["", "", ""],
        # ["", "", ""],
        # ["", "", ""],
    ])
    def test_add(self, left, right, expected_result):
        result = _add(left, right)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["[[[[1,1],[2,2]],[3,3]],[4,4]]", ["[1,1]", "[2,2]", "[3,3]", "[4,4]"]],
        ["[[[[3,0],[5,3]],[4,4]],[5,5]]", ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]"]],
        ["[[[[5,0],[7,4]],[5,5]],[6,6]]", ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"]],
        ["[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", sum_test_data_1],
        # ["", "", ""],
        # ["", "", ""],
    ])
    def test_sum(self, expected_result, arr):
        result = _sum(arr)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["[[[[0,7],4],[15,[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"],
        ["[[[[0,7],4],[[7,8],[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"],
        # ["", ""],
        # ["", ""],
    ])
    def test_split(self, number, expected_result):
        result, modified = split(number)
        self.assertTrue(modified)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        ["[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"],
        ["[[[[0,7],4],[7,[[8,4],9]]],[1,1]]", "[[[[0,7],4],[15,[0,13]]],[1,1]]"],
        ["[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"],
    ])
    def test_explode(self, string, expected_result):
        result, modified = explode(string)
        self.assertTrue(modified)
        self.assertEqual(expected_result, result)

    @parameterized.expand([
        [3, "[1,[2,[", "[1,[5,[0"],
        [7, "[1,[8,[", "[1,[15,[0"],
    ])
    def test_adjust_left(self, number, string, expected_result):
        result = add_to_left_number(number, string)
        self.assertEqual(expected_result, result)