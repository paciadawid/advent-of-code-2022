with open("input.txt") as f:
    backpacks = [backpack.strip() for backpack in f.readlines()]

# part 1
upper_offset = ord("A") - 27
lower_offset = ord("a") - 1

priority = 0
for backpack in backpacks:
    comp1, comp2 = backpack[:len(backpack) // 2], backpack.strip()[len(backpack) // 2:]
    shared = set(comp1).intersection(set(comp2))
    shared = next(iter(shared))
    if shared.isupper():
        priority += ord(shared) - upper_offset
    else:
        priority += ord(shared) - lower_offset
print(priority)

# part 2
priority = 0
group_size = 3
while len(backpacks) >= group_size:
    elves_found, backpacks_found, shared_items = 1, {backpacks[0]}, set(backpacks[0])
    for backpack in backpacks[1:]:
        if shared := shared_items.intersection(set(backpack)):
            shared_items = shared_items.intersection(shared)
            elves_found += 1
            backpacks_found.add(backpack)
        if elves_found == group_size:
            backpacks = [backpack for backpack in backpacks if backpack not in backpacks_found]
            shared = next(iter(shared_items))
            if shared.isupper():
                priority += ord(shared) - upper_offset
            else:
                priority += ord(shared) - lower_offset
            break
print(priority)
