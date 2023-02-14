import re
from collections import deque


class CratesMaster:
    def __init__(self):
        self.actions = {'[': self.add_crates, 'm': self.move_crates, ' ': self.add_crates}
        self.crates = [deque([]) for _ in range(100)]

    def add_crates(self, input_string):
        for i, letter in enumerate(input_string):
            if letter != ' ': self.crates[i].appendleft(letter)

    def move_crates(self, input_string):
        (count, index_from, index_to) = re.search("move (\d+) from (\d+) to (\d+)", input_string).groups()
        (count, index_from, index_to) = (int(count), int(index_from) - 1, int(index_to) - 1)
        new_elements = deque([])
        for _ in range(count):
            new_elements.appendleft(self.crates[index_from].pop())
        self.crates[index_to].extend(new_elements)

    def pass_line(self, input_string):
        pass

    def arrange_crates(self, lines):
        [self.actions[line[0]](re.sub(r"\[(\w)\]\s?", r"\1", line).replace("    ", " ")) for line in lines]

    def get_top_crates(self):
        return "".join([stack.pop() for stack in self.crates if len(stack) > 0])

if __name__ == "__main__":
    input_lines = [line for line in open("data.txt")]
    master = CratesMaster()
    master.arrange_crates(input_lines)
    print(master.crates)
    print(master.get_top_crates())
