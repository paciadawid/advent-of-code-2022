with open("input.txt", "r", encoding="utf-8") as f:
    commands = [line.strip().split() for line in f.readlines()]

directions_map = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0]
}


def calculate_move(head, tail):
    move = [0, 0]
    x_diff, y_diff = abs(head[0] - tail[0]), abs(head[1] - tail[1])
    if (x_diff > 1 and y_diff <= 1) or (x_diff >= 1 and y_diff >= 2):
        move[0] = 1 if head[0] > tail[0] else -1
    if (y_diff > 1 and x_diff <= 1) or (y_diff >= 1 and x_diff >= 2):
        move[1] = 1 if head[1] > tail[1] else -1
    return move


# part 1
rope_head, rope_tail, tail_locations = [0, 0], [0, 0], {(0, 0)}
for direction, moves in commands:
    for _ in range(int(moves)):
        rope_head[0] += directions_map[direction][0]
        rope_head[1] += directions_map[direction][1]
        x, y = calculate_move(rope_head, rope_tail)
        rope_tail[0] += x
        rope_tail[1] += y
        tail_locations.add(tuple(rope_tail))
print(len(tail_locations))

# part 2
rope, tail_locations = [[0, 0] for _ in range(10)], {(0, 0)}
for direction, moves in commands:
    for _ in range(int(moves)):
        rope[0][0] += directions_map[direction][0]
        rope[0][1] += directions_map[direction][1]
        for i in range(1, 10):
            x, y = calculate_move(rope[i - 1], rope[i])
            rope[i][0] += x
            rope[i][1] += y
        tail_locations.add(tuple(rope[-1]))
print(len(tail_locations))
