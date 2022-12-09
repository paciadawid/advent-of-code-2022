from functools import reduce

with open("input.txt", "r", encoding="utf-8") as f:
    trees = [[int(tree) for tree in line.strip()] for line in f.readlines()]

column, row = len(trees[0]), len(trees)


def check_visibility_and_scenic(x_tree, y_tree, trees_map):
    visible_directions = [True, True, True, True]
    scenic_scores = [0, 0, 0, 0]
    tree_height = trees_map[y_tree][x_tree]
    if x_tree in (0, column - 1) or y_tree in (0, row - 1):
        return True, 0
    for x_ in range(x_tree)[::-1]:
        scenic_scores[0] += 1
        if trees_map[y_tree][x_] >= tree_height:
            visible_directions[0] = False
            break
    for x_ in range(x_tree + 1, column):
        scenic_scores[1] += 1
        if trees_map[y_tree][x_] >= tree_height:
            visible_directions[1] = False
            break
    for y_ in range(y_tree)[::-1]:
        scenic_scores[2] += 1
        if trees_map[y_][x_tree] >= tree_height:
            visible_directions[2] = False
            break
    for y_ in range(y_tree + 1, row):
        scenic_scores[3] += 1
        if trees_map[y_][x_tree] >= tree_height:
            visible_directions[3] = False
            break
    scenic_score = reduce((lambda a, b: a * b), scenic_scores)
    return any(visible_directions), scenic_score


# part 1
visible_trees = 0
for y in range(row):
    for x in range(column):
        visible_trees += check_visibility_and_scenic(x, y, trees)[0]
print(visible_trees)

# part 2
highest_scenic = 0
for y in range(row):
    for x in range(column):
        if (new_highest := check_visibility_and_scenic(x, y, trees)[1]) > highest_scenic:
            highest_scenic = new_highest
print(highest_scenic)
