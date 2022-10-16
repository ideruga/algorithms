def same(coords_a, coords_b):
    for i in range(len(coords_a)):
        if coords_a[i] != coords_b[i]:
            return False
    return True


def get_delta(coords_a, coords_b):
    return [z[1] - z[0] for z in zip(coords_a, coords_b)]


def augment(scanner_a, scanner_b, delta):
    scanner_b = move_scanner(scanner_b, delta)
    for coord in scanner_b:
        if coord not in scanner_a:
            scanner_a.add(coord)
    return scanner_a


def move_scanner(scanner_b, delta):
    return [tuple(s[i] - delta[i] for i in range(len(delta))) for s in scanner_b]


def turn_scanner(scanner_b, negation, rotation):
    return [[s[rotation[r]] * negation[r] for r in range(len(rotation))] for s in scanner_b]


def find_intersection(scanner_a, scanner_b, rotation, negation, tolerance):
    scanner_b = turn_scanner(scanner_b, negation, rotation)

    for coord_a in scanner_a:
        for coord_b in scanner_b:
            delta = get_delta(coord_a, coord_b)
            intersections = get_intersection(scanner_a, scanner_b, delta)
            if intersections >= tolerance:
                # print(f"Trying delta {delta}")
                # print(f"Intersections: {intersection}")
                return (delta, rotation, negation), True
    return None, False


def get_intersection(scanner_a, scanner_b, delta):
    intersections = 0
    scanner_b = move_scanner(scanner_b, delta)

    for coord_a in scanner_a:
        if coord_a in scanner_b:
            intersections += 1
    return intersections


negations = [
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 1),
    (-1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (-1, -1, -1)
]

rotations = [
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),  # x
    (2, 1, 0),
    (1, 0, 2),
    (0, 2, 1)  # x
]


def adjust_scanner(scanner, scanner_transforms, scanner_marks, i):
    # prnt = i == 2
    while i != 0:
        delta, rotation, negation = scanner_transforms[i]
        # if prnt:
        #     print(f"Turning for {rotation}, n: {negation}, moving: {delta}")
        turned = turn_scanner(scanner, negation, rotation)
        scanner = move_scanner(turned, delta)
        i = scanner_marks[i]
        print(f"Next i: {i}")

    return scanner


def join_scanners(scanners, scanner_transforms, scanner_marks):
    result = set(scanners[0])
    # print(f"First result size: {len(result)}")

    for i in range(1, len(scanners)):
        print(f"Adjusting the scanner {i}")
        scanner_in_potition_0 = adjust_scanner(scanners[i], scanner_transforms, scanner_marks, i)
        # print(f"Scanner {i} in position 0: {scanner_in_potition_0}")
        result = result.union(scanner_in_potition_0)
        # print(f"Result size: {len(result)}")

    return result


def solve_sonars(scanners, tolerance):
    scanner_marks = [-1] * len(scanners)
    scanner_transforms = [(0, (0, 1, 2), (1, 1, 1))] * len(scanners)
    scanner_marks[0] = 0
    for i, s1 in enumerate(scanners):
        for j, s2 in enumerate(scanners):
            if j == i or scanner_marks[j] >= 0:
                continue
            print(f"Comparing scanners {i} and {j}")
            transform, found = augment_via_intersection(s1, s2, tolerance)
            if found and scanner_marks[i] != j:
                scanner_marks[j] = i
                scanner_transforms[j] = transform

        print(f"Intersections: {scanner_marks}")

    return len(join_scanners(scanners, scanner_transforms, scanner_marks))


def augment_via_intersection(scanner_a, scanner_b, tolerance):
    for r in rotations:
        for n in negations:
            transform, found = find_intersection(scanner_a, scanner_b, r, n, tolerance)
            if found:
                return transform, True
    return None, False


def get_scanner_positions_from_file(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f.readlines()]
        line_index = 0
        scanner_index = 0
        scanners = []
        while line_index < len(lines):
            scanner = []
            line_index += 1
            while line_index < len(lines) and lines[line_index] != '':
                coords = tuple(map(int, lines[line_index].split(",")))
                scanner.append(coords)
                line_index += 1
            line_index += 1
            scanners.append(scanner)
            scanner_index += 1
        return scanners


def solve_file(filename, tolerance):
    scanners = get_scanner_positions_from_file(filename)
    return solve_sonars(scanners, tolerance)


if __name__ == '__main__':
    # result1 = solve_file("test_input_1", 1)
    # print(f"Result 1: {result1}")
    # result2 = solve_file("test_input_2", 12)
    # print(f"Result 2: {result2}")
    result4 = solve_file("test_input_4", 12)
    print(f"Result 4: {result4}")
