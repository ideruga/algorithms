def count_depth_increase(depths):
    return len([x for i, x in enumerate(depths) if i < len(depths) - 1 and x < depths[i + 1]])


def count_depth_window_increase(depths):
    return len([x for i, x in enumerate(depths) if i < len(depths) - 3 and x < depths[i + 3]])


if __name__ == '__main__':
    with open("input", "r") as f:
        lines = [int(line.rstrip()) for line in f.readlines()]

        count = count_depth_increase(lines)
        windows_count = count_depth_window_increase(lines)

        print(count)
        print(windows_count)
