puzzle_input = [line.rstrip() for line in open("../puzzle_inputs/day_2_1.txt", "r")]

valid_count = 0
for puzzle in puzzle_input:
    limit, character, input_str = puzzle.split(" ")
    character = character.strip(":")[0]
    position_1, position_2 = [int(x) for x in limit.replace("-", " ").split(" ")]  
    statement_1 = input_str[position_1 - 1] == character
    statement_2 = input_str[position_2 - 1] == character
    if (statement_1 and not statement_2) or (not statement_1 and statement_2):
        valid_count += 1
print("Valid Count", valid_count)
