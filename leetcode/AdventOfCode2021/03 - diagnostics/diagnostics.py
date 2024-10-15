from functools import reduce
from operator import add

base_vectors = []


def freq(results, number):
    return map(add, results, number)


def to_numbers(lines, vector_length):
    global base_vectors

    base_vectors = [0b1 << n for n in reversed(range(vector_length))]

    b_numbers = [int(line, 2) for line in lines]
    return [[(n & b) // b for b in base_vectors] for n in b_numbers]


def count_frequences(numbers, vector_length):
    results = [0] * vector_length
    results = reduce(freq, numbers, results)

    return list(results)


def most_frequent(frequencies, count):
    result = ["1" if frq > count // 2 else "0" for frq in frequencies]
    return convert(result)


def least_frequent(most_frequent_element, length):
    base = int("".join(["1"] * length), 2)
    return (~most_frequent_element) & base


def convert(numbers):
    return int("".join(numbers), 2)


def reduce_to_single_number(numbers, vector_length, criterion):
    for i in range(vector_length):
        frequencies = count_frequences(numbers, vector_length)
        selection_bit = criterion(frequencies[i], len(numbers))
        numbers = [n for n in numbers if not (bool(n[i]) ^ selection_bit)]
        if len(numbers) == 1:
            break

    return convert(map(str, numbers[0]))


def most_frequent_criterion(a, l):
    return a > l // 2 or (l % 2 == 0 and a == l // 2)


def least_frequent_criterion(a, l):
    return a < l // 2 + l % 2


if __name__ == '__main__':
    with open("input", "r") as f:
        lines = [line.rstrip() for line in f.readlines()]

        vector_length = len(lines[0])
        numbers = to_numbers(lines, vector_length)
        frequencies = count_frequences(numbers, vector_length)
        most = most_frequent(frequencies, len(lines))
        least = least_frequent(most, len(lines[0]))
        print(f"Part 1: {most * least}")

        single_number_1 = reduce_to_single_number(numbers, vector_length, most_frequent_criterion)
        single_number_2 = reduce_to_single_number(numbers, vector_length, least_frequent_criterion)
        print(f"Part 2: {single_number_1 * single_number_2}")
