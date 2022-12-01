with open("input.txt", "r") as f:
    calories, elf = [], []
    for line in f.readlines():
        if line.strip():
            elf.append(int(line))
        else:
            calories.append(elf)
            elf = []

calories_sums = [sum(elf) for elf in calories]

# part 1
print(max(calories_sums))

# part 2
print(sum(sorted(calories_sums)[-3:]))
