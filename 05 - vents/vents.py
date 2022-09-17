import numpy

max_coordinate = 0


def split_coords(coords_string):
    global max_coordinate
    coords = tuple(map(int, coords_string.split(",")))

    max_coordinate = max([max_coordinate, *coords])

    return coords


def mark(lines, grid):
    c = 0
    for line in lines:
        start = line[0]
        end = line[1]
        # if start[0] == end[0] or start[1] == end[1]:
        i1 = start[0]
        i2 = end[0]
        j1 = start[1]
        j2 = end[1]

        length = max(abs(i2-i1), abs(j2-j1))+1
        delta_i = numpy.sign(i2-i1)
        delta_j = numpy.sign(j2-j1)
        for l in range(length):
            i = i1 + l*delta_i
            j = j1 + l*delta_j
            grid[i][j] += 1


def count(grid):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 1:
                cnt += 1
    return cnt


def solve_vents(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        lines = [line.rstrip().split(" -> ") for line in lines if line.strip() != ""]
        lines = [(split_coords(line[0]), split_coords(line[1])) for line in lines]
        grid = [[0] * (max_coordinate + 1) for i in range(max_coordinate + 1)]
        mark(lines, grid)
        return count(grid)


if __name__ == '__main__':
    result = solve_vents("input")
    print(f"Result: {result}")
    # print(f"Final Result Part I: {result[0]}")
    # print(f"Final Result Part II: {result[-1]}")
