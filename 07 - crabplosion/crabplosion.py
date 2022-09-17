import numpy
from numpy import cumsum


def calculate_cost(positions, position):
    left = [p for p in positions if p < position]
    right = [p for p in positions if p > position]

    return len(left) * position - sum(left) + sum(right) - len(right) * position


def solve_crabplosion(positions):
    costs = [0] * (len(positions))

    for i in range(len(positions)):
        costs[i] = calculate_cost(positions, i + 1)

    return min(costs)


cost_samples = []


def get_cost(position, target_position):
    delta = abs(target_position - position)
    return cost_samples[delta]


def calculate_cost2(positions, target_position):
    return sum([get_cost(p, target_position) for p in positions])


def solve_crabplosion2(positions):
    global cost_samples

    max_position = max(positions)
    cost_samples = cumsum([i for i in range(max_position+1)])
    costs = [0] * max_position

    for i in range(max_position):
        costs[i] = calculate_cost2(positions, i + 1)

    return min(costs)


def solve_file(filename, solve_function):
    with open(filename) as f:
        positions = list(map(int, f.readline().rstrip().split(",")))
        return solve_function(positions)


if __name__ == '__main__':
    result1 = solve_file("input", solve_crabplosion)
    result2 = solve_file("input", solve_crabplosion2)
    print(f"Result 1: {result1}")
    print(f"Result 2: {result2}")
