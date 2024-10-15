# Create a function that does the following 3 steps:
# 1. among all the lines, find the line that only contains numbers and spaces. Get indexes of all numbers in the line.
# 2. starting at this line, go backwards and extract the characters that correspond to the number indexes from the previous step.
# 3. Print out the result

def get_top_crates(input_lines):
    indexes = []
    # find the line that only contains numbers and spaces
    for i, line in enumerate(input_lines):
        if line.replace(" ", "").strip().isdigit():
            # get the indexes of all numbers in the line
            indexes = [j for j, char in enumerate(line) if char.isdigit()]
            # loop backwards to zero and extract the characters that correspond to the number indexes
            stacks = []
            for k, index in enumerate(indexes):
                stack = [input_line[index] for input_line in input_lines[i - 1::-1] if
                         len(input_line) > index and input_line[index] != " "]
                stacks.append(stack)

            # loop forwards from line i+2 and move crates according to the rules:
            # 1. parse the line using the format: move <count> crates from <source> to <destination>
            # 2. take one crate from the source stack and put it on the destination stack
            # 3. repeat <count> times
            for line in input_lines[i + 2:]:
                if line.startswith("move"):
                    count, _, source, _, destination = line.split(" ")[1:]
                    count = int(count)
                    for _ in range(count):
                        crate = stacks[int(source) - 1].pop()
                        stacks[int(destination) - 1].append(crate)

            # for every element of stacks array, take the last crate and concatenate them all into a string
            return "".join([stack[-1] for stack in stacks])


# only if executed as a script:
if __name__ == "__main__":
    # read input lines from a file and store them in a list
    input_lines = [line for line in open("data.txt")]

    print(get_top_crates(input_lines))
