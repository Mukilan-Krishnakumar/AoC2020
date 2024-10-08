puzzle_input = [line.rstrip() for line in open("../puzzle_inputs/day_2_1.txt", "r")]

valid_count = 0
for puzzle in puzzle_input:
    limit, character, input_str = puzzle.split(" ")
    character = character.strip(":")[0]
    lower, upper = [int(x) for x in limit.replace("-", " ").split(" ")]  
    if lower <= input_str.count(character) <= upper:
        valid_count += 1

print("Valid Count", valid_count)
