with open("input.txt", "r") as f:
    games = [game.strip().split() for game in f.readlines()]

shape_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

winning_seq = [["A", "Y"], ["B", "Z"], ["C", "X"]]
draw_seq = [["A", "X"], ["B", "Y"], ["C", "Z"]]

total_score = 0
for game in games:
    if game in winning_seq:
        total_score += 6
    elif game in draw_seq:
        total_score += 3
    total_score += shape_score[game[1]]
print(total_score)

# part 2
game_map = {
    "A": {
        "X": shape_score["Z"],
        "Y": 3 + shape_score["X"],
        "Z": 6 + shape_score["Y"],
    },
    "B": {
        "X": shape_score["X"],
        "Y": 3 + shape_score["Y"],
        "Z": 6 + shape_score["Z"],
    },
    "C": {
        "X": shape_score["Y"],
        "Y": 3 + shape_score["Z"],
        "Z": 6 + shape_score["X"],
    },
}

total_score = sum([game_map[player_1][player_2] for player_1, player_2 in games])
print(total_score)
