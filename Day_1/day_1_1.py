puzzle_input = [int(line.rstrip()) for line in open("../puzzle_inputs/day_1_1.txt",  "r")]

def brute_force(input_list):
    final_sum = 0
    for num_i, i in enumerate(input_list):
        for num_j, j in enumerate(input_list):
            if num_i != num_j and i + j == 2020:
                final_sum += i * j
                input_list.remove(i)
                input_list.remove(j)
    return final_sum

answer = brute_force(puzzle_input)
print(answer)
