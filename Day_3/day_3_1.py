puzzle_input = [line.rsplit() for line in open("../puzzle_inputs/day_3_1.txt", "r")]
max_len = len(puzzle_input[0][0])
puzzle_len = len(puzzle_input)

def tree_num(x, y):
    trees = 0
    for i in range(0, puzzle_len, y):
        if puzzle_input[i][0][(x*(i//y)) % max_len] == "#":
            trees += 1
    return trees


def aboreal_trees():
    input_conditions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_val = 1
    for x, y in input_conditions:
        tree = tree_num(x, y)
        tree_val *= tree
    return tree_val
print("trees", aboreal_trees())
