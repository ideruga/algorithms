import re
from functools import reduce

split_pattern = re.compile(r"(\d{2})")


def split(s):
    search_result = split_pattern.search(s)
    print(f"Splitting {s}")
    if search_result:
        large_number = search_result.group(1)
        print(f"Found number: {large_number}")
        left = int(large_number) // 2
        right = left + int(large_number) % 2
        split_number = f"[{left},{right}]"
        result = s.replace(large_number, split_number, 1)
        return result, True
    return s, False


def _add(left, right):
    res = f"[{left},{right}]"
    modified = True
    print(f"Reducing: {res}")

    while modified:
        res, modified = explode(res)
        if modified:
            continue

        res, modified = split(res)
        print(f"Split result: {res}")
    return res


pair_pattern = re.compile(r"\[(\d+),(\d+)\]")


def magnitude(number):
    modified = True
    while modified:
        m = pair_pattern.search(number)
        if m:
            left = int(m.group(1))
            right = int(m.group(2))
            pos = m.start()
            length = len(m.group())
            number = "".join([number[:pos], str(left * 3 + right * 2), number[pos + length:]])
            print(f"New number: {number}")
        else:
            modified = False
    return int(number)


def _sum(list_to_sum):
    return reduce(_add, list_to_sum)


last_number_pattern = re.compile(r"(\d+)\D*$")


def add_to_left_number(number, s):
    m = last_number_pattern.search(s)
    if m:
        replacing = m.group(1)
        position = m.start(1)
        return "".join([s[:position], str(int(replacing) + number), s[position + len(replacing):]])
    else:
        return s


number_pattern = re.compile(r"(\d+).*")


def explode(number_string):
    result = ""
    level = 0
    skip_until_index = 0
    remainder_right = 0
    modified = False
    for i in range(len(number_string)):
        if i < skip_until_index:
            continue

        if number_string[i] == "[":
            level += 1
            if number_string[i + 1] != "[":
                pair = number_string[i:number_string.index("]", i) + 1]
                m = pair_pattern.match(pair)
                if m:
                    if level > 4 and not modified:
                        print(f"Exploding: {pair}")
                        remainder_left = int(m.group(1))
                        result = add_to_left_number(remainder_left, result)
                        result += "0"
                        remainder_right = int(m.group(2))
                        skip_until_index = i + len(pair)
                        modified = True
                        continue
        elif number_string[i] == "]":
            level -= 1

        elif remainder_right > 0 and number_string[i].isdigit():
            number = number_pattern.match(number_string, i).group(1)
            result += str(int(number) + remainder_right)
            remainder_right = 0
            skip_until_index = i + len(number)
            continue
        result += number_string[i]

    print(f"Explode result: {result}")
    return result, modified


def max_magnitude(lines):
    max_element = 0
    for number1 in lines:
        for number2 in lines:
            max_element = max(magnitude(_add(number1, number2)), max_element)

    return max_element


if __name__ == '__main__':
    with open("input") as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        mag = magnitude(_sum(lines))

        _max = max_magnitude(lines)

        print(f"Final Result Part I: {mag}")
        print(f"Final Result Part II: {_max}")
