from functools import cmp_to_key

def compare_strings(a, b):
    a = a.lower()
    b = b.lower()
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


def walk_sort(a, b):
    limit = min(len(a), len(b))
    for i in range(limit):
        if a[i] == b[i]:
            if (len(a) == i + 1 and len(b) == i + 1):
                return 0
            else:
                continue
        a_is_file = len(a) == i + 1
        b_is_file = len(b) == i + 1
        if (a_is_file and b_is_file) or (not a_is_file and not b_is_file):
            return compare_strings(a[i], b[i])
        else:
            return 1 if a_is_file else (-1 if b_is_file else compare_strings(a[i], b[i]))


with open("input.txt", "r") as f:
    lines = [line.strip().replace("_", " ").split("\\") for line in f.readlines()]
    # sort lines using custom comparator
    lines.sort(key=cmp_to_key(walk_sort))
    result = ["\\".join(line).replace(" ", "_") for line in lines]
    with open("output.txt", "r") as f2:
        compare_lines = [line.strip() for line in f2.readlines()]
        for i in range(len(compare_lines)):
            if result[i] != compare_lines[i]:
                print(i, result[i], compare_lines[i])
                break
