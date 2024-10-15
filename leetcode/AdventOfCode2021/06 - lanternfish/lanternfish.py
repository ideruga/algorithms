import numpy
from numpy import cumsum


def solve_lanternfish(ages, iterations):

    school = [0] * iterations
    counts = [0] * iterations

    for a in ages:
        school[a] += 1
    for i in range(iterations):
        counts[i] += school[i]
        if i + 9 < len(school):
            school[i + 9] += school[i]
        if i + 7 < len(school):
            school[i + 7] += school[i]
    return sum(counts) + len(ages)


def solve_file(filename, iterations):
    with open(filename) as f:
        ages = list(map(int, f.readline().rstrip().split(",")))
        return solve_lanternfish(ages, iterations)


if __name__ == '__main__':
    result1 = solve_file("input", 80)
    result2 = solve_file("input", 256)
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
