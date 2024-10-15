import numpy as np


def read_card(card_lines):
    return np.array([card_lines[i * 5:(i + 1) * 5] for i in range(len(card_lines) // 5)], dtype=int)


def read_cards(card_lines):
    return [read_card(card_lines[i * 25:(i + 1) * 25]) for i in range(len(card_lines) // 25)]


def mark(n, cards, marks):
    for i in range(len(cards)):
        for j in range(len(cards[i])):
            for k in range(len(cards[i][j])):
                if n == cards[i][j][k]:
                    marks[i][j][k] = True


def solved(marks):
    for i in range(len(marks)):
        mark = marks[i]
        mark_t = mark.transpose()
        for j in range(len(mark)):
            if mark[j].sum() == 5 or mark_t[j].sum() == 5:
                return i
    return -1


def calculate_solution(card, mark, n):
    values = [card[i][j] for i in range(len(card)) for j in range(len(card[i])) if not mark[i][j]]
    return n * sum(values)


def solve(cards, marks, numbers):
    scores = []
    for n in numbers:
        mark(n, cards, marks)
        while True:
            position = solved(marks)
            if position < 0:
                break
            score = calculate_solution(cards[position], marks[position], n)
            scores.append((position, score))
            del cards[position]
            marks = np.delete(marks, position, axis=0)
            if len(cards) == 0:
                break

    return scores


def solve_bingo(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines if line.strip() != ""]
        random_numbers = map(int, lines[0].split(","))

        cards = [int(el) for line in lines[1:] for el in line.split(" ") if el != ""]
        cards = read_cards(cards)

        marks = np.array([[[False] * 5 for i in range(5)] for j in range(len(cards))], dtype=bool)

        return solve(cards, marks, random_numbers)


if __name__ == '__main__':
    result = solve_bingo("input")
    print(f"Result: {result}")
    print(f"Final Result Part I: {result[0]}")
    print(f"Final Result Part II: {result[-1]}")
