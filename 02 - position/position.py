from functools import reduce

commands = {
    "forward": lambda distance: (distance, 0),
    "down": lambda depth: (0, depth),
    "up": lambda depth: (0, -depth),
}

commands2 = {
    "forward": lambda distance: (distance, 0, 0),
    "down": lambda depth: (0, 0, depth),
    "up": lambda depth: (0, 0, -depth),
}


def _add(a, b):
    return a[0] + b[0], a[1] + b[1]


def _add2(a, b):
    aim = a[2] + b[2]
    distance = a[0] + b[0]
    depth = a[1] + b[0] * aim
    return distance, depth, aim


def find_position(route):
    vectors = [commands[a.split(" ")[0]](int(a.split(" ")[1])) for a in route]

    return reduce(_add, vectors)


def find_position2(route):
    vectors = [commands2[a.split(" ")[0]](int(a.split(" ")[1])) for a in route]

    return reduce(_add2, vectors)


if __name__ == '__main__':
    with open("input", "r") as f:
        lines = [line.rstrip() for line in f.readlines()]

        final_position, final_depth = find_position(lines)
        print(f"Part 1: {final_position * final_depth}")

        final_position2, final_depth2, _ = find_position2(lines)
        print(f"Part 2: {final_position2 * final_depth2}")
