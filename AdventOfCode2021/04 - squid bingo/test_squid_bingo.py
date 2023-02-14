from unittest import TestCase
from .squid_bingo import count_frequences, most_frequent, least_frequent, reduce_to_single_number, to_numbers, \
    most_frequent_criterion, least_frequent_criterion

data = ["00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"]


class Test(TestCase):
    def test_count_frequencies(self):
        vector_length = 5
        numbers = to_numbers(data, vector_length)
        frequencies = count_frequences(numbers, vector_length)
        self.assertEqual([7, 5, 8, 7, 5], frequencies)

    def test_most_frequent(self):
        vector_length = 5
        numbers = to_numbers(data, vector_length)
        frequencies = count_frequences(numbers, vector_length)
        self.assertEqual(22, most_frequent(frequencies, len(data)))

    def test_least_frequent(self):
        vector_length = 5
        numbers = to_numbers(data, vector_length)
        frequencies = count_frequences(numbers, vector_length)
        most = most_frequent(frequencies, len(data))
        self.assertEqual(9, least_frequent(most, 5))

    def test_reduction_least(self):
        vector_length = 5
        numbers = to_numbers(data, vector_length)
        reduced = reduce_to_single_number(numbers, vector_length, most_frequent_criterion)
        self.assertEqual(23, reduced)

    def test_reduction_most(self):
        vector_length = 5
        numbers = to_numbers(data, vector_length)
        reduced = reduce_to_single_number(numbers, vector_length, least_frequent_criterion)
        self.assertEqual(10, reduced)


