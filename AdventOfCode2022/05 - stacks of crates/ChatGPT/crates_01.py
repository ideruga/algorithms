def solve(stacks, moves):
    for move in moves:
        source_stack, target_stack = move.split(" from ")[1].split(" to ")
        source_stack, target_stack = int(source_stack) - 1, int(target_stack) - 1
        crate = stacks[source_stack].pop()
        stacks[target_stack].append(crate)
    return "".join(stacks[i][-1] for i in range(len(stacks)))

with open("test_data_01.txt", "r") as f:
    lines = f.readlines()

stacks = []
moves = []
for line in lines:
    if "[" in line:
        stack = line.strip().replace("[", "").replace("]", "").split()
        stacks.append([c for c in stack if c.isalpha()])
    else:
        moves.append(line.strip())

print(solve(stacks, moves)) # Output: "CMZ"