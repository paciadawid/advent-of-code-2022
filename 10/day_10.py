with open("input.txt", "r", encoding="utf-8") as f:
    commands = [line.strip().split() for line in f.readlines()]

cycle, pixel = 0, 0
x = 1
signal_strength = 0
image, row = [], ""
for command in commands:
    for word in command:

        # part 2
        if x - 1 <= len(row) <= x + 1:
            row += "#"
        else:
            row += "."

        if len(row) == 40:
            image.append(row)
            row = ""

        try:
            x += int(word)
        except ValueError:
            pass
        cycle += 1

        # part 1
        if cycle % 40 == 20:
            signal_strength += cycle * x

print(signal_strength)
for line in image:
    print("".join([letter * 2 for letter in line]))
