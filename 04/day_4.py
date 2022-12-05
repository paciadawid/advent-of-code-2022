with open("input.txt", "r") as f:
    sectors = []
    for line in f.readlines():
        sector = []
        for elf in line.strip().split(","):
            lower, upper = elf.split("-")
            elf_sector = set(range(int(lower), int(upper) + 1))
            sector.append(elf_sector)
        sectors.append(sector)

# part 1
overlapping_pairs = 0
for elf1, elf2 in sectors:
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        overlapping_pairs += 1
print(overlapping_pairs)

# part 2
overlapping_pairs = 0
for elf1, elf2 in sectors:
    if elf1.intersection(elf2):
        overlapping_pairs += 1
print(overlapping_pairs)
