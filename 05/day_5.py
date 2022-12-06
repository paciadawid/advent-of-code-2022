import copy

with open("input.txt", "r") as f:
    lines = f.readlines()
    num_of_stacks = len(lines[1]) // 4
    stacks: list[list[str]] = [[] for _ in range(num_of_stacks)]
    actions = []
    for line in lines:
        if "[" in line:
            for i in range(num_of_stacks):
                if crate := line[1 + 4 * i].strip():
                    stacks[i].insert(0, crate)
        elif "move" in line:
            action = {}
            words = line.strip().split()
            for i in range(0, len(words), 2):
                action[words[i]] = int(words[i + 1])
            actions.append(action)
print(stacks)
# part 1
stacks_copy = copy.deepcopy(stacks)
for action in actions:
    for _ in range(action["move"]):
        stacks[action["to"] - 1].append(stacks[action["from"] - 1].pop())
print("".join([crates[-1] for crates in stacks]))

# part 2
stacks = stacks_copy
for action in actions:
    crates_to_move = []
    for _ in range(action["move"]):
        crates_to_move.append(stacks[action["from"] - 1].pop())
    stacks[action["to"] - 1].extend(crates_to_move[::-1])
print("".join([crates[-1] for crates in stacks]))
